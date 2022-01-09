#  implement a Deque class
import random


class Deque():
    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return self.__items == []

    def addHead(self, item):
        self.__items.append(item)

    def addTail(self, item): # method name can be called: enqueue
        self.__items.insert(0, item)

    def removeHead(self): # method name can be called: dequeue
        # check if list is empty
        if self.isEmpty():
            return None
        else:
            return self.__items.pop()

    def removeTail(self):
        # check if list is empty
        if self.isEmpty():
            return None
        else:
            return self.__items.pop(0)

    def size(self):
        return len(self.__items)

    def getHead(self):
        return self.__items[-1]

    def getTail(self):
        return self.__items[0]

    def __str__(self):
        output = "<"
        # print(self.__items)
        for i in range(len(self.__items)-1, -1, -1):
            if i > 0:
                output += str(self.__items[i]) + ", "
            else:
                output += str(self.__items[i])
        output += ">"
        return output

# Test Deque
d = Deque()
print(d.removeHead())
print(d.removeTail())

for i in range(1, 6):
    d.addTail(i)

print('Content of deque is =', d)
print('Item at front =', d.getHead())
print('Item at back =', d.getTail())
print('Size:', d.size())

count = 0
while not d.isEmpty():
    # Alternate removing from head and tail
    if count % 2 == 0:
        print(d.removeHead())
    else:
        print(d.removeTail())
    print(d)
    count += 1


class Node:
    # Constructor
    def __init__(self):
        self.nextNode = None


class Temp(Node):
    def __init__(self, valCelsius):
        self.valCelsius = valCelsius
        super().__init__()

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.valCelsius == otherNode.valCelsius

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'<' not supported between instances of 'Temp' and 'NoneType'")
        return self.valCelsius < otherNode.valCelsius

    def __str__(self):
        return f'{self.valCelsius}'


class SortedList:
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insert(self, newNode):
        self.length += 1
        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return
        # Check if it is going to be new head
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return
        # Check it is going to be inserted
        # between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        # Once we reach here it must be added at the tail
        leftNode.nextNode = newNode

    def __str__(self):
        # We start at the head
        output = ""
        node = self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = f"'{node.__str__()}'"
                firstNode = False
            else:
                output += (', ' + f"'{node.__str__()}'")
            node = node.nextNode
        return output


class Fruit(Node):

    def __init__(self, fruit):
        self.fruit = fruit
        self.__wordLength = len(self.fruit)
        super().__init__()

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.__wordLength == otherNode.__wordLength

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'<' not supported between instances of 'Fruit' and 'NoneType'")
        return self.__wordLength < otherNode.__wordLength

    def __str__(self):
        return f'{self.fruit}'


l = SortedList()
fruits = ['Cherry', 'Apricot', 'lime', 'Blueberry', 'Apple']
print(fruits)
for fruit in fruits:
    l.insert(Fruit(fruit))
print(l)
