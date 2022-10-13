# Jacob Hardman
# CS 301
# Dr. Nathaniel Miller
# 2/10/2021

class Stack:
    # This method should have a constant runtime of O(1)
    def __init__(self):
        self.items = []

    # This method should have a linear runtime of O(n)
    def __str__(self):
        return str(self.items)

    # This method should have a constant runtime of O(1)
    def push(self, item):
        self.items.append(item)

    # This method should have a constant runtome of O(1)
    def pop(self):
        return self.items.pop()

    # This method should have a constant runtime of O(1)
    def peek(self):
        return self.items[len(self.items) - 1]

    # This method should have a constant runtime of O(1)
    def isEmpty(self):
        return self.items == []

    #This methoud should have a constant runtime of O(1)
    def size(self):
        return len(self.items)

class Queue:
    # This method should have a constant runtime of O(1)
    def __init__(self):
        self.items = []

    # This method should have a linear runtime of O(n)
    def __str__(self):
        return str(self.items)

    # This method should have a constant runtime of O(1)
    def enqueue(self, item):
        self.items.append(item)
    
    # This method should have a linear runtime of O(n)
    def dequeue(self):
        return self.items.pop(0)

    # This method should have a constant runtime of O(1)
    def isEmpty(self):
        return self.items == []

    # This method should have a constant runtime of O(1)
    def size(self):
        return len(self.items)

class Deque:
    # This method should have a constant runtime of O(1)
    def __init__(self):
        self.items = []

    # This method should have a linear runtime of O(n)
    def __str__(self):
        return str(self.items)

    # This method should have a linear runtime of O(n)
    def addFront(self, item):
        self.items.insert(0, item)

    # This method should have a constant runtime of O(1)
    def addRear(self, item):
        self.items.append(item)

    # This method should have a linear runtime of O(n)
    def removeFront(self):
        return self.items.pop(0)

    # This method should have a constant runtime of O(1)
    def removeRear(self):
        return self.items.pop()

    # This method should have a constant runtime of O(1)
    def isEmpty(self):
        return self.items == []

    # This method should have a constant runtime of O(1)
    def size(self):
        return len(self.items)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class Linked_List:
    def __init__(self):
        self.first_node = Node()

    def __str__(self):
        elements = []
        current_node = self.first_node
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        return str(elements)

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.first_node.next
        self.first_node.next = new_node

    def remove(self, item):
        current_node = self.first_node
        previous_node = self.first_node
        while current_node.next != None:
            previous_node = current_node
            current_node = current_node.next
            if current_node.data == item:
                previous_node.next = current_node.next
                return None
        print("Error, item not found in linked list.")
        return None

    def search(self, item):
        if self.size() == 0:
            print("ERROR, the linked list is currently empty.")
            return None
        else:
            current_node = self.first_node
            while current_node.next != None:
                current_node = current_node.next
                if current_node.data == item:
                    return True
            return False

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        size = 0
        current_node = self.first_node
        while current_node.next != None:
            size += 1
            current_node = current_node.next
        return size

    def append(self, item):
        new_node = Node(item)
        current_node = self.first_node
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def index(self, item):
        if self.size() == 0:
            print("ERROR, the linked list is currently empty.")
            return None
        else:
            index = 0
            current_node = self.first_node
            while current_node.next != None:
                current_node = current_node.next
                if current_node.data == item:
                    return index
                index += 1
            print("ERROR, item not found in linked list.")
            return None

    def insert(self, pos, item):
        if pos >= self.size() or pos < 0:
            print("ERROR, position specified is invalid.")
            return None
        else:
            current_node = self.first_node
            previous_node = self.first_node
            current_index = 0
            while current_node.next != None:
                current_node = current_node.next
                if current_index == pos:
                    new_node = Node(item)
                    previous_node.next = new_node
                    new_node.next = current_node
                    return None
                previous_node = current_node
                current_index += 1

    def pop(self, pos = None):
        if self.size() == 0:
            print("ERROR, the linked list is currently empty.")
            return None
        if pos == None:
            current_node = self.first_node
            previous_node = self.first_node
            while current_node.next != None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            return current_node.data
        else:
            current_node = self.first_node
            previous_node = self.first_node
            current_index = 0
            while current_node.next != None:
                current_node = current_node.next
                if current_index == pos:
                    break
                previous_node = current_node
                current_index += 1
            previous_node.next = current_node.next
            return current_node.data

