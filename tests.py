from unittest import TestCase
from movimientos import *


tablero = [
        ['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
    ]

tablero_secundario = [
        ['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
        ['p', 'p', 'p', ' ', 'p', 'p', 'p', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'p', ' ', ' ', ' ', 'p'],
        ['A', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['T', 'K', ' ', 'R', 'Q', 'A', 'K', 'T']
    ]

tablerotorre = [
        ['t', 'k', 'a', 'q', 'r', 'a', 'k', ' '],
        ['p', 'p', 'p', ' ', 'p', 'p', 'p', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 't'],
        [' ', ' ', ' ', 'p', ' ', ' ', ' ', 'p'],
        ['A', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['T', 'K', ' ', 'R', 'Q', 'A', 'K', 'T']
    ]


class Test_movimientos(TestCase):


    def test_tablero_a_cadena(self):
        dado = [tablero]
        espero = ""
        obtengo = tablero_a_cadena(dado)
        self.assertEquals(espero, obtengo)

    def test_obtener_nombre_pieza(self):
        dado = "t"
        espero = "t"
        obtengo = obtener_nombre_pieza(t)
        self.assertEquals(espero, obtengo)

    def test_mover_torre(self):
        dado = [tablero_secundario, 0, 0, 4, 0]
        espero = "El camino esta bloqueado por una pieza amiga"
        obtengo = mover_torre(tablero_secundario,0,0,4,0)
        self.assertEquals(espero, obtengo)

    def test_mover_torre(self):
        dado = [tablero_secundario, 7, 0, 7, 2]
        espero = "El camino esta bloqueado por una pieza amiga"
        obtengo = mover_torre(tablero_secundario, 7, 0, 7, 2)
        self.assertEquals(espero, obtengo)

    def test_mover_torre(self):
        dado = [tablero_secundario, 7, 0, 8, 0]
        espero = "la posicion no existe en el tablero"
        obtengo = mover_torre(tablero_secundario, 7, 0, 8, 0)
        self.assertEquals(espero, obtengo)

