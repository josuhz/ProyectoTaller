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
    if verificar: 
        texto = texto.lower()
        #
        for i in range(0,len(texto)):
            texto = texto.replace("á","a")
            texto = texto.replace("é","e")
            texto = texto.replace("í","i")
            texto = texto.replace("ó","o")
            texto = texto.replace("ú","u")
        return texto
    else:
        for i in range(0,len(texto)):
            texto = texto.replace("á","a")
            texto = texto.replace("é","e")
            texto = texto.replace("í","i")
            texto = texto.replace("ó","o")
            texto = texto.replace("ú","u")
        
        

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

    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
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



###
def vigenere_cod(texto,palabra):
    """
    Funcion que codifica un texto en cifrado vigenere con palabra clave
    Entradas y restricciones:
    -Texto debe ser string
    -Palabra clave debe ser string no puede estar vacio
    Salidas:
    -Texto codificado (String)
    """
    if type(texto) != str and type(palabra) != str:
        raise Exception("Texto y palabra deben ser un string")
    if not palabra:
        raise Exception("La palabra clave no puede estar vacía")
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ"
                ,"o","p","q","r","s","t","u","v","w","x","y","z"]
    texto_cod = ""
    texto = preparar_texto(texto)
    palabra = preparar_texto(palabra)
    palabra = palabra * (len(texto)//len(palabra) + 1) #esto es para que la palabra clave se repita todas las veces que cabe en el texto
    j=0 #Ocupo un contador aparte porque si no cuando habia espacios la palabra clave se adelantaba
    for i in range(0,len(texto)):
        if texto[i] in alfabeto:
            indice = (alfabeto.index(texto[i])+alfabeto.index(palabra[j]))%27 #esto es para sacar la letra que toca
            texto_cod += alfabeto[indice]
            j += 1
        else:
            texto_cod += texto[i] #esto es lo de los espacios, comas etc

    return texto_cod

def vigenere_dec(texto,palabra):
    """
    Funcion que descodifica un texto en cifrado vigenere con palabra clave
    Entradas y restricciones:
    -Texto debe ser string
    -Palabra clave debe ser string no puede estar vacio
    Salidas:
    -Texto descodificado (String)
    """
    if type(texto) != str and type(palabra) != str:
        raise Exception("Texto y palabra deben ser un string")
    if not palabra:
        raise Exception("La palabra clave no puede estar vacía")
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ"
                ,"o","p","q","r","s","t","u","v","w","x","y","z"]
    texto_dec = ""
    texto = preparar_texto(texto)
    palabra = preparar_texto(palabra)
    palabra = palabra * (len(texto)//len(palabra) + 1)
    j=0
    for i in range(0,len(texto)):
        if texto[i] in alfabeto:
            indice = (alfabeto.index(texto[i])-alfabeto.index(palabra[j]))%27
            texto_dec += alfabeto[indice]
            j += 1
        else:
            texto_dec += texto[i]

    print(texto_dec)
    return texto_dec   
    
def playfair_cod(texto, palabra):
    """
    Funcion que codifica un texto en cifrado playFair con palabra clave
    Entradas y restricciones:
    -Texto debe ser string
    -Palabra clave debe ser string no puede estar vacio
    Salidas:
    -Texto codificado (String)
    """
    if type(texto) != str and type(palabra) != str:
        raise Exception("Texto y palabra deben ser un string")
    if not palabra:
        raise Exception("La palabra clave no puede estar vacía")
    
    alfabeto = "abcdefghijklmnñopqrstuvwxyz123"
    texto = preparar_texto(texto)
    palabra = preparar_texto(palabra)
    palabra_sin_repetidas = ""
    for letra in palabra:
        if letra not in palabra_sin_repetidas and letra in alfabeto:
            palabra_sin_repetidas += letra
    alfabeto_cod = palabra_sin_repetidas
    for letra in alfabeto:
        if letra not in alfabeto_cod:
            alfabeto_cod += letra
    matriz = []
    for i in range(0, 30, 5):
        matriz.append(list(alfabeto_cod[i:i+5]))
    texto = texto.split()#divide el texto en lista por palabras
    texto_cod = ""
    for palabra in texto:
        palabra_nueva = ""
        i = 0
        # agrega '1' si tiene dos letras iguales seguidas 
        while i < len(palabra):
            palabra_nueva += palabra[i]
            if i + 1 < len(palabra) and palabra[i] == palabra[i+1]:
                palabra_nueva += "1"
                i += 1
            i += 1
        #agrega 1 si la cantidad de letras de la palabra es impar
        if len(palabra_nueva) % 2 != 0:
            palabra_nueva += "1"
        #agrupar la palabra en pares
        pares = []
        i = 0
        while i < len(palabra_nueva):
            pares.append(palabra_nueva[i:i+2])
            i += 2
        #hallar la posicion de cada letra de cada par en la matriz
        for par in pares:
            f1 = c1 = f2 = c2 = 0#inicializo las variables de fila y columna
            for fila in range(6):
                for col in range(5):
                    if matriz[fila][col] == par[0]:
                        f1 = fila
                        c1 = col
                    if matriz[fila][col] == par[1]:
                        f2 = fila
                        c2 = col
            # Codifica según el caso
            if f1 != f2 and c1 != c2:
                texto_cod += matriz[f1][c2] + matriz[f2][c1]
            elif f1 == f2:
                texto_cod += matriz[f1][(c1 + 1) % 5] + matriz[f2][(c2 + 1) % 5]
            elif c1 == c2:
                texto_cod += matriz[(f1 + 1) % 6][c1] + matriz[(f2 + 1) % 6][c2]
        texto_cod += " "
    return texto_cod.strip()

def playfair_dec(texto, palabra):
    """
    Función que decodifica un texto cifrado con Playfair modificado.
    Entradas:
    - texto: texto codificado (string)
    - palabra: palabra clave (string)
    Salidas:
    - texto_dec: texto descifrado (string)
    """
    if type(texto) != str and type(palabra) != str:
        raise Exception("Texto y palabra deben ser un string")
    if not palabra:
        raise Exception("La palabra clave no puede estar vacía")
    
    alfabeto = "abcdefghijklmnñopqrstuvwxyz123"
    texto = preparar_texto(texto)
    palabra = preparar_texto(palabra)

    palabra_sin_repetidas = ""
    for letra in palabra:
        if letra not in palabra_sin_repetidas and letra in alfabeto:
            palabra_sin_repetidas += letra

    alfabeto_cod = palabra_sin_repetidas
    for letra in alfabeto:
        if letra not in alfabeto_cod:
            alfabeto_cod += letra

    matriz = []
    for i in range(0, 30, 5):
        matriz.append(list(alfabeto_cod[i:i+5]))

    texto = texto.split()  # Lista de palabras
    texto_dec = ""

    for palabra in texto:
        pares = []
        i = 0
        while i < len(palabra):
            pares.append(palabra[i:i+2])
            i += 2

        for par in pares:
            f1 = c1 = f2 = c2 = 0
            for fila in range(6):
                for col in range(5):
                    if matriz[fila][col] == par[0]:
                        f1, c1 = fila, col
                    if matriz[fila][col] == par[1]:
                        f2, c2 = fila, col

            if f1 != f2 and c1 != c2:
                texto_dec += matriz[f1][c2] + matriz[f2][c1]
            elif f1 == f2:
                texto_dec += matriz[f1][(c1 - 1) % 5] + matriz[f2][(c2 - 1) % 5]
            elif c1 == c2:
                texto_dec += matriz[(f1 - 1) % 6][c1] + matriz[(f2 - 1) % 6][c2]
                
        texto_dec += " "
        texto_dec = texto_dec.replace("1","")
        texto_dec = texto_dec.replace("2","")
        texto_dec = texto_dec.replace("3","")

    return texto_dec.strip()


###
def cambiar_espacios(texto):
    """
    Funcion que cambia los espacios por guiones
    Entradas y restricciones:
    -Texto debe ser un string
    Salida: El texto con guiones en lugar de espacios (String)
    """
    if type(texto) != str:
        raise Exception("Texto debe ser un string")
    texto = texto.replace(" ","-")
    return texto
def cambiar_guiones(texto):
    """
    Funcion que cambia los guiones por espacios y quita los espacios al final del texto
    Entradas y restricciones:
    -Texto debe ser un string
    Salida: El texto con espacios en lugar de guiones
    """
    if type(texto) != str:
        raise Exception("Texto debe ser un string")
    texto = texto.replace("-"," ")
    texto = texto.strip()
    return texto
            
def railfence_cod(texto):
    """
    Funcion que codifica el texto a cifrado railfence
    Entradadas y restricciones:
    -Texto debe ser un string
    Salida: El texto codificado a cifrado railfence (String)
    """
    if type(texto) != str:
        raise Exception("Texto debe ser un string")
    for i in range(len(texto)):
        if len(texto) % 4 != 0:
            texto += " "
        
    texto = cambiar_espacios(texto)
    texto_c = texto[::4] + texto[1::2] + texto[2::4]
    cont = 0
    texto_cod = ""
    for i in range(len(texto_c)):
        if cont == 5:
            texto_cod += " "
            cont = 0
        texto_cod += texto_c[i]
        cont +=1
        
    return texto_cod


def railfence_dec(texto):
    """
    Funcion que descodifica el texto del cifrado railfence
    Entradadas y restricciones:
    -Texto debe ser un string
    Salida: El texto descodificado del cifrado railfence (String)
    """
    if type(texto) != str:
        raise Exception("Texto debe ser un string")
    
    texto = texto.replace(" ","")
    for i in range(len(texto)):
        if len(texto) % 4 != 0:
            texto += "-"
    txt_arriba = texto[:(len(texto)//4):]
    txt_medio = texto[(len(texto)//4):len(texto)//4+(len(texto)//4)*2:]
    txt_abajo = texto[len(texto)//4+(len(texto)//4)*2::]


    
    texto_dec = ""
    cont =0
    contA =0
    contB= 0
    contC=0
    for i in range(len(txt_medio)):
        if cont == 0:
            texto_dec += txt_arriba[contA] + txt_medio[contB]
            cont = 1
            contA +=1
            contB += 1

        elif cont ==1:
            texto_dec += txt_abajo[contC] + txt_medio[contB]
            cont = 0
            contC += 1
            contB += 1
    texto_dec = cambiar_guiones(texto_dec)
    print(texto_dec)
            
        
        

    
        


    

def codificar_o_decodificar():
    while True:
        metodo = input("Ingresa 0 para codificar o 1 para decodificar: ")
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
    Entradas y restricciones: ninguna
    Salidas: Impresion del mensaje codificado o decodificado
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
            print("1. Cifrado César")
            print("2.Cifrado monoalfabético con palabra clave")
            print("3. Cifrado Vigenère")
            print("4. Cifrado PlayFair modificado")
            print("5. Cifrado Rail Fence")
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
                    if metodo == 0:
                        texto = leer_texto(metodo)
                        palabra = input("Digite la palabra clave: ")
                        texto_cod = vigenere_cod(texto, palabra)
                        print()
                        print("texto codificado: " + texto_cod)
                    else:
                        texto = leer_texto(metodo)
                        palabra = input("Digite la palabra clave: ")
                        texto_dec = vigenere_dec(texto, palabra)
                        print()
                        print("texto decodificado: " + texto_dec)
                case 4:
                    metodo = codificar_o_decodificar()
                    if metodo == 0:
                        texto = leer_texto(metodo)
                        palabra = input("Digite la palabra clave: ")
                        texto_cod = playfair_cod(texto, palabra)
                        print()
                        print("texto codificado: " + texto_cod)
                    else:
                        texto = leer_texto(metodo)
                        palabra = input("Digite la palabra clave: ")
                        texto_dec = playfair_dec(texto, palabra)
                        print()
                        print("texto decodificado: " + texto_dec)
                    
                case 5:
                    metodo = codificar_o_decodificar()
                    if metodo == 0:
                        texto = leer_texto(metodo)
                        texto_cod = railfence_cod(texto)
                        print()
                        print("texto codificado: " + texto_cod)
                    else:
                        texto = leer_texto(metodo)
                        texto_dec = railfence_dec(texto)
                        print()
                        print("texto decodificado: " + texto_dec)
                    
                case 6:
                    metodo = codificar_o_decodificar()

                case _:
                    print("Número no válido")

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


if __name__ == "__main__":
    main()
    
