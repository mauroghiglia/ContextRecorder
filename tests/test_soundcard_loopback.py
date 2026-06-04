# tests/test_soundcard_loopback.py

import soundcard as sc
import soundfile as sf

duration = 10
samplerate = 48000

speaker = sc.default_speaker()

print("Default speaker:", speaker.name)
print("Recording Windows audio...")

with sc.get_microphone(id=str(speaker.name), include_loopback=True).recorder(samplerate=samplerate) as recorder:
    audio = recorder.record(numframes=samplerate * duration)

sf.write("recordings/windows_audio.wav", audio, samplerate)

print("Saved: recordings/windows_audio.wav")