import numpy as np


def read_lines(file):
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if len(l) > 0]
    return lines


def max_joltage(bank, digits=(2, 1)):
    """
    >>> max_joltage("811111111111119")
    89
    >>> max_joltage("818181911112111")
    92
    """
    # array[:-i] only works for i>0, so we add a dummy digit at the end
    bank = np.asarray([int(n) for n in str(bank) + "0"])
    rv = ""
    for i in digits:
        first_max_idx = np.argmax(bank[:-i])
        rv += str(bank[first_max_idx])
        bank = bank[first_max_idx + 1 :]
    return int(rv)


if __name__ == "__main__":
    res = sum([max_joltage(l) for l in read_lines("data/d3")])
    print(res)

    digits = range(12, 0, -1)
    res = sum([max_joltage(l, digits) for l in read_lines("data/d3")])
    print(res)
