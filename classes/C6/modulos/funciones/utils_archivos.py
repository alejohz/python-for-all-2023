def top_10(ruta, n):
    """Muestra las primeras diez lineas de un archivo""" # Docstring
    try:
        f = open(ruta, "r")
        lines = []
        contador = 1
        while contador <= n:
            line = f.readline()
            line = line.replace("\n", "")
            lines.append(line)
            contador += 1
        f.close()
        print("\n".join(lines))
        # print(lines)
    except FileNotFoundError:
        print("El archivo no existe")
