import numpy as np
from DSALinkedList import *
class Vertex():
    def __init__(self, label, type1, penalty):
        self._label = label
        self._vertex_list = LinkedList()
        self.type1 = type1
        """if self.type == "-":
            penalty = 0
        elif self.type == "F":
            penalty = -1
        elif self.type == "D":
            penalty = 100
        elif self.type == "T":
            penalty = 1
        else: 
            raise ValueError("Invalid type of Graph node" + str(self.type))
        """
        self.penalty = penalty
        self._visited = False
    def getLabel(self):
        return self.label
    def getValue(self):
        return self.value
    def getAdjacent(self):
        llist =  self._vertex_list
        list = []
        for i in llist:
            list.append(i[0])
        return list
    def getAdjacentWeight(self):
        llist =  self._vertex_list
        list = []
        for i in llist:
            list.append(i[1])
        return list
    def getBoth(self):
        llist =  self._vertex_list
        list = []
        for i in llist:
            list.append(i)
        return list 
    def addEdge(self, label, weight):
        if label not in self.getAdjacent():
            listAdjVertex = [label, weight]
            self._vertex_list.insertLast(listAdjVertex)
    def setVisited(self):
        self._visited = True
    def clearVisited(self):
        self._visited = False
    def getVisited(self):
        return self._visited
    def __str__(self) -> str:
        list= self.getAdjacent()
        return ("Label: " + self._label + ", Links: " + str(list)) 
    
def main():
    a = Vertex('a', "-")
    a.addEdge('b', 10)
    print(a)
    print(a.getBoth())

if __name__ == "__main__":
    main()
    