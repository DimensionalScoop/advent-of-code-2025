def read_lines(file):
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if len(l) > 0]
    return lines
