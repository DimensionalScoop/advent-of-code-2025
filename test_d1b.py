from d1b import process_step, parse_line

input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_fwd():
    document = [parse_line(l) for l in input.split("\n")]
    dial = 50

    zeros_obs = 0
    for step in document:
        assert step != 0

        dial, this_zero = process_step(dial, step)
        zeros_obs += this_zero
        if dial == 0:
            zeros_obs += 1

    assert dial == 32
    TARGET = 6
    assert zeros_obs == TARGET, f"Should be {TARGET}, but is {zeros_obs}"
