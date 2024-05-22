cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio']
numeros = [1, 2, 5, 8, 3, 4]

#ordenar
print(numeros)
numeros.sort()
print(numeros.sort())

#añadir
cantantes.append("Bbyno$") #se añade al final
cantantes.insert(1, "David Bisbal") #se añade en una posicion en especifico
print(cantantes)

#eliminar elementos
cantantes.pop(1)
print(cantantes)
cantantes.remove("Julio")
print(cantantes)

#invertir orden
print(numeros)
numeros.reverse()
print(numeros)

#test si existe o no
print('Drake' in cantantes)
print('Julio' in cantantes)

# Contar elementos
print(len(cantantes))

# Cuantas veces aparece un elemento
print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Drake"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)