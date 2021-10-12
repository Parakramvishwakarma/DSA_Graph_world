from DSA import *
from DSALinkedList import *
from DSAListNode import *
from DSAGraphVertex import *
from OBJpath import Path
import numpy as np

class DSAGraph():
    def __init__(self):
        self._vertices = LinkedList()
    def addVertex(self, label, type1, penalty):  
        vertice = Vertex(label, type1, penalty)           #the label input to this should be a graphvertex object tehrefore the value ofthe list node will be the graph vertex pbject 
        self._vertices.insertLast(vertice)
    def addEdge(self, label1, label2, weight):  #theese are both the graoph vertex objects
        vertice1 = self.getObject(label1)
        vertice2 = self.getObject(label2)
        vertice1.addEdge(label2, weight)
    def _hasVertexRec(self,label, curNode): #we are going to search for that object in my linked list
        if curNode == None:
            return False
        if curNode.value._label == label:
            ans = True
        else:
            ans = self._hasVertexRec(label, curNode.next)
        return ans
    def hasVertex(self, label):
        return self._hasVertexRec(label,self._vertices.head)
    def getVertexCount(self):
        count = 0
        for i in self._vertices:
            count += 1
        return count
    def getEdgeCount(self):
        length = 0
        for i in self._vertices:
            length = length + len(i.getAdjacent())
        edges = length/2
        return edges
    def isAdjacent(self, label1, label2):
        if self.hasVertex(label1) == False or self.hasVertex(label2) == False:
            return ValueError("vetice doestn exist in the graph")
        else:
            for i in self._vertices:
                if i._label == label1:
                    vertice1 = i
            list = vertice1.getAdjacent()
            if label2 not in list:
                ans = False
            else:
                ans = True
            return ans
    def getBoth(self, label):
        vertex = self.getObject(label)
        return vertex.getBoth()
    def getAdjacentWeight(self, label):
        vertex = self.getObject(label)
        return vertex.getAdjacentWeight()
    def getAdjacent(self, label):
        if self.hasVertex(label) == False:
            return ValueError("vetice doestn exist in the graph")
        else:
            for i in self._vertices:
                if i._label == label:
                    vertice = i
                    return vertice.getAdjacent()
    def displayAdjacencyWeight(self):
        numV = self.getVertexCount()
        array = np.zeros((numV+1, numV+1), dtype = object)
        j = 0
        for i in self._vertices:
            j += 1
            array[j][0] = i._label
            array[0][j]= i._label
        list1 = list(array[0][1:numV+1])
        for i in range(0,len(list1)):
            vertex = self.getObject(list1[i])
            list_both = vertex.getBoth()
            for j in list_both:
                index = list1.index(j[0])
                array[i+1][index+1] = str(j[1])
        for i in array:
            for j in range(0,len(i)):
                if i[j] == 0:
                    i[j] = ' '
        return array
    def displayList(self):
        numV = self.getVertexCount()
        array = np.zeros((numV,numV), dtype= str)
        j = -1
        for i in self._vertices:
            j += 1
            label = i._label
            adj = i.getAdjacent()
            while len(adj) < numV-1:
                adj.append(" ")
            array[j][0] = label
            array[j][1:numV]= adj
        return array
    def getObject(self, label):
        for i in self._vertices:
            if i._label ==label:
                vartice = i
                return vartice
    def sortOBJ(self, list_obj):
        for j in range(0, len(list_obj)):
            for i in range(0,len(list_obj)-1):
                sort = False
                while sort == False:
                    if list_obj[i]._label > list_obj[i+1]._label:
                        dummy = list_obj[i+1]
                        list_obj[i+1] = list_obj[i]
                        list_obj[i] = dummy
                    else:
                        sort = True
        return list_obj
    def depth(self):
        old = set()
        t= set()
        new = []
        queue = shuffleQueue()
        for i in self._vertices:
            new.append(i)
        new = self.sortOBJ(new)
        for i in new:
            queue.enqueue(i) 
        stack = DSAStack(len(new))
        v = queue.dequeue()
        stack.push(v)
        while stack.isFull() == False:
            old.add(v)
            listADJ = v.getAdjacent()
            object_listADJ = []
            for i in listADJ:
                object = self.getObject(i)
                object_listADJ.append(object)
                if object not in old:
                  t.add("("+ v._label +"," +i + ")")
            object_listADJ = self.sortOBJ(object_listADJ)
            i = 0
            while i < len(object_listADJ):
                if object_listADJ[i] not in old:
                    adj = object_listADJ[i]
                    i = len(object_listADJ)
                else:
                    adj = None
                i+=1
            if adj == None:
                for i in new:
                    if i not in stack.stack:
                        v = i
                        stack.push(i)
            else:
                stack.push(adj)
                v = adj
        print("final stack")
        print(stack.stack)
        print(t)
    def getAdjacentSet(self, v):
        listADJ = v.getAdjacent()
        object_listADJ = []
        for i in listADJ:
            object = self.getObject(i)
            object_listADJ.append(object) 
        list_adjacentObj = self.sortOBJ(object_listADJ)
        set_adj = set()
        for i in list_adjacentObj:
            set_adj.add(i)
        return set_adj
    def recursive_find(self, set_path):

    def BFS(self, start, finish):
        start_obj = self.getObject(start)
        target_obj = self.getObject(finish)
        old = set()
        t= set()
        new = []
        queue = shuffleQueue()
        for i in self._vertices:
            new.append(i)
        new = self.sortOBJ(new)
        v = new[0]
        old.add(v)
        queue.enqueue(v)
        while queue.isEmpty() == False:
            v = queue.dequeue()
            list_adj = self.getAdjacentSet(v)
            for object in list_adj:
                if object == target_obj:
                    
                        
                elif object not in old:
                    t.add("("+ v._label +"," +object._label + ")")
                    old.add(object)
                    queue.enqueue(object)
        print(t)
    def depthFirst(self):
        old = set()
        t= set()
        new = []
        queue = shuffleQueue()
        for i in self._vertices:
            new.append(i)
        new = self.sortOBJ(new)
        v = new[0] 
        stack= DSAStack(len(new))
        stack.push(v)
        old.add(v)
        print(v)
        while stack.isEmpty() == False:
            while self.getAdjacentSet(v).issubset(old) != True:
                for i in self.getAdjacentSet(v):
                    if i not in old:
                        w = i
                print(w)
                t.add("("+ v._label +"," +w._label + ")")
                old.add(w)
                stack.push(w)
                v = w
                print(stack.stack)
            v = stack.pop()
        print(t)
    def displayWorld(self):
        numT = 0
        num_ = 0
        numF = 0
        numD = 0
        energyBoost = 0
        penalty = 0
        for i in self._vertices:
            if i.type1 =="-":
                num_ += 1
            elif i.type1 == "D":
                numD += 1
                penalty += i.penalty
            elif i.type1 == "F":
                numF += 1
                energyBoost += i.penalty
            elif i.type1 == "T":
                numT += 1
                penalty += i.penalty
        listDisplay = "Number of dogs in the world are:" + str(numD) + "\nNumber of Toys in the world for distraction are: " + str(numT) + "\nNumber of food sources in the world are:" + str(numF) + "\nNumber of normal nodes are: " + str(num_)
        data = "Total Energy Boost available for player: " + str(energyBoost)
        data1 = "Total Penalties available for player: " + str(penalty) 
        print(listDisplay)
        print(data)
        print(data1)
    def _allPathsRec(self, start, finish, path, linked):
        start._visited = True
        path.push(start._label)
        if start == finish:
            pathOBJ = self.findLength(path)
            linked.insertFirst(pathOBJ)
        else:

            for i in start.getAdjacent():
                object_i = self.getObject(i)
                if object_i._visited == False:
                    self._allPathsRec(object_i,finish, path, linked)
        path.pop()
        start._visited = False

    def allPaths(self, start,finish):
        start = self.getObject(start) # finds object for start label
        finish = self.getObject(finish)
        for i in self._vertices:
            i._visited = False
        size = self.getVertexCount()
        path = DSAStack(size)
        linked = LinkedList()
        self._allPathsRec(start, finish, path, linked)
        return linked

    def findLength(self, path):
        total = 0
        list= []
        for i in path.stack:
            if i != 0:
                list.append(i)
        length = path.getCount()
        array_edges = np.zeros((length-1,2), dtype = object)
        for i in range(0, length-1):
            list1 = [path.stack[i], path.stack[i+1]]
            array_edges[i][0] = list1
            obj_initial = self.getObject(path.stack[i])

            for j in obj_initial.getBoth():
                if j[0] == path.stack[i+1]:
                    array_edges[i][1] = j[1]
                    total += j[1]
        for vertex in path.stack:
            if vertex != 0:
                vertex = self.getObject(vertex)
                total += vertex.penalty
        pathway = Path(list, total)
        return pathway
    def sortPaths(self, list_paths):
        listSorted = []
        while list_paths.isEmpty() == False:
            obj_path = list_paths.removeFirst()
            listSorted.append(obj_path)
            for j in range(0, len(listSorted)):
                for i in range(0,len(listSorted)-1):
                    sort = False
                    while sort == False:
                        if listSorted[i].length > listSorted[i+1].length:
                            dummy = listSorted[i+1]
                            listSorted[i+1] = listSorted[i]
                            listSorted[i] = dummy
                        else:
                            sort = True
        for i in listSorted:
            list_paths.insertLast(i)
        return list_paths
    def rankPaths(self, start, finish):
        print("PRINTING THE FASTEST PATHS FROM START TO TARGET")
        list_paths = self.allPaths(start, finish)
        listSorted = self.sortPaths(list_paths)
        for i in listSorted:
            print(i)
        return listSorted
        
        

        

    
def main():
    g = DSAGraph()
    g.addVertex("A", "-", 0)
    g.addVertex("B", "F", -1)
    g.addVertex("C", "D", 100)
    g.addVertex("D", "T", 1)
    g.addEdge("C", "A", 10)
    g.addEdge("A","C", 20)
    g.addEdge("A", "B", 10)
    g.addEdge("A", "D", 25)
    g.addEdge("C", "B", 20)
    g.addEdge("B", "D", 5)
    print(g.displayAdjacencyWeight())
    g.displayWorld()
    g.rankPaths("C", "D")


    
if __name__ == "__main__":


    main()




            


    
        







