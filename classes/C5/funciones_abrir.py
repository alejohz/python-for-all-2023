def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return lines