"""
8. Definir una funcion generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
Por ejemplo: generar_n_caracteres(5,"x") deberia devolver "xxxxx"
"""

def generar_n_caracteres (n, caracter):

    #Forma simplificada

    string = caracter
    print(n * caracter)

    #Forma mas larga
"""    
    for i in range(1,n):
        string += caracter
    
    print(string)
"""
generar_n_caracteres(5, 'x')