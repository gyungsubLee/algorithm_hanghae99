class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None

        value = self.front.value
        self.front = self.front.next
        return value

    def peek(self):
        if not self.front:
            return None
        return self.front.value

    def is_empty(self):
        if not self.front:
            return True
        return False
    