import math
from re import A
from method.method import Method


class Trapezoidal(Method):
    def execute(self, a, b, h, integral):
        mul = 1
        if a > b:
            a, b = b, a
            mul = -1
        
        n = math.ceil((b - a) / h)
        ans = 0
        for i in range(1, n + 1):
            ans += h/2 * (integral.f(a + (i-1)*h) + integral.f(a + i*h))
        return ans * mul
    
    def to_string(self):
        return 'Trapezoidal Method'