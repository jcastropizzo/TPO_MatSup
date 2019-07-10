import math

class PolarComplex(object):

    def __init__(self, module, arg):
        self.module = module
        self.arg = arg

    # def print(self):
    #     return '' + self.module + 'arg(' + self.arg + ')'

    @property
    def real(self):
        return math.cos(self.arg) * self.module

    @property
    def imaginary(self):
        return math.sin(self.arg) * self.module

