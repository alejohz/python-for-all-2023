import funciones.saludar as s
import funciones.despedir as d
from funciones_2.sumar import suma

# import funciones_2.sumar as s
# s.suma(4, 5)
from funciones_2.restar import resta
from utils import utils as u

from funciones.utils_archivos import top_10
import funciones.utils_archivos as t


import funciones.mini_funciones.mini_sumar as ms

print(ms.mini_suma(5))
# 10

s.saludar()
s.saludar_nombre("Juan")
d.despedir()


print(suma(4, 5))
print(resta(3, 4))

# lines = u.read_file(
#         "/Users/alejohz/Documents/Personal/python-for-all-2023/classes/C6/modulos/people.txt"
#     )
# print(
#     lines
# )

# top_10(
#     "/Users/alejohz/Documents/Personal/python-for-all-2023/classes/C6/people.txt",
#     5
# )

t.top_10(
    "/Users/alejohz/Documents/Personal/python-for-all-2023/classes/C6/people.txt",
    5
)