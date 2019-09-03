import sys
import collections
import multiprocessing
import time
from datetime import datetime, date

FIND_SCIENCE_MSG = "Find a scientist name = %s, age = %d"


def process_item(item):
    time.sleep(1)

    born = 2017 - item.born

    print(FIND_SCIENCE_MSG % (item.name, born))

    return {
        'name': item.name,
        'age': born
    }


def print_time_duration(process, start, end):
    duration = datetime.combine(date.min, end) - datetime.combine(date.min, start)
    print(" (%s) process in second : %s " % (process, str(duration.total_seconds())))


def sequential_process(scientists):
    start = datetime.now().time()
    print("###Start : " + start.strftime("%H:%M:%S"))

    for a_scientist in scientists:
        process_item(a_scientist)

    end = datetime.now().time()
    print("###End   : " + end.strftime("%H:%M:%S"))

    print_time_duration("Sequential", start, end)


def parallel_process(scientists):
    start = datetime.now().time()
    print("###Start : " + start.strftime("%H:%M:%S"))

    pool = multiprocessing.Pool()
    result = pool.map(process_item, scientists)

    end = datetime.now().time()
    print("###End   : " + end.strftime("%H:%M:%S") + "\n")

    for r in result:
        print(FIND_SCIENCE_MSG % (r["name"], r["age"]))

    print_time_duration("Parallel", start, end)


if __name__ == "__main__":
    Scientist = collections.namedtuple('Scientist', [
        'name',
        'born',
    ])

    scientists = (
        Scientist(name='Ada Lovelace', born=1815),
        Scientist(name='Emmy Noether', born=1882),
        Scientist(name='Marie Curie', born=1867),
        Scientist(name='Tu Youyou', born=1930),
        Scientist(name='Ada Yonath', born=1939),
        Scientist(name='Vera Rubin', born=1928),
        Scientist(name='Sally Ride', born=1951),
    )

    # 1. Sequential
    sequential_process(scientists)

    print("\n")

    # 2. Parallel
    parallel_process(scientists)
