import sys
import os
import math
import time

class Queue:
    def __init__(self, initState):
        self.nodesToExplore = [initState]
        self.nodesExplored = []
        pass

    def push(node):
        self.nodesToExplore.append(node)
    
    def pop():
        node = self.nodesToExplore
        self.nodesExplored.append(node)


class Problem:
    def __init__(self, filename):
        """
            All state is represented as coordinate (x, y), including walls, agent position.
            Map size is presented as (length in Y axis, length in X axis), 
            the bound of X axis is (0, lenX), and the bound of Y axis is (0, lenY)
        """

        
        # Initialize problem configuration
        with open(filename) as f:

            self.mapSize = [int(x) for x in f.readline()[1:-2].strip().split(',')]
            # print("Map Size:\t", self.mapSize)
            self.agentState = [int(x) for x in f.readline()[1:-2].strip().split(',')]
            # print("Agent initial State:\t", self.agentState)

            self.posGoals = []
            for t in f.readline().split('|'):
                coord = t.strip()[1:-1].split(',')
                print(coord)
                self.posGoals.append([int(coord[0]), int(coord[1])])
            # print("Goal States: ", self.posGoals)

            self.walls = []
            s = f.readline()
            while s:
                (x, y, lenX, lenY) = [int(x) for x in s.strip()[1:-1].split(',')]
                for wallX in range(x, x + lenX):
                    for wallY  in range(y, y + lenY):
                        self.walls.append([wallX, wallY])
                s = f.readline()
            # print("Walls: ", self.walls)
    

    def getNextState(self):
        nextStates = []
        candidateStates = [
            [self.agentState[0] + 1, self.agentState[1]],
            [self.agentState[0] - 1, self.agentState[1]],
            [self.agentState[0], self.agentState[1] + 1],
            [self.agentState[0], self.agentState[1] - 1]
        ]
        # valid state
        mapBoundX, mapBoundY = self.mapSize[1], self.mapSize[0]

        for state in candidateStates:
            # if is out of boundary and wall collision
            if state[0] < 0 or state[0] >= mapBoundX:
                pass
            elif state[1] < 0 or state[1] >= mapBoundY:
                pass
            elif state in self.walls:
                pass
            else:
                nextStates.append(state)
        return nextStates
    
    def search(self):
        pass

    # Render map
    def renderMap(self, agentState):
        symbols = {
            'wall': " #",
            'agent': ' o',
            'goal': ' x',
            'area': ' .'
        }
        for x in range(self.mapSize[0]):
            for y in range(self.mapSize[1]):
                if [y, x] in self.walls:
                    print(symbols['wall'], end='')
                elif [y, x] == agentState:
                    print(symbols['agent'], end='')
                elif [y, x] in self.posGoals:
                    print(symbols['goal'], end='')
                else:
                    print(symbols['area'], end='')
            print()
        

# cost function
def cost(state, goal):
    # state: (x, y)
    # goal: (x, y)

    # Manhattan distance
    cost = math.abs(state[0] - goal[0]) + math.abs(state[1] - goal[1])
    # Euclidean distance
    cost = math.sqrt((state[0] - goal[0])^2 + (state[1] - goal[1]))

    return cost



def main(argList):
    # python search.py problems/RobotNav-test.txt bfs
    print(argList)
    problem = Problem(argList[0])
    method = argList[1]


    queue = Queue(problem.agentState)
    # problem.getNextState()
    notSolved = True

    
    while notSolved:
        # if agent is at goal state
        if problem.agentState in problem.posGoals:
            print("Great! Resolved.")
            notSolved = False
            break
        # add candidate states into queue
        for candidate in problem.getNextState():
            if candidate not in queue.nodesToExplore and candidate not in queue.nodesExplored:
                queue.nodesToExplore.append(candidate)
        # get next state from nodesToExplore, set it as agent new state
        # pop the new state from nodes to be explored
        problem.agentState = queue.nodesToExplore.pop(0)
        # add the new state into nodesExplore
        queue.nodesExplored.append(problem.agentState)
        problem.renderMap(problem.agentState)
        print("-----------------------------")
        print(len(queue.nodesExplored), '\t', len(queue.nodesToExplore))

        

if __name__ == '__main__':
    main(sys.argv[1:])
   