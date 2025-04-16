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
    print(texto_dec)




    
