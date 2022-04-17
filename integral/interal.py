class Integral:

    def __init__(self, Fx = None, Exp = None, DiscreatePoints = None):
        self.Fx = Fx
        self.Exp = Exp
        self.DiscreatePoints = DiscreatePoints
        return
   
    def to_string(self):
        return self.Fx