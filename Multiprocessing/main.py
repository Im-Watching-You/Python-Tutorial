import time
from concurrent import futures
from multiprocessing import Process


def some_process(seconds):
    """Function for processing"""
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print(f'Woke up after {seconds} second(s)')


def multiprocessing_concurrent(seconds):
    """Short way of multiprocessing with the concurrent module"""
    with futures.ProcessPoolExecutor() as executor:
        executor.map(some_process, seconds)


def multiprocessing_multiprocessing(seconds):
    """Manual way of multiprocessing with the multiprocessing module"""
    processes = []

    for s in seconds:
        t = Process(target=some_process, args=(s,))
        t.start()
        processes.append(t)

    for thread in processes:
        thread.join()


if __name__ == '__main__':
    BEGIN = time.perf_counter()
    secs = [1, 2, 3, 4, 5]

    multiprocessing_concurrent(secs)        # with the concurrent module
    # multiprocessing_multiprocessing(secs)   # with the multiprocessing module

    FINISH = time.perf_counter()
    print('Finished in {} second(s)'.format(round(FINISH - BEGIN, 2)))
