import UI.MainMenu as menu
import math
# import Models.PolarComplex 
# from  Models import BinomicComplex
import matplotlib.pyplot as plt
import numpy as np
import re
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
        scale = 1.5
        plt.xlim(-abs(z.imag * scale),abs(z.imag * scale))
        plt.ylim(-abs(z.real * scale),abs(z.real * scale))

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


        
    

def complex_eval(expression = "(1,2)+(4,6)"):
    expression = expression.replace(" ", "")
    expression = expression.replace(";", ",")


    for bincomplex in re.findall("(.\d*.,.\d*.)", expression):
        print bincomplex
        bincomplex_str =bincomplex.strip("(").strip(")")
        bincomplex = bincomplex_str.split(",")
        
        expression = expression.replace(bincomplex_str, "({}+{}j)".format(bincomplex[0],bincomplex[1] ))

    # for polcomplex in re.findall("[.\d*.,.\d*.]", expression):
    #     print polcomplex
    #     polcomplex_str = polcomplex.strip("[").strip("]")
    #     polcomplex = polcomplex_str.split(",")
    #     real = math.cos(polcomplex[1]) * polcomplex[0]
    #     imag = math.sin(polcomplex[1]) * polcomplex[0]
    #     expression = expression.replace(polcomplex_str, "({}+{})".format(real,imag ))
    
    return eval(expression)



if __name__ == "__main__":
    # menu.start()
    # menu.init()
    print complex_eval()
    # graphicate(complex(3,4))
    exit(0)