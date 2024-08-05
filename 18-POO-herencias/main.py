import clases


persona = clases.Persona()
persona.setNombre("Joel")
persona.setApellidos("Requena")
persona.setAltura("175cm")
persona.setEdad("23 años")

print({persona.getNombre()}, {persona.getApellidos()})

print(persona.hablar())

informatico = clases.Informatico()

informatico.setNombre("Mc")
informatico.setApellidos("Dalenas")

print({informatico.getNombre()}, informatico.getApellidos())

tecnico = clases.tecnicoRedes()
print(tecnico.auditoriaRedes, tecnico.getNombre)