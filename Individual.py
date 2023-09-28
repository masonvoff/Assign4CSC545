import random
# Author Fan Zhang
class Individual:

    def __init__(self,map):
        self.map = map# the map
        self.fitness=1# fitness is cached and only updated on request whenever necessary
        self.genome = len(map.states)
        self.genome = self.randomColors()
        self.updateFitness()
    # Updates the fitness value based on the genome and the map.
    def singleColor(self,change):
        #changes one color
        colors = ["Red", "Blue", "Green", "Yellow"]
        change = colors[random.randint(0,3)]
        return change

    def randomColors(self):
        #assigns colors randomly to states
        colors = ["Red", "Blue", "Green", "Yellow"]
        colorAssignments = {}
        random.shuffle(colors)
        for state in self.map.states:
            colorAssignments[state] = colors[random.randint(0,3)]
        return colorAssignments

    def calculateFitness(self):
        ones_count = 0
        fitness = 0
        for all in self.map.borders:
            firstIn = self.map.states[self.map.borders[ones_count].index1]
            secondIn = self.map.states[self.map.borders[ones_count].index2]
            if self.genome[firstIn] == self.genome[secondIn]:
                #if two states touching have same color add one fitness
                fitness += 1
            ones_count += 1
        return fitness

    def updateFitness(self):
        self.fitness = self.calculateFitness()

    # Reproduces a child randomly from two individuals (see textbook).
    # x The first parent.
    # y The second parent.
    # return The child created from the two individuals.
    def reproduce(self, x, y):
        child = Individual(self.map)  # Create a new individual with the same map
        child.genome = self.genome
        counter = 0
        for all in self.map.borders:
            firstIn = self.map.states[self.map.borders[counter].index1]
            secondIn = self.map.states[self.map.borders[counter].index2]
            if self.genome[firstIn] == self.genome[secondIn] and y.genome[firstIn] != y.genome[secondIn]:
                #if y has different second state and x has a collision then the childs second state is changed to y's state

                child.genome[firstIn] = y.genome[firstIn]
                child.genome[secondIn] = y.genome[secondIn]
            else:
                #randomly change the color if it cannot be merged
                child.genome[firstIn] = self.singleColor(firstIn)
                child.genome[secondIn] = self.singleColor(secondIn)
        child.updateFitness()
        return child

    # Randomly mutates the individual.
    def mutate(self):
        #simply rerandomizes an individual
        self.genome = self.randomColors()

    def isGoal(self):
        if self.fitness == 0:
            return True

    def printresult(self):
        print("Your result:")
        # TODO implement printing the individual in the following format:
        # fitness: 15
        # North
        # Carolina: 0
        # South Carolina: 2
        # ...
        print(self.fitness)
        print(self.genome)
