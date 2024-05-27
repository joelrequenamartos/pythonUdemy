"""
Ejercicio 5
Crear una lista con el contenido de una tabla
Videojuegos:
Shooter: Cod, Pubg, gta
Aventura: Zelda, CrashB, AC
Deportes: MotoGP, Fifa, RocketLeague

Mostrar esta informacion ordenada. 
"""

table = [
    {
        "category": "Shooter",
        "games": ["COD", "Pugb", "GTA"]
    },
    {
        "category": "Adventure",
        "games": ["Zelda", "CrashBandicoot", "AnimalCrossing"]
    },
    {
        "category": "Sports",
        "games": ["MotoGP", "Fifa", "RocketLeague"]
    }
]

for categoria in table:
    print(f"--------{categoria['category']}---------")
    for juego in categoria['games']:
            print("- " + juego)
            
"""
dentro del segundo for solamente se imprime 'juego' por que ya le estamos indicando que queremos que itere 
"""


     