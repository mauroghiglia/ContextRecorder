import keyboard
from recorder import Recorder
from commands import register_commands
from devices import list_devices

list_devices()


def main():
    recorder = Recorder()

    register_commands(recorder)

    print("ContextSuggest started.")

    keyboard.wait("q")

    print("Exiting...")


if __name__ == "__main__":
    main()