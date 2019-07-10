import math
import re
import cmath
import constants

def complex_eval(expression):
    print expression
    expression = expression.replace(" ", "")
    expression = expression.replace("^", "**")


    for bincomplex in re.findall(constants.get("REGEX_BINOM"), expression):
        print bincomplex
        bincomplex = bincomplex[0]
        bincomplex_list = bincomplex.strip("(").strip(")").split(",")
        
        expression = expression.replace(bincomplex, "({}+{}j)".format(bincomplex_list[0],bincomplex_list[1] ))

    for polcomplex in re.findall(constants.get("REGEX_POLAR"), expression):
        print polcomplex
        polcomplex = polcomplex[0]
        polcomplex_list = polcomplex.strip("[").strip("]").split(";")
        real = math.cos(float(polcomplex_list[1])) * float(polcomplex_list[0])
        imag = math.sin(float(polcomplex_list[1])) * float(polcomplex_list[0]) 
        expression = expression.replace(polcomplex, "({}+{}j)".format(real,imag ))

    print expression
    return eval(expression)

def to_binomic(z):
    print z
    return "({},{})".format(str(z.real), str(z.imag) )

def to_polar(z):
    print z
    z = cmath.polar(z)
    return "[{};{}]".format(str(z[0]), str(z[1]))

def to_z(expression):
    if is_binom(expression):
        expression_list = expression.strip("(").strip(")").split(",")
        return complex(float(expression_list[0]),float(expression_list[1] ))

    if is_polar(expression):
        expression_list = expression.strip("[").strip("]").split(";")
        real = math.cos(float(expression_list[1])) * float(expression_list[0])
        imag = math.sin(float(expression_list[1])) * float(expression_list[0]) 
        return complex(real,imag)
        
    return expression
         

def toggle(expression):
    if is_binom(expression) and is_binom(expression) == len(expression):
        print expression
        expression_list = expression.strip("(").strip(")").split(",")
        z = complex(float(expression_list[0]),float(expression_list[1] ))
        return to_polar(z)

    if is_polar(expression) and is_polar(expression) == len(expression):
        print expression
        expression_list = expression.strip("[").strip("]").split(";")
        real = math.cos(float(expression_list[1])) * float(expression_list[0])
        imag = math.sin(float(expression_list[1])) * float(expression_list[0]) 
        z = complex(real,imag)
        return to_binomic(z)
    return expression

def is_polar(expression):
    match = re.match(constants.get("REGEX_POLAR"), expression)
    if match:
        return len(match.group(0))
    return 0

def is_binom(expression):
    match = re.match(constants.get("REGEX_BINOM"), expression)
    if match:
        return len(match.group(0))
    return 0

