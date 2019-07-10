import math

class BinomicComplex(object):

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # def print(self):
    #     return '', self.real, '+i', self.imaginary

    @property
    def arg(self):
        return math.atan(self.imaginary/self.real)

    @property
    def module(self):
        return math.sqrt((self.real*self.real) + (self.imaginary*self.imaginary))
