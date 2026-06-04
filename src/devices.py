import soundcard as sc


def list_devices():
    print("\nSpeakers / loopback-capable outputs:")
    for i, speaker in enumerate(sc.all_speakers()):
        print(f"  speaker:{i}  {speaker.name}")

    print("\nMicrophones:")
    for i, mic in enumerate(sc.all_microphones()):
        print(f"  mic:{i}      {mic.name}")


def get_input_device(device_type="speaker", index=0):
    if device_type == "speaker":
        devices = sc.all_speakers()
        return sc.get_microphone(
            id=str(devices[index].name),
            include_loopback=True
        )

    if device_type == "mic":
        devices = sc.all_microphones()
        return devices[index]

    raise ValueError("device_type must be 'speaker' or 'mic'")