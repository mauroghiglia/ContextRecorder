import keyboard


def register_commands(recorder):
    print("Commands:")
    print("  s = start recording")
    print("  x = stop recording")
    print("  q = quit")

    keyboard.add_hotkey("s", recorder.start_recording)
    keyboard.add_hotkey("x", recorder.stop_recording)