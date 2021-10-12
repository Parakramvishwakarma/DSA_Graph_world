from DSA import *
from numpy import array
from DSAGraph import *
from DSAGraphVertex import *
from DSALinkedList import *
from DSAListNode import *
class fileIO():
    def __init__(self, fileName):
        self.fileName = fileName
    def fileReader(self):
        with open(self.fileName, "r") as fileobj:
            data = fileobj.readlines()
            list1 = []
            for i in range(0, len(data)):
                sublist = (data[i].split(" "))
                empty = []
                for i in sublist:
                    j = i.strip()
                    empty.append(j)
                list1.append(empty)
        return list1
    def numEdges(self):
        edges = self.fileReader()
        return len(edges)
    def createGraph(self):
        graph = DSAGraph()
        list_edges = self.fileReader()
        for i in list_edges:
            for j in [0,1]:
                if graph.hasVertex(i[j]) == False:
                    graph.addVertex(i[j])
            graph.addEdge(i[0], i[1])
        return graph
    def display(self):
        graph = self.createGraph()
        numV = graph.getVertexCount()
        arrray = np.zeros((numV, numV), dtype = str)
        j =0
        for i in graph._vertices:
            label = i._label
            adj = i.getAdjacent()
            while len(adj)< numV -1:
                adj.append(" ")
            arrray[j][0] = label
            arrray[j][1:numV] = adj
            j += 1
        print(arrray)
        

def main():
    a = fileIO("prac6_2.al")
    a.fileReader()
    a.createGraph()
    a.display()
main()
    

    