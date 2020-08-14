import time
from threading import Thread
from concurrent import futures


def some_process(seconds):
    """Function for processing"""
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print(f'Woke up after {seconds} second(s)')


def multithreading_concurrent(seconds):
    """Short way of multithreading with the concurrent module"""
    with futures.ThreadPoolExecutor() as executor:
        executor.map(some_process, seconds)


def multithreading_threading(seconds):
    """Manual way of multithreading with the threading module"""
    threads = []

    for s in seconds:
        t = Thread(target=some_process, args=[s])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    BEGIN = time.perf_counter()
    secs = [1, 2, 3, 4, 5]

    multithreading_threading(secs)      # with the threading module
    # multithreading_concurrent(secs)     # with the concurrent module

    FINISH = time.perf_counter()
    print('Finished in {} second(s)'.format(round(FINISH - BEGIN, 2)))
