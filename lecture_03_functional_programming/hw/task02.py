"""
Here's a not very efficient calculation function that calculates something important::

    import time
    import struct
    import random
    import hashlib

    def slow_calculate(value):
        '''Some weird voodoo magic calculations'''
        time.sleep(random.randint(1,3))
        data = hashlib.md5(str(value).encode()).digest()
        return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""
import hashlib
import multiprocessing
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    ans = sum(struct.unpack('<' + 'B' * len(data), data))
    return ans


def calculate_0_500():
    start_time = time.time()
    with multiprocessing.Pool(60) as p:
        all_calculations = p.map(slow_calculate, range(501))

    summary = sum(all_calculations)
    end_time = time.time()
    time_exucute = round((end_time - start_time), 2)
    result = {
        'summary': summary,
        'time': time_exucute
    }

    return result


if __name__ == '__main__':
    calculate_0_500()

"""
    ANOTHER SOLUTION

    processes = []
    start_time = time.time()
    for i in range(501):
        p = multiprocessing.Process(target=slow_calculate, args=(i,))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    end_time = time.time()
    print(round((end_time - start_time), 2), 'sec')
"""
