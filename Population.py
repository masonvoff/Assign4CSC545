#Class representing a population of individuals
# Author Fan Zhang

from Individual import Individual
import secrets

class Population:
	# Actual standard ctor.
	# param map The map.
	# param initialSize The initial size of the population.
    def __init__(self,map,initialSize):
        self.vector=[]
        for i in range(initialSize):
            self.vector.append(Individual(map))

    # Randomly selects an individual out of the population
    # proportionally to its fitness.
    # return The selected individual.
    def randomSelection(self):
        # Randomly select an individual from the population
        return secrets.SystemRandom().choice(self.vector)
