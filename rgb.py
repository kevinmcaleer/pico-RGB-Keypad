# RGB class for storing colour values

class RGB():
    """ RGB Colour Class """
    def __init__(self, R=None, G=None, B=None):
        if R is None:
            R = 0
        if G is None:
            G = 0
        if B is None: 
            B = 0
        self.red = R
        self.green = G
        self.blue = B
    
    @property
    def value(self):
        return self.red, self.green, self.blue

    @value.setter
    def value(self,R=None, G=None, B=None):
        if R is None:
            R = 0
        if G is None:
            G = 0
        if B is None: 
            B = 0
        self.red = R
        self.green = G
        self.blue = B 
    
    def show(self):
        print("R:", self.red)
        print("G:", self.green)
        print("B:", self.blue)