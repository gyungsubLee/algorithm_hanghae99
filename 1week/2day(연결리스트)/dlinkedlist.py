class DoubleLinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        if not self.head:
            self.head = Node(value, None, None)
            self.tail = self.head
            return

        node = Node(value, self.tail, None)
        prevNode = self.tail
        prevNode.next = node
        self.tail = node

    def pop(self):
        if not self.tail:
            return

        node = self.tail
        prevNode = node.prev
        self.tail = prevNode
        prevNode.next = None
        return node.value

    def insert(self, index, value):
        node = Node(value, None, None)
        if not self.tail:
            self.head = node
            self.tail = node
            return

        if index == 0:
            nextNode = self.head
            node.next = nextNode
            nextNode.prev = node
            self.head = node
            return

        curnode = self.head.next
        nodeIndex = 1
        while curnode:
            if index == nodeIndex:
                prevNode = curnode.prev

                node.next = curnode
                node.prev = prevNode

                prevNode.next = node
                curnode.prev = node
                return
            curnode = curnode.next
            nodeIndex += 1

    def remove(self, value):
        if not self.tail:
            return None
        if self.head.value == value:
            nextNode = self.head.next
            nextNode.prev = None
            self.head = nextNode
            return

        curNode = self.tail
        while curNode:
            if curNode.value == value:
                prevNode = curNode.prev
                nextNode = curNode.next
                prevNode.next = nextNode
                nextNode.prev = prevNode
                curNode = None
                return
            curNode = curNode.prev
