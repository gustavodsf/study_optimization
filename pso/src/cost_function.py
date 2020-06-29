class CostFunction(object):

    @staticmethod
    def sphere(x):
        total = 0
        for i in range(len(x)):
            total = total + x[i]**2
        return total
