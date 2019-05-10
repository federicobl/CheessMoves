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
        [' ', ' ', ' ', 'p', ' ', ' ', ' ', 'P'],
        ['A', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', 'P', 'P', 'P', 'P', 'P', ' '],
        ['T', 'K', ' ', 'R', 'Q', 'A', 'K', 'T']
    ]

tablerotorre = [
        ['t', 'k', 'a', 'q', 'r', 'a', 'k', ' '],
        ['p', 'p', 'p', ' ', 'p', 'p', 'p', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 't'],
        [' ', ' ', ' ', 'p', ' ', ' ', ' ', ' '],
        ['A', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', 'P', 'P', 'P', 'P', 'P', ' '],
        ['T', 'K', ' ', 'R', 'Q', 'A', 'K', 'T']
    ]

    #tableros peón

#movimiento inicial de dos pasos
tablerop = [
        ['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
        ['p', ' ', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
    ]

#movimiento inicial o normal de un paso
tablerop1 =[
        ['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
        ['p', ' ', 'p', ' ', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', 'p', ' ', ' ', ' ', ' '],
        [' ', 'p', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
    ]

#tablero inicial comer pieza
tablerop2 = [
        ['t', ' ', 'a', 'q', 'r', 'a', 'k', ' '],
        ['p', 'p', 'p', ' ', 'p', 'p', 'p', ' '],
        [' ', ' ', 'k', ' ', ' ', ' ', ' ', 't'],
        [' ', 'P', ' ', 'p', ' ', ' ', ' ', 'P'],
        ['A', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', 'P', 'P', 'P', 'P', 'P', ' '],
        ['T', 'K', ' ', 'R', 'Q', 'A', 'K', 'T']
    ]

#tablero final comer pieza y tablero de camino bloqueado por una pieza
tablerop3 = [
        ['t', ' ', 'a', 'q', 'r', 'a', 'k', ' '],
        ['p', 'p', 'p', ' ', 'p', 'p', 'p', ' '],
        [' ', ' ', 'P', ' ', ' ', ' ', ' ', 't'],
        [' ', ' ', ' ', 'p', ' ', ' ', ' ', 'P'],
        ['A', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', ' ', ' ', 'P', 'P', 'P', 'P', ' '],
        ['T', 'K', ' ', 'R', 'Q', 'A', 'K', 'T']
    ]

#Tablero inicial cambiar peon por cualquier pieza
tablerop4 = [
        ['P', ' ', 'a', 'q', 'r', ' ', 'k', 't'],
        [' ', ' ', 'p', ' ', ' ', 'p', 'p', ' '],
        [' ', ' ', ' ', 'a', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'p', ' ', ' ', ' ', 'p'],
        [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'A', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['T', 'K', ' ', 'R', 'Q', 'A', 'K', 'T']
    ]

#Tablero final cambiar peon por cualquier pieza
tablerop5= [
        ['Q', ' ', 'a', 'q', 'r', ' ', 'k', 't'],
        [' ', ' ', 'p', ' ', ' ', 'p', 'p', ' '],
        [' ', ' ', ' ', 'a', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'p', ' ', ' ', ' ', 'p'],
        [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'A', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
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
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_torre(self):
        dado = [tablero_secundario, 0, 0, 4, 0]
        espero = "camino bloqueado"
        obtengo = mover_torre(tablero_secundario, 0, 0, 4, 0)
        self.assertEquals(espero, obtengo)

    def test_mover_torre(self):
        dado = [tablero_secundario, 7, 0, 7, 2]
        espero = [tablerotorre]
        obtengo = mover_torre(tablero_secundario, 7, 0, 7, 2)
        self.assertEquals(espero, obtengo)

    def test_mover_torre(self):
        dado = [tablero_secundario, 7, 0, 8, 0]
        self.assertRaises(TypeError, mover_torre, tablero_secundario, 7, 0, 8, 0)

        #pruebas unitarias del peón

    def test_mover_peon(self):
        dado = [tablero,1,1,3,1]
        espero = [tablerop]
        obtengo = mover_peon(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_peon(self):
        dado = [tablerop,1,4,2,4]
        espero = [tablerop1]
        obtengo = mover_peon(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_peon(self):
        dado = [tablerop2,4,1,3,2]
        espero = [tablerop3]
        obtengo = mover_peon(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_peon(self):
        dado = [tablerop3,7,3,7.4]
        espero = "camino bloqueado"
        obtengo = mover_peon(dado)
        self.assertEquals(espero, obtengo)

    def test_cambiar_peon(self):
        dado = [tablerop4,"Q"]
        espero = [tablerop5]
        obtengo = mover_peon(dado)
        self.assertEquals(espero, obtengo)
