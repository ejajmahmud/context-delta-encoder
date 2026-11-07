"""CLI for context-delta-encoder."""
import sys
import argparse
from .encoder import ContextDeltaEncoder


def main():
    parser = argparse.ArgumentParser(description="Context Delta Encoder")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    args = parser.parse_args()

    if args.demo:
        t1 = "line 1: init\nline 2: config=False\nline 3: done"
        t2 = "line 1: init\nline 2: config=True\nline 3: done"
        patch = ContextDeltaEncoder.create_patch(t1, t2)
        print(f"Created patch: {len(patch.diff_lines)} diff lines")
        print("Diff:")
        print("".join(patch.diff_lines))
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
