import math


class Solver:
    def __init__(self, integral, method, estimator):
        self.integral = integral
        self.method = method
        self.estimator = estimator
    
    def solve(self):
        print('> Enter your parameters (a, b, epsilon): ', end='')
        a, b, eps = map(float, input().split())
        print('{} {} {}'.format(a, b, eps))
        while True:
            is_continous = True
            break_point = None
            if self.integral.get_discrete_points() != None:
                for pt in self.integral.get_discrete_points():
                    if (a <= pt and pt <= b) or (a >= pt and pt >= b):
                        is_continous = False
                        break_point = pt
                        print("The interval is not continous at point {}".format(pt))
                        break
            if is_continous is False:
                print("> Do you want to continue calculate the LEFT part or the RIGHT of the integral? (L/R):", end='')
                direct = input()
                breakpt_eps = min(eps, abs(b - a) / 2)
                if direct == 'L':
                    if b > a: 
                        b = break_point - breakpt_eps
                    else:
                        a = break_point - breakpt_eps
                else:
                    if b > a:
                        a = break_point + breakpt_eps
                    else:
                        b = break_point + breakpt_eps
                print("> New parameters (a, b, epsilon): ({}, {}, {})".format(a, b, eps), end='')
            else:
                break

        h = math.pow(eps, 1/4)
        cnt_split = 0
        while self.estimator.estimate(a, b, h, self.integral, self.method) >= eps:
            cnt_split += 1
            h /= 2
        
        res = dict()
        res['result'] = self.method.execute(a, b, h, self.integral)
        res['steps'] = math.ceil(abs(b-a)/h)
        res['splits'] = cnt_split
        res['error'] = self.estimator.estimate(a, b, h, self.integral, self.method)
        return res
        