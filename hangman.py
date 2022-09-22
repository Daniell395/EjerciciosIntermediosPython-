import os
import random

ruta_dir = os.path.dirname(__file__)
rutaR = os.path.join(ruta_dir, "./archivos/data.txt")


def read():
    """lee la lista de datos, recorre todas las palabras, elimina los saltos"

    Returns:
        list: listado de todas las palabras
    """
    with open(rutaR, "r", encoding="utf-8") as f:
        words = [i.replace("\n", "") for i in f]
    return words


def choose():
    """escoje cualquier palabra de la lista ya leida

    Returns:
        string: palabra ya seleccionada
    """
    words = read()
    data_random = random.choice(words)
    return data_random


def size_word_blank(word):
    """genera una longitud de espacios _ con la cantidad de letras de la palabra

    Args:
        word (string): palabra pre seleccionada

    Returns:
        string: genera los '_'
    """
    word_blank = ['_' for i in range(0, len(word))]
    word_h = ''
    for i in word_blank:
        word_h += f'{i} '
    return word_blank


def find_letter(letter, word):
    """Se recibe una letra y una palabra para ser evaluadas si son iguales

    Args:
        letter (string): letra sin tildes y solo caracteres
        word (string): palabra con cualquier tipo de informacion

    Returns:
        list: retorna la lista ya evaluada con la letra ingresada
    """

    vocals, expressions = 'aeiou', 'áéíóú'
    non_expressions = str.maketrans(vocals, expressions)
    word = word.translate(non_expressions)
    if letter in word:
        search = word.index(letter)
        position = [i for i in range(0, len(word)) if letter == word[i]]
    else:
        position = []
    return position


def validate_letter(letter, word_blank, posicions):
    """coloca la letra en la posicion correcta

    Args:
        letter (string): letras por usuario
        word_blank (list): palabra vacia
        posicions (int): indice de la posicion

    Returns:
        list: retorna las letras colocadas en la palabra
    """
    for i in posicions:
        word_blank[i] = letter
        
    return word_blank


def comparison(word, letter):

    """Compara las letras ingresadas por el usuario con la palabra registrada

    Raises:
        NameError: longitud de caracteres
        NameError: numeros
        NameError: simbolos

    Returns:
        string: caracter ingresado
    """
    w = list(word)
    l = list(letter)
    
    user = ''
    while w != l:
        try:
            founded= False
            user = input("ingrese una letra: ")

            if len(user) > 1:
                raise NameError("Por favor ingrese un solo caracter")
            elif user.isnumeric() or not(user.isalpha()):
                raise NameError("Por favor solo agregue letras")
            os.system("clear")
            for i in range(0, len(w)):
                if w[i] == user:
                    l[i] = w[i]
                    founded = True
            
            if(not(founded)):
                print("la letra no coincide")
            print(" ".join(l).upper())
            print("\n")

        except NameError as Ne:
            print(Ne)
    return user


def validate_word(word):
    """Valida si la palabra fue encontrada

    Args:
        word (string)

    Returns:
        boolean: false si no fue encontrada, true si se halla
    """

    return word.count("_") != 0

def run():
    try:
        attemps = 0
        word = choose()
        word_draw = size_word_blank(word)
        os.system("clear")

        if validate_word(word_draw):
            print("!ADIVINA LA PALABRA !")
            letter = comparison(word, word_draw)
            posicions = find_letter(letter, word)
            word_draw = validate_letter(letter, word_draw, posicions)

        print("la palabra es: "+ word+ "\n ¡Ganaste!")

    except (FileNotFoundError, NameError, SyntaxError):
        print("Error, datos no encontrados")


if __name__ == '__main__':
    run()
