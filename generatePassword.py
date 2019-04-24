# Se importa el módulo string y el módulo random
import string
import random

# Función que permite generar una contraseña aleatoria de entre
# 4 y 16 caracteres que puede incluir minúsculas, mayúsculas,
# números y caracteres especiales
# Entradas:     Ninguna
# Salidas:      Password con las características antes citadas
def generatePassword():
    v_cantidad = random.randrange(4,16)     # Se obtiene la cantidad de caracteres
    v_password = ""                         # Se inicializa el password
    for v_contador in range(1, v_cantidad): # Cantidad de caracteres
        v_tipo = random.randrange(3)        # 1=ascii, 2=digitos, 3=puntuación
        if v_tipo == 1:
            v_password += random.choice(string.ascii_letters)
        elif v_tipo == 2:
            v_password += random.choice(string.digits)
        else:
            v_password += random.choice(string.punctuation)
    return v_password                       # Retorna el password

#Ejecución principal
print(generatePassword());
