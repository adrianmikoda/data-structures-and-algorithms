# implementation of stack and queue data structures using linked lists
# implementation of queue using 2 stacks


class Node():
    def __init__(self, value=None):
        self.next = None
        self.val = value

class Stack():
    def __init__(self):
        self.top = None

    def empty(self):
        return self.top is None
    
    def append(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.empty():
            temp = self.top.val
            self.top = self.top.next
            return temp
    
    def print(self):
        p = self.top
        answer = []
        while p is not None:
            answer.append(p.val)
            p = p.next
        print(answer)

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def empty(self):
        return self.front is None
    
    def append(self, value):
        new_value = Node(value)
        if self.empty():
            self.front = new_value
            self.rear = self.front
        else:
            self.rear.next = new_value
            self.rear = self.rear.next

    def pop(self):
        if not self.empty():
            temp = self.front.val
            self.front = self.front.next
            return temp

    def print(self):
        p = self.front
        answer = []
        while p is not None:
            answer.append(p.val)
            p = p.next
        print(answer)

class QueueFromStacks():
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()

    def empty(self):
        return self.input_stack.empty() and self.output_stack.empty()
    
    def transform(self):
        while not self.input_stack.empty():
            self.output_stack.append(self.input_stack.pop())

    def append(self, value):
        self.input_stack.append(value)

    def pop(self):
        if not self.empty():
            if self.output_stack.empty():
                self.transform()
            return self.output_stack.pop()
            
    def print(self):
        self.input_stack.print()
        self.output_stack.print()
