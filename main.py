import UI.MainMenu as menu
import math
# import Models.PolarComplex 
# from  Models import BinomicComplex
import matplotlib.pyplot as plt
import numpy as np

def graphicate(z):
    try:
        X = np.array((0))
        Y= np.array((0))
        U = np.array((z.imag))
        V = np.array((z.real))

        fig, ax = plt.subplots()
        q = ax.quiver(X, Y, U, V,units='xy' ,scale=1)

        plt.grid()
        plt.autoscale(enable=True, axis='y')
        ax.set_aspect('equal')

        plt.xlim(-5,5)
        plt.ylim(-5,5)

        plt.title('({};{})'.format(str(z.real),str(z.imag)),fontsize=10)
        plt.show()
        return
    except Exception as ex:
        print ex
        return
        
def sum(z, p):
    return z+p
def res(z, p):
    return z-p
def mult(z, p):
    return z*p
def div(z, p):
    return z/p
def pow(z, p):
    return z**p 


        
    

def complex_eval(expression = "(3,5)"):
    expression = expression.replace(" ", "")
    expression = expression.replace(";", ",")
    first_split = ""
    pass



def string_to_complex(expression="(3,4)" ):
    expression = expression.replace(" ", "")
    expression = expression.replace(";", ",")
    evaluated  = eval(expression)

    if "(" in expression:        
        # expression  = evaluated[0] + evaluated[1] + "j"
        return complex(evaluated) 

    if "[" in expression:
        return string_to_complex(polar_to_binomic(expression))
        
    return ""

def polar_to_binomic(expression = "[1,2]"):
    evaluated  = eval(expression)
    return "(" + str(math.cos(evaluated[1]) * evaluated[0]) + "," + str(math.sin(evaluated[1]) * evaluated[0]) + ")"


if __name__ == "__main__":
    # menu.start()
    # menu.init()
    # print string_to_complex()
    # z = PolarComplex.__init__(2, 3)
    # print z
    graphicate(complex(3,4))
    exit(0)