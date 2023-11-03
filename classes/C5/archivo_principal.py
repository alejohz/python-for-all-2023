from funciones_abrir import read_file
from funciones_juntar import join_list

def concatenar_archivos(*paths):
    # print(*paths)
    if len([*paths]) == 0:
        print("No paso ningun argumento")
    lista_de_archivos = []
    for path in paths:
        # print(path)
        try:
            lines = read_file(path)
            # print("Aqui si leyo el archivo")
            lista_de_archivos.append(join_list(lines))
            # print(lista_de_archivos)
        except FileNotFoundError:
            print("El archivo no existe", path)
    # print(lista_de_archivos)
    return join_list(lista_de_archivos)

main_path = "/Users/alejohz/Documents/Personal/python-for-all-2023/classes/C5/"
resultado = concatenar_archivos(
    f"{main_path}datos.txt", 
    f"{main_path}nombres.txt", 
    f"{main_path}apellidos.txt"
)
print(resultado)