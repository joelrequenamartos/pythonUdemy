# Herencia, capacidad de compartir atributos y metodos
# entre clases, y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad 
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos
        
    def setAltura(self, altura):
        self.altura = altura
        
    def setEdad(self, edad):
        self.edad = edad
        
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy dormir"
    
class Informatico(Persona):
    """
    lenguaje
    experiencia
    """
    
    def __init__(self):
        self.lenguajes = "HTLM, CSS, JAVA, PHP"
        self.experiencia = 5
        
    def getLenguajes(self):
        return self.lenguajes
   
    def setAprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "Te lo arreglo."
    
    
class tecnicoRedes(Informatico):
    def ___init__(self):
        self.auditoriaRedes = "experto"
        self.experienciaRedes = 15
        
    def auditoria(self):
        return "estoy auditando"