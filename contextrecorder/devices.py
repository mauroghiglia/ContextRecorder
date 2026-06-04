import soundcard as sc


def list_devices():
    print("\nAvailable recording devices:\n")

    for i, speaker in enumerate(sc.all_speakers()):
        print(f"speaker:{i}  {speaker.name}")

    for i, mic in enumerate(sc.all_microphones()):
        print(f"mic:{i}      {mic.name}")


def parse_device_selection(selection):
    try:
        device_type, index = selection.strip().lower().split(":")
        index = int(index)
    except ValueError:
        raise ValueError("Use format speaker:0 or mic:0")

    if device_type not in ("speaker", "mic"):
        raise ValueError("Device type must be speaker or mic")

    return device_type, index


def get_input_device(device_type, index):
    if device_type == "speaker":
        speakers = sc.all_speakers()
        selected = speakers[index]

        return sc.get_microphone(
            id=str(selected.name),
            include_loopback=True
        )

    if device_type == "mic":
        microphones = sc.all_microphones()
        return microphones[index]

    raise ValueError("Device type must be speaker or mic")


def choose_device():
    list_devices()

    while True:
        try:
            selection = input(
                "\nSelect device (speaker:0, mic:0) or q to quit: "
            ).strip().lower()

            if selection in ("q", "quit", "exit"):
                print("Exiting...")
                raise SystemExit(0)

            device_type, index = parse_device_selection(selection)
            device = get_input_device(device_type, index)

            print(f"\nSelected: {device.name}\n")
            return device_type, index

        except KeyboardInterrupt:
            print("\nExiting...")
            raise SystemExit(0)

        except (ValueError, IndexError) as error:
            print(f"Invalid selection: {error}")