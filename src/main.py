import keyboard

from commands import register_commands
from devices import choose_device
from recorder import Recorder


def main():
    device_type, device_index = choose_device()

    recorder = Recorder(
        device_type=device_type,
        device_index=device_index
    )

    register_commands(recorder)

    print("ContextRecorder started.")
    print("Press s to start, x to stop, q to quit.")

    keyboard.wait("q")

    print("Exiting...")


if __name__ == "__main__":
    main()