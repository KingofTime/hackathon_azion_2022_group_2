import threading
import os
import argparse


def run(semaphore: threading.BoundedSemaphore, link: str):
    semaphore.acquire()
    print(link)
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

    semaphore = threading.BoundedSemaphore(value=max_workers)
    with open(input_path, "r") as file:
        for link in file.readlines():
            thread = threading.Thread(target=run, args=(semaphore, link))
            thread.start()