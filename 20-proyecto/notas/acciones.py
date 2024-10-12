import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(f"\nOk, {usuario[1]} vamos a crear una nueva nota...")
        
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >= 1:
            print(f"\n Se ha guardado bien la nota: {nota.titulo}")