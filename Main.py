import random

from Border import Border
from Individual import Individual
from Map import Map
from Population import Population

# Author Fan Zhang
def createBigMap():
    # Creates a Map object with all of the states from bigstates.txt
    map = Map()
    uniqueStates = set()
    uniqueBorders = set()
    with open('bigstates.txt', 'r') as file:
        for line in file:
            stateCodes = line.strip().split(',')
            # Add the first state code to the map's states list and the set
            if stateCodes[0] not in uniqueStates:
                map.states.append(stateCodes[0])
                uniqueStates.add(stateCodes[0])
            for i in range(1, len(stateCodes)):
                # Add the next state code to the states list and the set
                if stateCodes[i] not in uniqueStates:
                    map.states.append(stateCodes[i])
                    uniqueStates.add(stateCodes[i])
                # Create a border between the first state and the following state if it doesn't exist
                border = (map.states.index(stateCodes[0]), map.states.index(stateCodes[i]))
                # Check if the border or its reverse already exists
                if border not in uniqueBorders and (border[1], border[0]) not in uniqueBorders:
                    map.borders.append(Border(*border))
                    uniqueBorders.add(border)
    return map


def initMap(map):
    map.states.append("North Carolina")
    map.states.append("South Carolina")
    map.states.append("Virginia")
    map.states.append("Tennessee")
    map.states.append("Kentucky")
    map.states.append("West Virginia")
    map.states.append("Georgia")
    map.states.append("Alabama")
    map.states.append("Mississippi")
    map.states.append("Florida")

    map.borders.append(Border(0, 1))
    map.borders.append(Border(0, 2))
    map.borders.append(Border(0, 3))
    map.borders.append(Border(0, 6))
    map.borders.append(Border(1, 6))
    map.borders.append(Border(2, 3))
    map.borders.append(Border(2, 4))
    map.borders.append(Border(2, 5))
    map.borders.append(Border(3, 4))
    map.borders.append(Border(3, 6))
    map.borders.append(Border(3, 7))
    map.borders.append(Border(3, 8))
    map.borders.append(Border(4, 5))
    map.borders.append(Border(6, 7))
    map.borders.append(Border(6, 9))
    map.borders.append(Border(7, 8))
    map.borders.append(Border(7, 9))

if __name__ == '__main__':
    #bigmap = createBigMap()
    map = Map()
    initMap(map)
    populationSize = 10
    population = Population(map, populationSize)
    maxIterations = 20000
    currentIteration = 0
    goalFound = False
    bestIndividual = Individual(map)  # to hold the individual representing the goal, if any
    while currentIteration < maxIterations and not goalFound:
        newPopulation = Population(map, 0)
        for i in range(populationSize):
            x = population.randomSelection()
            y = population.randomSelection()
            child = x.reproduce(x, y)
            if random.randint(0,200) == 23:
                child.mutate()
            if child.isGoal():
                goalFound = True
                bestIndividual = child
            newPopulation.vector.append(child)
        currentIteration += 1
        population = newPopulation

    if goalFound:
        print("Found a solution after", currentIteration, "iterations")
        bestIndividual.printresult()
    else:
        print("Did not find a solution after", currentIteration, "iterations")
