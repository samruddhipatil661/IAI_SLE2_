"""Small in-process sampling profiler inspired by py-spy's sampling approach.

It periodically samples the current Python call stack while main.py runs.
This is useful when py-spy cannot be installed on an offline machine.
"""

import runpy
import sys
import threading
import time
from collections import Counter

SAMPLE_HZ = 200
DURATION = 2.0


def profiler(samples, stop_event):
    interval = 1.0 / SAMPLE_HZ
    main_thread = threading.main_thread()

    while not stop_event.is_set():
        frame = sys._current_frames().get(main_thread.ident)
        if frame is not None:
            stack = []
            while frame is not None:
                stack.append(frame.f_code.co_name)
                frame = frame.f_back
            samples.append(";".join(reversed(stack)))
        time.sleep(interval)


def main():
    samples = []
    stop_event = threading.Event()
    thread = threading.Thread(target=profiler, args=(samples, stop_event), daemon=True)
    thread.start()

    try:
        runpy.run_path("main.py", run_name="__main__")
    finally:
        stop_event.set()
        thread.join(timeout=1)

    counts = Counter(samples)
    print(f"\nSampling profile: {len(samples)} samples @ {SAMPLE_HZ} Hz")
    print("Top sampled call stacks:")
    for stack, count in counts.most_common(10):
        print(f"{count:4d}  {stack}")


if __name__ == "__main__":
    main()
