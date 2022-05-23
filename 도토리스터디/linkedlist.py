class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    # 헤드초기화
    def __init__(self):
        self.head = None

    # 푸쉬
    def push(self, value):
        if not self.head:
            self.head=Node(value, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value, None)

        """
        while node:
            if not node.next:
                node.next = Node(value, None)
                return
            node = node.next
        """

    # 삭제
    def pop(self):
        if not self.head:
            return 0

        node = self.head
        while node:
            if not node.next:
                value = node.value
                node = None
                return value
            node = node.next

        # while node.next:
        #     node = node.next
        # value = node.value
        # node = None
        # return value

    # 중간 넣기
    def insert(self, value, index):
        if not self.head:
            self.head = Node(value, None)
            return
        if index == 0:
            node = Node(value, self.head.next)
            self.head = node
            return
        curIndex = 1
        prevNode = self.head
        node = self.head.next
        while node:
            if curIndex == index:
                tempNode = node
                node = Node(value, tempNode)
                prevNode.next = node
                return
            prevNode = node
            node = node.next
            curIndex += 1

    # 인덱스 조회
    def index(self, value):
        if not self.head:
            return 0
        node = self.head
        curIndex = 0
        while node:
            if node.value == value:
                return print(curIndex)
            node = node.next
            curIndex += 1

    # 값보기
    def get(self, index):
        if not self.head:
            return 0
        if index == 0:
            return self.head.value

        curIndex = 1
        node = self.head.next
        while node:
            if curIndex == index:
                return print(node.value)
            node = node.next
            curIndex += 1

"""
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    # 헤드초기화
    def __init__(self):
        self.head = None

    #푸쉬
    def push(self, value):
        if not self.head:
            self.haed = Node(value, Node)

        node = self.head
        while node:
            if not node.next:
                node.next = Node(value, None)
                return

            node = node.next

    # 팝
    def pop(self):
        if not self.head:
            return 0

        node = self.head
        while node:
            if not node.next:
                value = node.value
                node = None
                return value

            node = node.next

    # 중간 넣기
    def insert(self, value, index):
        if not self.head:
            self.haed = Node(value, None)
            return
        # node가 1개일 때, index = 0이라 표현
        # 어떻게 index로 구분을 하지?
        #  -> 구분을 위해 임의로 정해 놓은 것.
        if index == 0:
            node = Node(value, self.head.next)
            self.head = node
            return
        curIndex = 1
        prevNode = self.head
        node = self.head.next
        while node:
            if curIndex == index:
                tempNode = node
                node = Node(value, tempNode)
                prevNode.next = node
                return
            prevNode
            node = node.next
            curIndex += 1


    # 중간 빼기
    def remove(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return

        curIndex = 1
        prevNode = self.head
        node = self.head.next
        while node:
            if curIndex == index:
                prevNode == index # 뭐지?
                prevNode.next = node.next
                return
            prevNode = node
            node = node.next
            curIndex += 1

    # 인덱스 조회
    def index(self, value):
        if not self.head:
            return 0
        node = self.head
        curIndex = 0
        while node:
            if node.value == value:
                return print(curIndex)
            node = node.next
            curIndex += 1

    # 값보기
    def get(self, index):
        if not self.head:
            return 0
        if index == 0:
            return self.head.value

        curIndex = 1
        node = self.head.next
        while node:
            if curIndex == index:
                return print(node.value)
            node = node.next
            curIndex += 1

"""



