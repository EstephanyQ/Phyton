"""
desarrollar un programa que permita categorizar a una persona segun su edad:

Si la persona es menor de 18 años, sera menor de edad
Si la persona tiene entre 18 y 35 años , sera un adulto joven
Si la persona tiene  mas de 35 hasta 70 años , sera un adulto 
Finalmente si la persona tiene mas de 70 es de la tercera edad
"""

edad = int(input("Ingrese su edad:"))

if edad <18:
    print("menor de edad")

else: 
    if edad <= 35:
        print("adulto joven")

    else:
        if edad <=70:
            print("Adulto")

        else:
            print("adulto mayor")

print("Adios")            