"""
Ejercicio 3.
Muestra el cuadrado de los 60 primeros numero naturales.
- Resolverlo con el FOR y con el WHILE
"""

print("Metodo While")
numeroMax = 0
while numeroMax <= 60:
    print(f"{numeroMax} x {numeroMax} = {numeroMax*numeroMax}")
    numeroMax += 1
    if numeroMax == 60:
        print("--------------------------")
        
print("Metodo For")
for numeroMax in range (61):
    print(f"{numeroMax} x {numeroMax} = {numeroMax*numeroMax}")