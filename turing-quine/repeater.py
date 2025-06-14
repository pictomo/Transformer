#!/usr/bin/env python3

import sys
import subprocess
from time import sleep

wait_time = 0.05


def run_main():
    try:
        # execute main.py
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)

        # print output
        print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, file=sys.stderr)

        return result.returncode == 0
    except Exception as e:
        print(f"repeater: error: {e}", file=sys.stderr)
        return False


def main():
    print("repeater: starting turing machine")
    print("repeater: Ctrl+C to stop")

    try:
        while True:
            sleep(wait_time)
            if not run_main():
                print("repeater: turing machine stopped")
                break
    except KeyboardInterrupt:
        print("repeater: finish execution")


if __name__ == "__main__":
    main()
