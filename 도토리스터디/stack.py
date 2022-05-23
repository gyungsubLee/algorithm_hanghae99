# stack 연결리스 구현
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class stackByLinkedList:
    def __init__(self):
        self.top= None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if not self.top:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        if self.head:
            return False
        return True

# stackByArray
class stack(list):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False




