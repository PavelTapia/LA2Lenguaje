import sys
import ply.lex as lex

"""
El módulo sys es el encargado de proveer variables y funcionalidades,
directamente relacionadas con el intérprete.
    sys.argv:
        Retorna una lista con todos los argumentos pasados por línea de
        comandos. Al ejecutar python modulo.py arg1 arg2,
        retornará una lista: ['modulo.py', 'arg1', 'arg2']
"""

def nombre = '\w'

tokens = (
    'break',
    'case',
    'class',
    'Const',
    'else',
    'for',
    'if',
    'import',
    'new',
	'package',
    'private',
    'public',
    'return',
    'switch',
    'void',
    'while',
    'and',
    'or',
	'print',
    'read',
    'bool',
	'char',
    'float',
    'int',
	'suma',
    'resta',
    'mult',
	'div',
    'llaveizq',
	'llaveder'
    'menorque',
	'mayorque',
    'igual',
    'negacion',
	'comentario',
    'comillaizq',
    'comillader',	
	#'parentesisizq',
	#'parentesisder'
)

def t_break(t):
    
    return t

def t_case(t):
    
    return t

def t_class(t):
    
    return t	
	
def t_const(t):
    
    return t

def t_else(t):
    
    return t
	
def t_for(t):
    
    return t

def t_if(t):
    
    return t

def t_import(t):
    
    return t
	
def t_new(t):
    
    return t	
	
def t_package(t):
    
    return t

def t_private(t):
    
    return t

def t_public(t):
    
    return t

def t_return(t):
    
    return t

def t_switch(t):
    
    return t

def t_void(t):
    
    return t

def t_while(t):
    
    return t

def t_and(t):
    
    return t	
	
def t_or(t):
    
    return t
	
def t_print(t):
    
    return t

def t_read(t):
    
    return t	
	
def t_bool(t):
    
    return t

def t_char(t):
    
    return t

def t_float(t):
    
    return t

def t_int(t):
    
    return t

def t_suma(t):
    
    return t

def t_menos(t):
    
    return t

def t_mult(t):
    
    return t	

def t_div(t):
    
    return t

def t_llaveizq(t):
    
    return t
	
def t_llaveder(t):
    
    return t	

def t_menorque(t):
    
    return t	
	
def t_mayorque(t):
    
    return t	
	
def t_igual(t):
    
    return t

def t_negacion(t):
    
    return t	
	
def t_comentario(t):
    
    return t

def t_comillaizq(t):
    
    return t	
	
def t_comillader(t):
    
    return t	
	
		
	
# Patron para saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Patron que contiene caracteres ignorados (espacios y tabuladores)
t_ignore = ' \t'


# Regla de manejo de errores
def t_error(t):
    print("{:15}|{:15}|{:5}|".format(
        t.value[0], "ERROR", t.lineno))
    t.lexer.skip(1)


"""
t.type   = Token encontrado
t.value  = Valor del lexema.
t.lineno = El numero de la linea donde se encontro el lexema
"""


def analisis_lexico(data):
    analizador = lex.lex()
    analizador.input(data)
    while True:
        t = analizador.token()
        if not t:
            break
        print("{:15}|{:15}|{:5}|{:5}".format(
            t.value, t.type, t.lineno, last))


if __name__ == '__main__':
    file = open(str(sys.argv[1]), "r")
    print("{:15}|{:15}|{:5}|{:5}".format(
        "LEXEMA", "TOKEN", "LINEA", "POSICION"))
    analisis_lexico(file.read())
