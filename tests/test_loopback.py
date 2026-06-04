import sounddevice as sd
import soundfile as sf

duration = 10
device = 8  # Speakers WASAPI

device_info = sd.query_devices(device)
samplerate = int(device_info["default_samplerate"])

print("Recording Windows audio...")

audio = sd.rec(
    int(duration * samplerate),
    samplerate=samplerate,
    channels=2,
    dtype="float32",
    device=(device, None),
)

sd.wait()

sf.write("recordings/windows_audio.wav", audio, samplerate)

print("Saved.")