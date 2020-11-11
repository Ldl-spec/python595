import random

class NumericalIntegrator():

    def __init__(self):
        n = 0
        m = 0

    def integrate(self, lower_bound, upper_bound):

        count = 0

        x_min, x_max = lower_bound, self.m(upper_bound)
        y_min, y_max = lower_bound, self.m(upper_bound)

        for i in range(0, self.n):
            x = random.uniform(x_min, x_max)
            y = random.uniform(y_min, y_max)

            if x * x > y:
                count += 1

        integral_value = count / float(self.n)
        return integral_value


    def set_objective(self, a):
        self.m = a

    def set_scenarios(self, n):
        self.n = n