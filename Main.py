
from Border import Border
from Individual import Individual
from Map import Map
from Population import Population
from Searches import bfsWithBack,bfsWithBackForward,bfsWithBackAC3,minConflicts
import time
import secrets



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
def createMapGraph():
    with open('smallstates.txt', 'r') as file:
        data = file.read()
    graph = {}
    lines = data.split("\n")
    for line in lines:
        if line:
            state_codes = line.split(",")
            first_state = state_codes[0]
            connected_states = state_codes[1:]
            graph[first_state] = connected_states
    return graph


if __name__ == '__main__':
    # Example graph represented as an adjacency list

    graph = createMapGraph()
    colors = ['Red', 'Green', 'Blue', 'Yellow']
    initial = input("would you like a state initialized(Florida always red) input 0 or 1")
    if initial != 1 or initial != 0:
        initial = 0 #makes sure that the program will run if wrong input is entered

    before = float(time.time())
    mapSolver = bfsWithBack(graph)
    solution = mapSolver.mapColoring(colors, initial)
    after = float(time.time())
    if solution:
        print("Map coloring solution found with backtracking in :",after-before)
        for node, color in solution.items():
            print(f"{node}: {color}")
    else:
        print("No solution found.")

    before = float(time.time())
    mapSolver = bfsWithBackForward(graph, colors, initial)
    solution = mapSolver.solve()
    after = float(time.time())
    if solution:
        print("Map coloring solution found with backtracking and forward in:",after-before)
        for node, color in solution.items():
            print(f"{node}: {color}")
    else:
        print("No solution found.")

    before = float(time.time())
    mapSolver = bfsWithBackAC3(graph, colors, initial)
    solution = mapSolver.solve()
    after = float(time.time())
    if solution:
        print("Map coloring solution found with backtracking and ac3 in:",after-before)
        for node, color in solution.items():
            print(f"{node}: {color}")
    else:
        print("No solution found.")

    before = float(time.time())
    mapSolver = minConflicts(graph, colors, initial)
    solution = mapSolver.solve()
    after = float(time.time())
    if solution:
        print("Map coloring solution found with min-conflicts in:",after-before)
        for node, color in solution.items():
            print(f"{node}: {color}")
    else:
        print("No solution found within the maximum number of steps.")

    # bigmap = createBigMap()
    map = Map()
    initMap(map)
    before = float(time.time())
    populationSize = 10  # TODO find a reasonable value
    population = Population(map, populationSize)
    maxIterations = 200000  # TODO find a reasonable value
    currentIteration = 0
    goalFound = False
    bestIndividual = Individual(map)  # to hold the individual representing the goal, if any
    while currentIteration < maxIterations and not goalFound:
        newPopulation = Population(map, 0)
        for i in range(populationSize):
            x = population.randomSelection()
            y = population.randomSelection()
            child = x.reproduce(x, y)
            if secrets.SystemRandom().randint(0, 200) == 23:  # TODO use a small probability instead
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
        after = float(time.time())
    else:
        print("Did not find a solution after", currentIteration, "iterations")
        after = float(time.time())
    print("Map coloring solution found with genetic algorithm in:",after-before)







