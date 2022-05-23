# 흐름만...
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init_(self):
        self.head = None

    def push(self, value):
        if self.head is not None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp


    def pop(self):
        if self.head is None:
            return 0

        self.head = self.head.next


    def peek(self):
        if self.head is None:
            return 0
        return self.head.data





