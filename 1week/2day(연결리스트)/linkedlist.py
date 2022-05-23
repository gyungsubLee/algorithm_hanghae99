# 자료구조
# 특정 알고리즘 문제를 풀때, 이미 효율적으로 해결할 수 있는 자료구조가 있다.

# 주제) 연결리스트

# Array vs Linked list
# Array는 중간값 삽입 시 물리메모리에 저장된 데이터를 다 뒤로 수정 후 빈 메모리 공간에 데이터를 넣는다.
# linked list는 물리적으로 연결되어있지 않기 때문에 데이터를 삽입하고자 하는 위치만 찾고 넣는다.

# __init__: initiating(시작)의 약어, 정의 시 class가 호출 될떄 해당 함수(def) 반드시 실행
# -> Person이라는 함수가 호출 될때,  self.name = name 반드시 실행된다.


# Class
# self는 파이썬이 알아서 넣어주는 parameter. 그냥 갖다 쓰면 됨.
# self 다음 두번째부터 parameter 지점.
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def sayhello(self, to):
#         print(f"hello {to}, I'm {self.name}")
#
#
# rtan = Person("rtanny")
# rtan.sayhello("hanghae")


# linkedList
# ㅣ
# 기본단위 box와 화살표 ->

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# 중간 데이터로 접근을 하기 위해, 첫번쨰 값에서 next-> next(한칸, 한칸 순서대로) 움직인다.
# 따라서 시작점을 지정해야한다. -> self.head =none
"""
1. 변수란?
프로그래밍 언어에서 '변수'란 값을 저장할 수 있는 메모리상의 공간을 의미한다.
이 공간에 저장된 값은 변
"""
class LinkedList:
    def __init__(self):
        #변수에 대한 이해도 부족
        self.head = None

    # linkedList에 node를 추가한다.
    def append(self, val):
        # head 값을 비우고 Node를 넣는다.
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        #의문점)node next = none아닌가? 왜 while문이 실행되지?
            # -> node.next가 none이면 while문 그냥 넘어간다.
        # 강의 표현: node의 next(화살표)가 있는 한 실행된다.
        while node.next:
            node = node.next
        # 새로운 노드를 next에 넣는는.
        node.next = ListNode(val, None)

lst = [1, 2, 3]
l1 = LinkedList()
for e in lst:
    l1.append(e)
#l1 =head ={1, next={2, next={3, next}}}
print(l1)


# 연결리스트 초기화
class Node:
    def __init__(self, date = 0, next = None):
        self.date = date
        self.next = next

def init_list():
    global nade_A
    #4개의 노드생성
    node_A = Node("A")
    node_B = Node("B")
    node_C = Node("C")
    node_D = Node("D")
    # 각각의 노드에 데이터 저장 후 각 노드 링크로 연결
    node_A.next = node_B.next
    node_B.next = node_C.next
    node_C.next = node_D.next

def print_list(): #node 데이터 print
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print

if __name__ == '__main__':
    print("연결 리스트 초기화 후")
    init_list()
    print_list()


