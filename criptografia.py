def preparar_texto (texto):
    """
    Convierte el texto a minusculas, sustituye acentos y elimina espacios
    al inicio y al final
    Entradas: texto a procesar
    Salidas: Texto sin mayusculas, acentos y espacios al inicio o
    al final
    Restricciones: Texto debe ser un string
    """
    if type(texto) != str:
        raise Exception("Texto debe ser un string")
    texto = texto.lower()
    #
    for i in range(0,len(texto)):
        texto = texto.replace("á","a")
        texto = texto.replace("é","e")
        texto = texto.replace("í","i")
        texto = texto.replace("ó","o")
        texto = texto.replace("ú","u")
    return texto

def cesar_cod (texto, desplazamiento):
    """
    Funcion que codifica el texto en cifrado cesar
    Entradas y restricciones:
    -Texto a codificar string
    -Desplazamiento int puede ser positivo o negativo
    Salidas:
    Texto codificado (String)
    """
    if type(texto) != str:
        raise Exception("Texto debe ser un string")
    if type(desplazamiento) != int:
        raise Exception("El desplazamiento debe ser un numero entero")
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ"
                ,"o","p","q","r","s","t","u","v","w","x","y","z"]
    #Mae lo que hace la linea de abajo nd mas es crear el alfabeto codificado
    #Segun el desplazamiento
    alfabeto_cod = alfabeto[desplazamiento::] + alfabeto[:desplazamiento]
    texto = preparar_texto(texto)
    texto_cod = ""
    for i in range(0,len(texto)):
            if texto[i] in alfabeto:
                indice = alfabeto.index(texto[i])
                texto_cod += alfabeto_cod[indice]
            else:
                texto_cod += texto[i] #Este else es por si hubiera un espacio,
                #una coma o algo que lo deje y lo añada nd mas
    
    return texto_cod

def cesar_dec(texto, desplazamiento):
    """
    Funcion que descodifica un texto en cifrado cesar
    Entradas y restricciones:
    -Texto a descodificar string
    -Desplazamiento int puede ser positivo o negativo
    Salidas:
    Texto descodificado (String)
    """
    if type(texto) != str:
        raise Exception("Texto debe ser un string")
    if type(desplazamiento) != int:
        raise Exception("El desplazamiento debe ser un numero entero")
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ"
                ,"o","p","q","r","s","t","u","v","w","x","y","z"]
    desplazamiento = desplazamiento * -1
    alfabeto_cod = alfabeto[desplazamiento::] + alfabeto[:desplazamiento]
    texto = preparar_texto(texto)
    texto_dec = ""
    for i in range(0,len(texto)):
            if texto[i] in alfabeto:
                indice = alfabeto.index(texto[i])
                texto_dec += alfabeto_cod[indice]
            else:
                texto_dec += texto[i] 
    return texto_dec


def mono_cod(texto, palabra):
    """
    Funcion que codifica el texto en cifrado monoalfabético con palabra clave
    Entradas y restricciones:
    -Texto a codificar string
    -palabra clave string no puede ser vacía
    Salidas:
    Texto codificado (String)
    """
    if type(texto) != str and type(palabra) != str:
        raise Exception("Texto y palabra deben ser un string")
    if not palabra:
        raise Exception("La palabra clave no puede estar vacía")

    alfabeto = "abcdefghijklmnñopqrstuvwxwz"
    texto = preparar_texto(texto)
    palabra = preparar_texto(palabra)

    #quita las letras repetidas de la palabra clave si es que tuviera
    palabra_sin_repetidas = ""
    for letra in palabra:
        if letra not in palabra_sin_repetidas and letra in alfabeto:
            palabra_sin_repetidas += letra

    #Crea el alfabeto con la palabra clave
    alfabeto_cod = palabra_sin_repetidas
    for letra in alfabeto:
        if letra not in alfabeto_cod:
            alfabeto_cod += letra

    #codifica el texto original
    texto_cod = ""
    for letra in texto:
        if letra in alfabeto:
            indice = alfabeto.index(letra) #toma la posicion de la letra en el alfabeto
            texto_cod += alfabeto_cod[indice]
        else:
            texto_cod += letra #para mantener los espacios

    return texto_cod
    
