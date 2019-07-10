import math
import re
import cmath


def complex_eval(expression):
    print expression
    expression = expression.replace(" ", "")
    expression = expression.replace("^", "**")


    for bincomplex in re.findall("(\((-|).*,(-|).*\))", expression):
        print bincomplex
        bincomplex = bincomplex[0]
        bincomplex_list = bincomplex.strip("(").strip(")").split(",")
        
        expression = expression.replace(bincomplex, "({}+{}j)".format(bincomplex_list[0],bincomplex_list[1] ))

    for polcomplex in re.findall("(\[(-|).*;(-|).*\])", expression):
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
    return "[{};{}]".format(str(z[0]), str(z[1]) )

def toggle(expression):
    if re.match("(\((-|).*,(-|).*\))", expression) and len(re.match("(\((-|).*,(-|).*\))", expression).group(0)) == len(expression):
        print expression
        expression_list = expression.strip("(").strip(")").split(",")
        z = complex(float(expression_list[0]),float(expression_list[1] ))
        return to_polar(z)

    if re.match("(\[(-|).*;(-|).*\])", expression) and len(re.match("(\[(-|).*;(-|).*\])", expression).group(0)) == len(expression):
        print expression
        expression_list = expression.strip("[").strip("]").split(";")
        real = math.cos(float(expression_list[1])) * float(expression_list[0])
        imag = math.sin(float(expression_list[1])) * float(expression_list[0]) 
        z = complex(real,imag)
        return to_binomic(z)

    return expression


