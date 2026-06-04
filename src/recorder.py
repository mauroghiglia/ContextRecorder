import os
import threading
from datetime import datetime
from devices import get_input_device

import numpy as np
import soundcard as sc
import soundfile as sf


class Recorder:
    def __init__(self, sample_rate=48000, chunk_seconds=1, device_type="speaker", device_index=0):
        self.sample_rate = sample_rate
        self.chunk_seconds = chunk_seconds
        self.recording = False
        self.audio_data = []
        self.thread = None
        self.device = get_input_device(device_type, device_index)

        os.makedirs("recordings", exist_ok=True)

    def _record_loop(self):
        with self.device.recorder(samplerate=self.sample_rate) as recorder:
            while self.recording:
                chunk = recorder.record(
                    numframes=self.sample_rate * self.chunk_seconds
                )
                self.audio_data.append(chunk)

        with mic.recorder(samplerate=self.sample_rate) as recorder:
            while self.recording:
                chunk = recorder.record(
                    numframes=self.sample_rate * self.chunk_seconds
                )
                self.audio_data.append(chunk)

    def start_recording(self):
        if self.recording:
            print("Already recording.")
            return

        print(f"Recording Windows audio from: {self.speaker.name}")

        self.audio_data = []
        self.recording = True

        self.thread = threading.Thread(target=self._record_loop)
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

        max_value = np.max(np.abs(audio))
        if max_value > 0:
            audio = audio / max_value * 0.9

        filename = datetime.now().strftime("recordings/windows_speakers_%Y%m%d_%H%M%S.wav")
        sf.write(filename, audio, self.sample_rate)

        print(f"Saved: {filename}")