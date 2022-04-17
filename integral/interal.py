class Integral:

    def __init__(self, Exp = None, Fx = None, discrete_points = None):
        self.Exp = Exp
        self.Fx = Fx
        self.discrete_points = discrete_points
        return
   
    def to_string(self):
        return self.Exp
    
    def get_discrete_points(self):
        return self.discrete_points
    
    def f(self, x):
        return self.Fx(x)