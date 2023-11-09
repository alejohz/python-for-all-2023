def read_file(file_path):
    # file = open(file_path, "modo")
    # file.close()
    # with open(file_path, "modo") as f:
    #   Aqui proceso el archivo
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines