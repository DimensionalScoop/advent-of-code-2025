def parse_line(line):
    dir = line[0]
    raw_steps = int(line[1:])

    match dir:
        case "L":
            steps = raw_steps
        case "R":
            steps = -raw_steps
        case _:
            raise NotImplementedError()
    return steps


with open("data/d1", "r") as f:
    lines = f.readlines()
document = [parse_line(l) for l in lines]

dial = 50
DIAL_RANGE = 100

if __name__ == "__main__":
    zeros_obs = 0
    for step in document:
        dial += step
        dial = dial % DIAL_RANGE
        if dial == 0:
            zeros_obs += 1
    print(zeros_obs)
