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
        scale = 1.5
        plt.xlim(-abs(z.imag * scale),abs(z.imag * scale))
        plt.ylim(-abs(z.real * scale),abs(z.real * scale))

        plt.title('({};{})'.format(str(z.real),str(z.imag)),fontsize=10)
        plt.show()
        return
    except Exception as ex:
        print ex
        return