print("☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻punto 1☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻")
#Enteroa
anio = 2024
#Decimal
estatura = 1.78
altura = int(estatura)
print(type(estatura))
decimal = float(anio) #conversion de int a floar
#cadena
num = 1232
nombre = "Andres Rodriguez"
print(type(nombre))
texto = str(num) #conversion de int a str
print(f"Conversion de Entero a float: {decimal}")
print(f"Conversion de float a entero: {altura}")
print(f"Conversion de entero a cadena: {texto}")

print("☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻Punto 2 --multilineas de cadena☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻")
mensaje = "este\ttexto\tes tabulado\npara la prueba\ndel parcial\n"
mensaje2 = "cadena con una comilla simple \'. una comilla doble \" y una deagonal invertida \\" #cadena de caracteres
print(mensaje2)
print(mensaje)
print("☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻punto 3 --Funcion len()☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻")
print(f"el tamaño del texto en la variable nombre es: {len(nombre)}") #len para ver el tamaño de una variable

print("\n☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻punto 4 Sub cadenas:☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻")
informacion = "Electiva profesional"
n=4
extraer = informacion[0:n] #extraer caracteres
print(f"A: Primeros {n} caracteres de 'Electiva profesional': {extraer}")
# a continuacion se usa len y dividir n para encontrar la mitad
print(f"B: Los caracteres de en medio son: {informacion[len(informacion)//2-n//2:len(informacion)//2+n//2]} ")
print(f"C: ultimos {n} caracteres: {informacion[len(informacion)-n:len(informacion)]}") #ultimos n
print(f"\n-→ Funcion upper:  \t{nombre.upper()}") #mayusculas
print(f"-→ Funcion lower:  \t{nombre.lower()}") #minusculas
print("""-→ Ejemplo  de multilineas  
       > de una cadena  
       > de caracteres""")#multilineas de caracteres
name = " Andru rodrig "
name = name.strip("A ig") #eliminar caracteres al inicio y al final
print(f"-→ Función strip(): \t{name}")
print(f"-→ Función repleace: {nombre.replace("Rodriguez","Rod Salazar")}")#modificar o reemplazar
var_split=informacion.split()
print(f"-→ Función split(): \t{var_split}")#separar str
carrera = "Ing en sistemas"
materia = "Electiva profesional"
semestre = 6                     #F-string para concatenar variables en un print
print('-→ Formato de cadenas F-String: Estudio " %s ", la materia es "%s" y estoy en "%d" semestre ' % (carrera,materia,semestre))