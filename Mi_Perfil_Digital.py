#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Johan Felipe Vargas Rojas"
edad = 14
estatura = 1.65
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("Johanzu-11", "johan_cap29")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Unslept", "artista": "Miraidempa", "duracion": "2:10"},
{"titulo": "No Hace falta-Version Acustica", "artista": "Sunny", "duracion": "4:07"},
{"titulo": "Babydoll", "artista": "Dominic Fike", "duracion": "1:38"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
