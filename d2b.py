import numpy as np
from tqdm import tqdm

from d2a import get_dubs, get_input


def is_repeated_seq(number):
    """
    >>> is_repeated_seq(111)
    True
    >>> is_repeated_seq(112)
    False
    >>> is_repeated_seq(123123123)
    True
    """
    for partition in partition_equally(number):
        if all(np.asarray(partition) == partition[0]):
            return True
    return False


def partition_equally(number):
    """
    >>> tuple(partition_equally("1234"))
    (['12', '34'], ['1', '2', '3', '4'])
    >>> tuple(partition_equally("123456"))
    (['123', '456'], ['12', '34', '56'], ['1', '2', '3', '4', '5', '6'])
    >>> tuple(partition_equally("123123123"))
    (['123', '123', '123'], ['1', '2', '3', '1', '2', '3', '1', '2', '3'])
    """
    number = str(number)
    for div in range(2, len(number) + 1):
        if len(number) % div != 0:
            continue  # not divisible
        else:
            subdiv_length = len(number) // div
            subdivs = range(0, len(number) + 1, subdiv_length)
            yield [number[a:b] for a, b in zip(subdivs[:-1], subdivs[1:])]


if __name__ == "__main__":
    all_dubs = [
        get_dubs(start, stop, is_repeated_seq) for start, stop in tqdm(get_input())
    ]
    print(sum([sum(l) for l in all_dubs]))