class Doubly_Linked_List:
    def __init__(self):
        self.first_node = Node()

    def __str__(self):
        elements = []
        current_node = self.first_node
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        return str(elements)

    def add(self, item):
        new_node = Node(item)
        next_node = self.first_node.next

        new_node.next = self.first_node.next
        new_node.previous = self.first_node

        if self.size() != 0:
            next_node.previous = new_node
            
        self.first_node.next = new_node

        current_node = self.first_node
        while current_node.next != None:
            current_node = current_node.next
        self.first_node.previous = current_node

    def remove(self, item):
        current_node = self.first_node
        next_node = self.first_node.next
        while current_node.next != None:
            current_node = current_node.next
            previous_node = current_node.previous
            next_node = current_node.next
            if current_node.data == item:
                previous_node.next = current_node.next
                if next_node != None:
                    next_node.previous = previous_node
                return None
        print("Error, item not found in linked list.")
        return None

    def search(self, item):
        if self.size() == 0:
            print("ERROR, the linked list is currently empty.")
            return None
        else:
            current_node = self.first_node
            while current_node.next != None:
                current_node = current_node.next
                if current_node.data == item:
                    return True
            return False

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        size = 0
        current_node = self.first_node
        while current_node.next != None:
            size += 1
            current_node = current_node.next
        return size

    def append(self, item):
        new_node = Node(item)
        current_node = self.first_node
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        new_node.previous = current_node

    def index(self, item):
        if self.size() == 0:
            print("ERROR, the linked list is currently empty.")
            return None
        else:
            index = 0
            current_node = self.first_node
            while current_node.next != None:
                current_node = current_node.next
                if current_node.data == item:
                    return index
                index += 1
            print("ERROR, item not found in linked list.")
            return None

    def insert(self, pos, item):
        if pos >= self.size() or pos < 0:
            print("ERROR, position specified is invalid.")
            return None
        else:
            current_node = self.first_node
            current_index = 0
            while current_node.next != None:
                current_node = current_node.next
                previous_node = current_node.previous
                next_node = current_node.next
                if current_index == pos:
                    new_node = Node(item)
                    previous_node.next = new_node
                    new_node.next = current_node
                    if next_node != None:
                        next_node.previous = new_node
                    return None
                current_index += 1

    def pop(self, pos = None):
        if self.size() == 0:
            print("ERROR, the linked list is currently empty.")
            return None
        if pos == None:
            current_node = self.first_node
            while current_node.next != None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            return current_node.data
        else:
            current_node = self.first_node
            current_index = 0
            while current_node.next != None:
                current_node = current_node.next
                previous_node = current_node.previous
                next_node = current_node.next
                if current_index == pos:
                    break
                current_index += 1
            previous_node.next = current_node.next
            if next_node != None:
                next_node.previous = previous_node
            return current_node.data

##########################################################

# QUESTIONS:

# 1. Based on my observations, I believe that python's internal implementation of a list is a different entity than a linked list or doubly linked list.
# Python's own lists are inherently ordered, while I did build a sort of order into the linked and doubly linked list, they function different in practice than a 
# regular lst does. For instance, with a regular python list, appending an item to the end of a list is a constant runtime operation. This is not true with linked
# or doubly linked lists due to their inherent complexity. So while Python lists do exhibit similar traits as doubly or singly linked lists, I would have to say
# that it is neither of these data types.

# 2. For stacks, I would expect a standard Python list to give the best running time as they are nearly identical in function. 
# For queues, I would expect a linked list to work best as the linked list already contains links between items that we would need to calculate with a standard list. 
# For deques, I would expect a doubly linked list to give the best running time as it contains links between nodes going backwards and forwards, which would be useful 
# for a deque when we are manipulating both the beginning and the end of the deque.

##########################################################

def testing():
    #Test code here
    print("Testing...")

testing()