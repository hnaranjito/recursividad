from collections import deque

cola = deque(["lapiz", "goma", "boli"])
cola.append("libreta")
print(cola)


lista = ["margarita", "azucena", "clavel", "rosa",
         "amapola", "hortensia", "narciso", "nardo"]

lista.remove("clavel")

print(lista)

lista.pop()

print(lista)
