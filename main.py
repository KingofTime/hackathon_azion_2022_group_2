import threading
import os
import argparse

from mvp import Routine


def run(
        semaphore: threading.BoundedSemaphore, 
        link: str,
        routine: Routine
    ):
    semaphore.acquire()
    routine(link)
    semaphore.release()

MAX_WORKERS = 4
DEFAULT_INPUT_PATH = os.path.join("data", "links.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--workers", action="store", type=int)
    parser.add_argument("-i", "--input_path", action="store", type=int)
    args = parser.parse_args()

    max_workers = MAX_WORKERS
    input_path = DEFAULT_INPUT_PATH

    if args.workers:
        max_workers = args.workers

    if args.input_path:
        input_path = args.input_path

    routine = Routine("7b787f05-651f-4d29-b653-6704497d7536")
    semaphore = threading.BoundedSemaphore(value=max_workers)
    with open(input_path, "r") as file:
        for link in file.readlines():
            thread = threading.Thread(target=run, args=(semaphore, link, routine))
            thread.start()