from DSAGraph import *
import numpy as np
from DSAGraphVertex import *
from DSA import *
from DSALinkedList import *
from DSAListNode import *
import sys
def usage():
    print("The program uses command line arguments, run python3 game.py with -i for an interactive mode. \n Use -s for the simulation with the file gameofcatz.txt ")

def simRead():
    with open("gameofcatz.txt", "r") as dataFile:
        data = dataFile.readlines()
        for i in range(0, len(data)):
            data[i] = data[i].split(" ")
            for j in range(0,len(data[i])):
                data[i][j] = data[i][j].strip()
        return data

def makeSpec():
    list_big = simRead()
    list_type = []
    list_penalty = []
    number_Ncode = 0
    for i in list_big:
        if i[0] == "Ncode":
            number_Ncode += 1
    array_type = np.zeros((number_Ncode,1), dtype =object)
    array_penalty = np.zeros((number_Ncode,1), dtype =object)
    j = 0
    for i in list_big:
        if i[0] == "Ncode":
            array_type[j][0] = i[1]
            array_penalty[j][0]= int(i[2])
            j+= 1
    specs = np.array ((array_type, array_penalty), dtype= object)
    return specs   # this code creates an array for a specifications of type and penalty associated with the node this will help in creatinf the nonodes

class world():
    def __init__(self, listData, specs):
        self.graph = DSAGraph()
        self.listbig = listData
        self.specs = specs
    def addVertices(self):
        for i in self.listbig:
            if i[0] == "Node":
                label = i[1]
                type1 = i[2]
                j = 0
                for i in self.specs[:][0]:
                    if i[0] == type1:
                        index = j
                    j += 1
                penalty = self.specs[1][index][0] # to get the integer out of the array
                self.graph.addVertex(label,type1, penalty)
    def addEdges(self):
        list_type = []
        list_weight = []
        for i in self.listbig:
            if i[0] == "Ecode":
                list_type.append(i[1])
                list_weight.append(int(i[2]))
        specs_edges = np.array((list_type, list_weight), dtype = object)
        for i in self.listbig:
            if i[0] == "Edge":
                vertex1 = i[1]
                vertex2 = i[2]
                type = i[3]
                ind = list(specs_edges[:][0]).index(type)
                weight = specs_edges[1][ind]
                self.graph.addEdge(vertex1, vertex2, weight)
    def allPaths(self):
        for i in self.listbig:
            if i[0] == "Start":
                start = i[1]
            if i[0] == "Target":
                target = i[1]
        self.graph.rankPaths(start,target)
    
def siMain():
    list_big = simRead()
    specs = makeSpec()
    graph = world(list_big, specs)
    graph.addVertices()
    graph.addEdges()
    graph.graph.displayWorld()
    print(graph.graph.displayAdjacencyWeight())
    graph.allPaths()
    
def main():

    if len(sys.argv) != 2:
        usage()
    else:
        if sys.argv[1] == "-s":
            print("RUNNING SIMULATION FROM THE FILE GAMEOFCATZ.TXT")
            siMain()
        elif sys.argv[1] == "-i":
            raise NotImplementedError
        else:
            usage()
    
if __name__ == "__main__":
    main()