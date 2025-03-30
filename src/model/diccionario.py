import random


class Diccionario:
    """
    Clase que representa un diccionario de palabras para el juego del ahorcado.

    Attributes:
        palabras (list[str]): Lista de palabras cargadas desde un archivo.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase Diccionario, cargando las palabras desde un archivo.
        """
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        """
        Carga las palabras desde el archivo "assets/palabras.txt".

        Returns:
            list[str]: Lista de palabras disponibles en el diccionario.
        """
        palabras = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                palabras.append(line.strip())
        return palabras

    def obtener_palabra(self) -> str:
        """
        Obtiene una palabra aleatoria del diccionario.

        Returns:
            str: Una palabra seleccionada aleatoriamente.
        """
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]