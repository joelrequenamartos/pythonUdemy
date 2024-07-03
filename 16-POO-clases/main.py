#programacion orientada a objectos.

'''
Definicion de clase.
'Molde' para crear mas de un objeto de este tipo.
Por ejemplo, 'coche' con caracteristicas similares
'''

class Coche:
    
    # Atributos o propiedades.
    # Caracteristicas del cooche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    cv = 500
    plazas = 2
    
    # Metodos
    # Son acciones que hace el objeto
    
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
        
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1
        
    def frenar(self):
        self.velocidad -=1
        
    def getVelocidad(self):
        return self.velocidad

#fin definicion clase

#Crear objectos / Instanciar la clase


coche = Coche()

velocidad = coche.getVelocidad()
modelo = coche.getModelo()
color = coche.getColor()

coche.setColor("Verde")
coche.setModelo("Murcielago")

print(coche.velocidad, coche.modelo, coche.color)

"""
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print(coche.velocidad, coche.velocidad)

coche.frenar()
coche.frenar()

print(coche.velocidad) """


# Crear mas objectos
coche2 = Coche()
coche2.setColor("Azul")
print(coche2.getColor())