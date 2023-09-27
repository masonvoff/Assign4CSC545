import random
# Author Fan Zhang
class Individual:

    def __init__(self,map):
        self.map = map# the map
        self.fitness=0# fitness is cached and only updated on request whenever necessary
        # TODO some representation of the genome of the individual
        self.genome = len(map.states)
        # TODO implement random generation of an individual
        self.genome = self.randomColors()
        self.updateFitness()
    # Updates the fitness value based on the genome and the map.
    def randomColors(self):
        colors = ["Red", "Blue", "Green", "Yellow"]
        colorAssignments = {}
        random.shuffle(colors)
        for state in self.map.states:
            color = colors.pop(0)
            colorAssignments[state] = color
            colors.append(color)
        return colorAssignments

    def calculateFitness(self):
        ones_count = 0
        firstIn = 0
        secondIn = 0
        for all in self.genome:
            #print(self.map.states[self.map.borders[ones_count].index1])
            firstIn = self.map.states[self.map.borders[ones_count].index1]
            secondIn = self.map.states[self.map.borders[ones_count].index2]
            #print(firstIn,secondIn)
            print("the values here: ",self.genome[firstIn], self.genome[secondIn])
            if self.genome[firstIn] == self.genome[secondIn]:
                print("collision")
            ones_count += 1
            #this is what i need to finish
            #idea was to check all colors in genome to see if they are different
        return ones_count

    def updateFitness(self):
        #TODO implement fitness function
        self.fitness=self.calculateFitness()

    # Reproduces a child randomly from two individuals (see textbook).
    # x The first parent.
    # y The second parent.
    # return The child created from the two individuals.
    def reproduce(self, x, y):
        child = Individual(self.map)  # Create a new individual with the same map
        # TODO reproduce child from individuals x and y
        child.updateFitness()
        return child

    # Randomly mutates the individual.
    def mutate(self):
        # TODO implement random mutation of the individual
        self.updateFitness()

    # Checks whether the individual represents a valid goal state.
    # return Whether the individual represents a valid goal state.
    def isGoal(self):
        return self.fitness == len(self.map.borders)

    def printresult(self):
        print("Your result:")
        # TODO implement printing the individual in the following format:
        # fitness: 15
        # North
        # Carolina: 0
        # South Carolina: 2
        # ...
