import argparse
import keyboard

from .commands import register_commands
from .devices import choose_device
from .recorder import Recorder


def main():
    parser = argparse.ArgumentParser(
        description="ContextRecorder"
    )

    parser.add_argument(
        "--chunks",
        action="store_true",
        help="Record audio in chunks"
    )

    parser.add_argument(
        "--chunk-seconds",
        type=int,
        default=10,
        help="Chunk duration in seconds (default: 10)"
    )

    parser.add_argument(
        "--output-dir",
        default="recordings",
        help="Directory where chunks will be saved"
    )

    args = parser.parse_args()

    device_type, device_index = choose_device()

    recorder = Recorder(
        device_type=device_type,
        device_index=device_index
    )

    if args.chunks:
        print("Starting chunk recording mode...")
        print(f"Chunk duration: {args.chunk_seconds}s")
        print(f"Output folder: {args.output_dir}")

        recorder.record_chunks(
            output_dir=args.output_dir,
            chunk_seconds=args.chunk_seconds
        )
        return

    register_commands(recorder)

    print("ContextRecorder started.")
    print("Press s to start, x to stop, q to quit.")

    keyboard.wait("q")

    print("Exiting...")


if __name__ == "__main__":
    main()