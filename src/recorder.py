import os
import threading
from datetime import datetime

import numpy as np
import soundfile as sf

from devices import get_input_device


class Recorder:
    def __init__(
        self,
        sample_rate=48000,
        chunk_seconds=1,
        device_type="speaker",
        device_index=0,
        output_dir="recordings",
    ):
        self.sample_rate = sample_rate
        self.chunk_seconds = chunk_seconds
        self.device_type = device_type
        self.device_index = device_index
        self.output_dir = output_dir

        self.device = get_input_device(device_type, device_index)

        self.recording = False
        self.audio_data = []
        self.thread = None

        os.makedirs(self.output_dir, exist_ok=True)

    def _record_loop(self):
        try:
            with self.device.recorder(samplerate=self.sample_rate) as recorder:
                while self.recording:
                    chunk = recorder.record(
                        numframes=self.sample_rate * self.chunk_seconds
                    )

                    if chunk is not None and chunk.size > 0:
                        self.audio_data.append(chunk)

        except Exception as error:
            print(f"Recording error: {error}")
            self.recording = False

    def start_recording(self):
        if self.recording:
            print("Already recording.")
            return

        print(f"Recording from: {self.device.name}")

        self.audio_data = []
        self.recording = True

        self.thread = threading.Thread(
            target=self._record_loop,
            daemon=True
        )
        self.thread.start()

    def stop_recording(self):
        if not self.recording:
            print("Not recording.")
            return

        print("Stopping recording...")

        self.recording = False

        if self.thread:
            self.thread.join()
            self.thread = None

        if not self.audio_data:
            print("No audio captured.")
            return

        audio = np.concatenate(self.audio_data, axis=0)
        audio = self._normalize(audio)

        filename = self._build_filename()
        sf.write(filename, audio, self.sample_rate)

        print(f"Saved: {filename}")

    def _normalize(self, audio):
        max_value = np.max(np.abs(audio))

        if max_value > 0:
            return audio / max_value * 0.9

        return audio

    def _build_filename(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        source = f"{self.device_type}_{self.device_index}"

        return os.path.join(
            self.output_dir,
            f"{source}_{timestamp}.wav"
        )