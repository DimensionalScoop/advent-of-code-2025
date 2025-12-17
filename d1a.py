def read_lines(file):
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if len(l) > 0]
    return lines


def parse_line(line):
    dir = line[0]
    raw_steps = int(line[1:])  # ignore \n

    match dir:
        case "L":
            steps = -raw_steps
        case "R":
            steps = raw_steps
        case _:
            raise NotImplementedError()
    return steps


dial = 50
DIAL_RANGE = 100

if __name__ == "__main__":
    lines = read_lines("data/d1a")
    document = [parse_line(l) for l in lines]

    zeros_obs = 0
    for step in document:
        dial += step
        dial = dial % DIAL_RANGE
        if dial == 0:
            zeros_obs += 1
    print(zeros_obs)
