tablero = [
['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
[' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
]

def tablero_a_cadena(tablero):
    """
    (list of str) -> str
    recibimos un tablero o diccionario y devolvemos una cadena



    :param tablero: el tablero con la posicionde cada ficha
    :return: dict el tablero con la nueva posicion de las fichas
    """

    cadena = ""
    for fila in tablero:
        cadena += str(fila) + "\n"
    return cadena

def obtener_nombre_pieza(simbolo):
    """
    (str) -> str

    >>> obtener_nombre_pieza('p')
    'Peon blanco'
    >>> obtener_nombre_pieza('R')
    'Rey Negro'

    Retorna el nombre de la pieza del ajedrez dado su simbolo

    :param simbolo: la representacion de la pieza segun el enunciado
    :return: El nombre y color de la pieza
    """
    tipo = 'Negro'
    if simbolo.islower():
        tipo = 'blanco'
    retorno = simbolo.lower()
    if retorno == 'p':
        return 'Peon '+tipo
    elif retorno == 't':
        return 'Torre ' + tipo
    elif retorno == 'k':
        return 'Caballo ' + tipo
    elif retorno == 'a':
        return 'Alfil ' + tipo
    elif retorno == 'q':
        return 'Reina ' + tipo
    elif retorno == 'r':
        return 'Rey ' + tipo
    else:
        return 'No es una pieza'

def mover_peon(tablero,x_inicial,y_inicial,x_final,y_final):
    '''
    ([][],int,int,int,int)-> [][]: tablero resultante del movimiento de un peon.

    :param tablero: [][]: matriz con la posicion de las fichas
    :param x_inicial: int: entero indocando posicion en x inicial
    :param y_inicial: int: entero indocando posicion en y inicial
    :param x_final: int: entero indocando posicion en x final
    :param y_final: int: entero indocando posicion en y final
    :return: [][] tablero resultante
    '''

    ficha = tablero[x_inicial][y_inicial]
    peon = 'pP'
    if (ficha not in peon):
        raise TypeError('no es un peon')

    ultima_posicion = tablero[x_final][y_final]
    have_to_eat = False
    team = ficha.islower()
    team2 = False
    if (ultima_posicion != ' '):
        team2 = ultima_posicion.islower()
        if (team == team2):
            raise TypeError('camino bloqueado')
    if(x_final>x_inicial and team):
        x_diferencia = x_final - x_inicial
    elif(x_final<x_inicial and team2):
        x_diferencia = x_inicial-x_final
    else:
        return 'movimiento invalido'

    maxmov = 0
    if x_inicial == 1 or x_inicial == 6:
        maxmov = 2
    else:
        maxmov = 1

    if x_diferencia>2 or x_diferencia>maxmov:
        return 'movimiento_invalido'


    try:
        for fila in range(x_inicial, x_final):
            if (x_inicial == x_final):
                break
            if fila==x_inicial:
                continue
            elif fila != x_inicial and tablero[fila][y_inicial] != ' ' and x_diferencia!=2:
                have_to_eat = True
                tablero[fila][y_inicial] = ficha
                break
            elif fila != x_inicial and tablero[fila][y_inicial] == ' ' and x_diferencia == 2:
                return 'movimiento invalido'




        for columna in range(y_inicial, y_final):
            if (y_inicial == y_final):
                break
            elif columna != y_inicial and columna != y_final and tablero[x_inicial][columna] != ' ':
                return 'camino bloqueado'

        tablero[x_final][y_final] = ficha
        tablero[x_inicial][y_inicial] = ' '

        tablero = tablero_a_cadena(tablero)
    except:
        TypeError('la posicion esta fuera del tablero')

    return tablero;


def mover_torre(tablero, x_inicial, y_inicial, x_final, y_final):
    '''
    ([][],int,int,int,int)-> [][]: tablero resultante del movimiento de una torre.


    :param tablero: [][]: matriz con la posicion de las fichas
    :param x_inicial: int: entero indocando posicion en x inicial
    :param y_inicial: int: entero indocando posicion en y inicial
    :param x_final: int: entero indocando posicion en x final
    :param y_final: int: entero indocando posicion en y final
    :return: [][] tablero resultante
    '''

    ficha =  tablero[x_inicial][y_inicial]
    torre = 'tT'
    if (ficha not in torre):
        return 'no es una torre'

    ultima_posicion = tablero[x_final][y_final]
    team = ficha.islower()
    team2= False
    if (ultima_posicion != ' '):
        team2 = ultima_posicion.islower()
        if(team==team2):
            return 'camino bloqueado'

    if x_inicial!=x_final and y_inicial!=y_final:
       return 'movimiento invalido'
    try:
        for fila in range(x_inicial,x_final):
            if(x_inicial == x_final):
                break
            elif fila != x_inicial and fila != x_final and tablero[fila][y_inicial] != ' ':
                return 'camino bloqueado'

        for columna in range(y_inicial,y_final):
            if (y_inicial == y_final):
                break
            elif columna != y_inicial and columna != y_final and tablero[x_inicial][columna] != ' ':
                return 'camino bloqueado'
    except:
        TypeError('la posicion no existe en el tablero')


    tablero[x_final][y_final] = ficha
    tablero[x_inicial][y_inicial] = ' '

    tablero = tablero_a_cadena(tablero)

    return tablero;




print(mover_torre(tablero, 0, 0, 1, 0))

