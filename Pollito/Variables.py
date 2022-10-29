Nombre = input("Ingrese su nombre: ")
Edad = input ("Ingrese su edad: ")
Ecivil = input("Ingrese su estado civil ")

if Ecivil == "C":
    Valorec = "Casado"
elif Ecivil == "V":
    Valorec = "Viudo"
elif Ecivil == "D":
    Valorec = "Divorsiado"
else:
    Valorec = "Soltero"

print ("Hola ", Nombre , "su estado civil es", Valorec)
