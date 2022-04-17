import math
from estimator.runge_estimator import RungeEstimator
from integral.interal import Integral
from method.trapezoidal import Trapezoidal
from solver.solver import Solver
class Invoker:


    def __init__(self):
        self.integrals = []
        self.estimators = []
        self.methods = []
        return

    def invoke(self):
        print('> Welcome to the integral world!')

        self.initIntegrals()
        self.initMethods()
        self.initEstimators()

        while True:
            self.pickIntegral()
            self.pickMethod()
            self.pickEstimator()
            solver = Solver(self.integrals[self.picked_integral], self.methods[self.picked_method], self.estimators[self.picked_estimator])
            result = solver.solve()

            if isinstance(result, str):
                print(result)
            else:
                print('----------RESULT----------')
                print("> Result: {}".format(result['result']))
                print("> Number of steps: {}".format(result['steps']))
                print("> Number of splits: {}".format(result['splits']))
                print("> Error: {}".format(result['error']))

            inp = input("> Do you want to continue? (Y/N): ")
            if inp == 'N':
                exit(0)
        

    def initIntegrals(self):
        self.integrals = [
            Integral("3x^2 + 2", lambda x: 3 * math.pow(x, 2) + 2),
            Integral("sin(x) + 4x^3 - x", lambda x: math.sin(x) + 4 * math.pow(x, 3) - x),
            Integral("e^x + cos(x) - x^3", lambda x: math.exp(x) + math.cos(x) - math.pow(x, 3)),
            Integral("ln(x) - e^x", lambda x: math.log(x) - math.exp(x), [0]),
            Integral("1/x", lambda x: 1/x, [0])
        ]
    
    def pickIntegral(self):
        print('----------INTEGRALS----------')
        print('> Which integral do you want to pick?', end='')
        for i, option in enumerate(self.integrals):
            print("> {}. {}".format(i, option.to_string()))


        while True:
            print("> Enter your variant: ", end='')
            self.picked_integral = int(input())
            if (self.picked_integral >= len(self.integrals)) or (self.picked_integral < 0):
                print("> Option invalid. Please pick again!")
                continue
            break
        

    def initMethods(self):
        self.methods = [
            Trapezoidal()
        ]


    def pickMethod(self):
        print('----------METHODS----------')
        print('> Which method do you want to pick?')
        for i, option in enumerate(self.methods):
            print("> {}. {}".format(i, option.to_string()))


        while True:
            print("> Enter your variant: ", end='')
            self.picked_method = int(input())
            if (self.picked_method >= len(self.methods)) or (self.picked_method < 0):
                print("> Option invalid. Please pick again!")
                continue
            break
        

    def initEstimators(self):
        self.estimators = [
            RungeEstimator()
        ]

    def pickEstimator(self):
        print('----------ESTIMATORS----------')
        print('> Which estimator do you want to pick?')
        for i, option in enumerate(self.estimators):
            print("> {}. {}".format(i, option.to_string()))


        while True:
            print("> Enter your variant: ", end='')
            self.picked_estimator = int(input())
            if (self.picked_estimator >= len(self.estimators)) or (self.picked_estimator < 0):
                print("> Option invalid. Please pick again!")
                continue
            break