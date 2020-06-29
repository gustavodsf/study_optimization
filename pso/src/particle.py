from __future__ import division

import numpy as np


class Particle(object):

    def __init__(self, x0):
        self.position = []
        self.velocity = []
        self.best_position = []
        self.err_best = -1
        self.err = -1
        self.num_dimensions = len(x0)

        for i in range(self.num_dimensions):
            self.velocity.append(np.random.uniform(low=-1.0, high=1.0))
            self.position.append(x0[i])

    def evaluate(self, costFunc):
        self.err = costFunc(self.position)

        if self.err < self.err_best or self.err_best == -1:
            self.best_position = self.position
            self.err_best = self.err

    def update_velocity(self, best_position_global):
        w = 0.5  # constant inertia weight
        c1 = 1   # cognative constant
        c2 = 2  # social constant

        for i in range(0, self.num_dimensions):
            r1 = np.random.random()
            r2 = np.random.random()

            vel_cognitive = c1 * r1 * (self.best_position[i] - self.position[i])
            vel_social = c2 * r2 * (best_position_global[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + vel_cognitive + vel_social

    def update_position(self, bounds):

        for i in range(0, self.num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]

            if self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]

            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
