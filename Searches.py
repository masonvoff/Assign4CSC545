from collections import deque
import secrets


class bfsWithBack():
    def __init__(self, graph):
        self.graph = graph

    def isValid(self, node, color, colorMap):
        for neighbor in self.graph[node]:
            if neighbor in colorMap and colorMap[neighbor] == color:
                return False
        return True

    def mapColoring(self, colors, initial):
        queue = deque()
        queue.append({})
        while queue:
            colorMap = queue.popleft()
            if len(colorMap) == len(self.graph):
                return colorMap
            node = next(iter(set(self.graph.keys()) - set(colorMap.keys())))
            if initial != 1:
                for color in colors:
                    if self.isValid(node, color, colorMap):
                        newColorMap = colorMap.copy()
                        newColorMap[node] = color
                        queue.append(newColorMap)
            else:
                newColorMap = colorMap.copy()
                newColorMap[node] = colors[0]
                queue.append(newColorMap)
                initial = 0
        return None


class bfsWithBackForward():
    def __init__(self, graph, colors, initial=0):
        self.graph = graph
        self.colors = colors
        self.assignment = {}
        if initial == 1:
            self.assignment["FL"] = 'Red'

    def isValid(self, node, color, colorMap):
        for neighbor in self.graph[node]:
            if neighbor in colorMap and colorMap[neighbor] == color:
                return False
        return True

    def forwardCheck(self, node, color, colorMap):
        invalid = set()
        for neighbor in self.graph[node]:
            if neighbor not in colorMap:
                invalid.add(color for color in self.colors if not self.isValid(neighbor, color, colorMap))
        return invalid

    def solve(self):
        queue = deque()
        queue.append({})
        while queue:
            colorMap = queue.popleft()
            if len(colorMap) == len(self.graph):
                return colorMap
            node = next(iter(set(self.graph.keys()) - set(colorMap.keys())))
            for color in self.colors:
                if self.isValid(node, color, colorMap):
                    forwardCheckVal = self.forwardCheck(node, color, colorMap)
                    if all(forwardCheckVal):
                        newColorMap = colorMap.copy()
                        newColorMap[node] = color
                        queue.append(newColorMap)
        return None


class bfsWithBackAC3():
    def __init__(self, graph, colors, initial=0):
        self.graph = graph
        self.colors = colors
        self.assignment = {}
        if initial == 1:
            self.assignment["FL"] = 'Red'

    def isValid(self, node, color, colorMap):
        for neighbor in self.graph[node]:
            if neighbor in colorMap and colorMap[neighbor] == color:
                return False
        return True

    def ac3(self):
        queue = deque([(state1, state2) for state1 in self.graph.keys() for state2 in self.graph[state1]])
        while queue:
            state1, state2 = queue.popleft()
            if self.revise(state1, state2):
                if not self.colors[state1]:
                    return False
                for neighbor in self.graph[state1]:
                    if neighbor != state2:
                        queue.append((neighbor, state1))
        return True

    def revise(self, state1, state2):
        revised = False
        counter = 0
        for color1 in self.colors:
            counter += 1
            if not any(self.isValid(state2, color2, self.assignment) for color2 in self.colors):
                self.colors[state1].remove(color1)
                revised = True
        return revised

    def solve(self):
        if not self.ac3():
            return None
        for node in self.graph.keys():
            if node not in self.assignment:
                for color in self.colors:
                    if self.isValid(node, color, self.assignment):
                        self.assignment[node] = color
                        break

        if len(self.assignment) == len(self.graph):
            return self.assignment
        return None


class minConflicts():
    def __init__(self, graph, colors, initial, maxSteps=10000):
        self.graph = graph
        self.colors = colors
        self.assignment = {node: secrets.SystemRandom().choice(colors) for node in graph.keys()}
        self.max_steps = maxSteps
        if initial == 1:
            self.assignment["FL"] = 'Red'

    def isValidColor(self, node, color, colorMap):
        for neighbor in self.graph[node]:
            if neighbor in colorMap and colorMap[neighbor] == color:
                return False
        return True

    def countConflicts(self, node, color, colorMap):
        conflicts = 0
        for neighbor in self.graph[node]:
            if neighbor in colorMap and colorMap[neighbor] == color:
                conflicts += 1
        return conflicts

    def minConflictsVal(self, node, colorMap):
        minConflicts = float('inf')
        minColor = None
        for color in self.colors:
            conflicts = self.countConflicts(node, color, colorMap)
            if conflicts < minConflicts:
                minConflicts = conflicts
                minColor = color
        return minColor

    def solve(self):
        for _ in range(self.max_steps):
            conflictedNodes = [node for node in self.assignment.keys() if not self.isValidColor(node, self.assignment[node], self.assignment)]
            if not conflictedNodes:
                return self.assignment
            node = secrets.SystemRandom().choice(conflictedNodes)
            newColor = self.minConflictsVal(node, self.assignment)
            self.assignment[node] = newColor
        return None
