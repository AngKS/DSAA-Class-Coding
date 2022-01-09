class Stack:
    def __init__(self):
        self.__list = []

    def isEmpty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def clear(self):
        self.__list.clear()

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()

    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]

    def __str__(self):
        output = '<'
        for i in range(len(self.__list)):
            item = self.__list[i]
            # condition used to avoid printing the last comma
            if i < len(self.__list)-1:
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += '>'
        return output

# Lab task 03


class Stack2:
    def __init__(self):
        self.__list = []

    def isEmpty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def clear(self):
        self.__list.clear()

    def push(self, item):
        self.__list.insert(0, item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop(0)

    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[0]

    def __str__(self):
        output = '<'
        for i in range(len(self.__list)):
            item = self.__list[i]
            # condition used to avoid printing the last comma
            if i < len(self.__list)-1:
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += '>'
        return output


class Stack3(Stack):
    '''This is my self documentation'''
    def __init__(self, item):
        self._list = []  # private attribute

    def getItems(self):
        return self._list


s = Stack()
print(s.pop())
for i in range(1, 6):
    s.push(i)
print('Content of stack =', s)
print('Item at top=', s.get())
print('Size=', s.size())
while not s.isEmpty():
    print(s.pop())
    print(s)
