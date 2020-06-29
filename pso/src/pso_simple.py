from src.cost_function import CostFunction
from src.particle import Particle


class PSOSimple(object):

    def run(self):
        initial = [5, 5]
        bounds = [(-10, 10), (-10, 10)]
        self.__minimize(CostFunction.sphere,
                        initial,
                        bounds,
                        num_particles=15,
                        maxiter=30,
                        verbose=True)

    def __minimize(self, constFunc, x0, bounds, num_particles, maxiter, verbose=False):
        err_best_g = -1
        pos_best_g = []

        swarm = []

        for i in range(0, num_particles):
            swarm.append(Particle(x0))

        i = 0
        while i < maxiter:

            if verbose:
                print(f'iter: {i:>4d}, best solution: {err_best_g:10.6f}')

            for j in range(0, num_particles):
                swarm[j].evaluate(constFunc)

                if swarm[j].err < err_best_g or err_best_g == -1:
                    pos_best_g = list(swarm[j].position)
                    err_best_g = float(swarm[j].err)

            for j in range(num_particles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)
            i = i + 1

        print('\nFINAL SOLUTION:')
        print(f'   > {pos_best_g}')
        print(f'   > {err_best_g}\n')