def mono_dec(texto, palabra):
    """
    Funcion que descodifica un texto en cifrado monoalfabético con palabra clave
    Entradas y restricciones:
    -Texto a codificar string
    -palabra clave string no puede ser vacía
    Salidas:
    Texto descodificado (String)
    """
    if type(texto) != str and type(palabra) != str:
        raise Exception("Texto y palabra deben ser un string")
    if not palabra:
        raise Exception("La palabra clave no puede estar vacía")

    alfabeto = "abcdefghijklmnñopqrstuvwxwz"
    texto = preparar_texto(texto)
    palabra = preparar_texto(palabra)

    #quita las letras repetidas de la palabra clave si es que tuviera
    palabra_sin_repetidas = ""
    for letra in palabra:
        if letra not in palabra_sin_repetidas and letra in alfabeto:
            palabra_sin_repetidas += letra

    #Crea el alfabeto con la palabra clave
    alfabeto_cod = palabra_sin_repetidas
    for letra in alfabeto:
        if letra not in alfabeto_cod:
            alfabeto_cod += letra

    #decodifica el texto codificado
    texto_dec = ""
    for letra in texto:
        if letra in alfabeto_cod:
            indice = alfabeto_cod.index(letra) #toma la posicion de la letra en el alfabeto codificado
            texto_dec += alfabeto[indice]
        else:
            texto_dec += letra #para mantener los espacios

    return texto_dec



def codificar_o_decodificar():
    while True:
        metodo = input("Ingresa 0 para codificar o 1 para decodificar")
        if metodo == "0" or metodo == "1":
            return int(metodo)
        else:
            print("Opción inválida. Por favor, ingrese solo 0 o 1.")

def leer_texto(metodo):
    if metodo == 0:
        texto = input("Ingrese el texto a codificar: ")
    else:
        texto = input("Ingrese el texto a decodificar: ")
    return texto

def main():
    """
    Programa principal donde se elige el metodo a codificar y se
    obtiene el texto codificado
    """
    
    try:
        print("Bienvenido(a) al nuestro programa para codificar y descodificar textos")
        print("Este programa tiene diferentes métodos de cifrado de textos")
        print("Vos escogés el método que quieras, ya sea para codificar o decodificar el texto")
        opcion = 1
        while(opcion != 0):
            print()
            print()
            print("0. Salir del programa")
            print("1. Cifrado César")#los siguientes los comento hasta que los vayamos a usar
            print("2.Cifrado monoalfabético con palabra clave")
            #print("3. Cifrado Vigenère")
            #print("4. Cifrado PlayFair modificado")
            #print("5. Cifrado Rail Fence")
            #print("6. Escítala")
            print()

            opcion = int(input("Digite el número: "))
            
            match opcion:
                case 0:
                    print("Gracias por usar nuestro programa")
                    print("Nos vemos pronto")
                    
                case 1:
                    metodo = codificar_o_decodificar()
                    if metodo == 0:
                        texto = leer_texto(metodo)
                        desplazamiento = int(input("Digite el desplazamiento a realizar: "))
                        texto_cod = cesar_cod (texto, desplazamiento)
                        print()
                        print("texto codificado: " + texto_cod)
                    else:
                        texto = leer_texto(metodo)
                        desplazamiento = int(input("Digite el desplazamiento a realizar: "))
                        texto_dec = cesar_dec (texto, desplazamiento)
                        print()
                        print("texto decodificado: " + texto_dec)
                    
                case 2:
                    metodo = codificar_o_decodificar()
                    if metodo == 0:
                        texto = leer_texto(metodo)
                        palabra = input("Digite la palabra clave: ")
                        texto_cod = mono_cod (texto, palabra)
                        print()
                        print("texto codificado: " + texto_cod)
                    else:
                        texto = leer_texto(metodo)
                        palabra = input("Digite la palabra clave: ")
                        texto_dec = mono_dec (texto, palabra)
                        print()
                        print("texto decodificado: " + texto_dec)
                    
                case 3:
                    metodo = codificar_o_decodificar()
                    
                case 4:
                    metodo = codificar_o_decodificar()
                    
                case 5:
                    metodo = codificar_o_decodificar()
                    
                case 6:
                    metodo = codificar_o_decodificar()

                case _:
                    print("Número no válido")

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


if __name__ == "__main__":
    main()




    
    
