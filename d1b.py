from d1a import read_lines, parse_line, dial, DIAL_RANGE


def process_step(dial, step):
    """
    >>> process_step(10, 5)
    (15, 0)
    >>> process_step(77, 100)
    (77, 1)
    >>> process_step(65, -5)
    (60, 0)
    >>> process_step(40, -101)
    (39, 1)
    >>> process_step(40, -201)
    (39, 2)
    >>> process_step(88, 0)
    (88, 0)
    >>> process_step(33, -33)
    (0, 0)
    """
    zero_passes = 0
    old_dial = dial
    # when turning over 98 steps
    full_turns = step // DIAL_RANGE
    if full_turns < 0:  # for a negative step direction, // overestimates by 1
        full_turns += 1
    step -= full_turns * DIAL_RANGE
    zero_passes += abs(full_turns)

    assert dial > -DIAL_RANGE
    assert dial < DIAL_RANGE

    dial += step
    if old_dial == 0:
        pass
    elif dial != (dial % DIAL_RANGE):
        zero_passes += 1

    dial = dial % DIAL_RANGE
    return dial, zero_passes


if __name__ == "__main__":
    lines = read_lines("data/d1a")
    document = [parse_line(l) for l in lines]

    zeros_obs = 0
    for step in document:
        assert step != 0

        dial, this_zero = process_step(dial, step)
        zeros_obs += this_zero
        if dial == 0:
            zeros_obs += 1
    print(zeros_obs)
