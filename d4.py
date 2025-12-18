import numpy as np

from common import read_lines

PAPER = 0
EMPTY = 1


def parse_input():
    lines = read_lines("data/d4")
    map = np.asarray([EMPTY if c == "." else PAPER for line in lines for c in line])
    map = map.reshape(len(lines[0]), -1)
    return map


def pad_map(map):
    new_map = np.ones([map.shape[0] + 2, map.shape[1] + 2])
    new_map *= EMPTY
    new_map[1:-1, 1:-1] = map
    return new_map


MIN_AIR_FOR_FREE = 5
MAX_PAPER_FOR_FREE = 3


def is_free(map, x, y):
    """
    >>> map = np.array([
    ...    [1,1,1],
    ...    [1,0,1],
    ...    [1,1,1]])
    >>> is_free(map, 1,1)
    True
    >>> map = np.array([
    ...    [0,0,0],
    ...    [1,0,0],
    ...    [1,1,1]])
    >>> is_free(map, 1,1)
    False
    >>> map = np.array([
    ...    [0,0,0],
    ...    [0,0,0],
    ...    [1,1,1]])
    >>> is_free(map, 1,1)
    False
    """
    max_x = len(map)
    max_y = len(map[0])

    assert map[x, y] == PAPER
    assert x < max_x - 1
    assert x > 0
    assert y < max_y - 1
    assert y > 0

    paper_count = 0
    empty_count = 0
    for u in [x - 1, x, x + 1]:
        for v in [y - 1, y, y + 1]:
            if u == x and v == y:
                continue
            if map[u, v] == PAPER:
                paper_count += 1
            elif map[u, v] == EMPTY:
                empty_count += 1

    assert empty_count + paper_count == 8
    return paper_count <= MAX_PAPER_FOR_FREE


if __name__ == "__main__":
    unpadded_map = parse_input()
    map = pad_map(unpadded_map)
    free_count = 0
    for x in range(unpadded_map.shape[0]):
        for y in range(unpadded_map.shape[1]):
            if map[x + 1, y + 1] == PAPER:
                free_count += is_free(map, x + 1, y + 1)
    print(free_count)
