from estimator.estimator import Estimator


class RungeEstimator(Estimator):
    
    def to_string(self):
        return 'Runge Estimator Method'
    
    def estimate(self, a, b, h, integral, method):
        return abs(method.execute(a, b, h, integral) - method.execute(a, b, h * 2, integral)) / 12
    
