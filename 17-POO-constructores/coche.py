class Coche:
    
    # Atributos o propiedades.
    # Caracteristicas del cooche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    cv = 500
    plazas = 2
    
    soyPublico = "Soy un atributo publico"
    __soyPrivado = "Soy un atributo privado"
    
    #constructor
    def __init__(self, color, marca, modelo, velocidad, cv, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.cv = cv
        self.plazas = plazas
        
    # Metodos
    # Son acciones que hace el objeto
    
    def getPrivado(self):
        return self.__soyPrivado
    
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
        
    def getModelo(self):
        return self.modelo

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca
        
    def acelerar(self):
        self.velocidad += 1
        
    def frenar(self):
        self.velocidad -=1
        
    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        info = "-Info-"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        
        return info