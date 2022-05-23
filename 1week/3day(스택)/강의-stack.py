# stack
# 스택은 FILO(First in Last out) 구조의 자료형이다.
# 데이터를 저장하는 공간, 스택의 top를 가리키는 변수나 포인터 필요(항상 top을 출력하기 때문)
"""
-스택의 활용
웹브라우저 뒤로가기 버튼
DFS(깊이 우선 탐색)
후위 연산자의 연산(즉, 계산기)
 . . .

 -스택을 구현하는 다양한 방법 존재
 속도가 중요한 알고림즘의 경우 상황에 맞추어 구현한다.
"""

def test_stack():
    stack = stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()

# keyword: push, pop, is_empty

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)
        """ case1) -> 새로운 Node가 기존의 Node의 next에 할당 된다. 
        (초기화: 변수는 선인 시 처음에는 값이 정해지지 않은 상태이다. 이 상태에서 최초로 값을 저장하는 행위를 변수를 초기화한다 라고 표현함.) 
        Node 1개, self.top = {item:val1, next:self.top}
        Node 2개, self.top = {item:val1, next:{item:val2, next:self.top}}
        Node 3개, self.top = {item:val1, next:{item:val2, next:{item:val3, next:self.top}}}
          의문점) stack은 선입후출(first in last out) 구조인데 밑에 pop을 보면 먼저 넣은 Node를 가져온다.
           ->queue의 형태, 위의 객체 형태는 맞는데... 뭐지? 구조가 잘못된건가?
            재귀 호출과 유사? 
        """

        """ case2) -> 새로운 Node의 next에 이전 Node를 할당시킨다. 
           => 논리 구조상 이게 맞음. 근데 왜 그런거지?
                   
        Node.self.top은 이전에 만들어진 self.top을 말함. ?? 아직도 명확하지 않음
        ->
        Node 1개, self.top = {item:val1, next:self.top}
        Node 2개, self.top = {item:val2, next:{item:val1, next:self.top}}
        Node 3개, self.top = {item:val3, next:{item:val2, next:{item:val1, next:self.top}}}
        """

    def pop(self):
        if self.top is None:
            return None
        # self.top을 node에 넣어 item(value)를 가져온다.
        node = self.top
        self.top = self.top.next
        return node.item
        """ 1)
        self.top = {item:val1, next:{item:val2, next:{item:val3, next:self.top}}}
        --------------------
        pop() 실행 시
        --------------------
        self.top = {item:val2, next:{item:val3, next:self.top}}
        node.item = self.top.item = val1을 가져온다.
        의문점) self.top.next.next.next = val3을 가져와야한다.. 구조가 잘못된 듯?
        """

        """ 2)
        -> push 시 생성되는 구조 잘못 (논리상 이게 맞음, 이유는 아직도 의문...)
        
        self.top = {item:val3, next:{item:val2, next:{item:val1, next:self.top}}}
        --------------------
        pop() 실행 시
        -------------------- 
        self.top = {item2:val2, next:{item:val1, next:self.top}}
        node.item = val3       
        """
        # => 함수의 선언, 초기화, 할당에 대한 개념 부족
        # self.top = Node(value, self.top) 앞에 self.top 메모리에 새로 선언하는 것이고 뒤에 self.top은 이미 참조된 self.top 을 가르킨다.

    #왜 존재해야하지? pop에 조건으로 넣으면 안되나?
    # -> 검증이유(?)  -> 컴퓨터적인 사고를 위해 아직은 이해가 불가하지만 우선 전체 맥락을 보고 넘어가고 나중에 다시 봐라.
    def is_empty(self):
        return self.top is None


# 파이썬 list를 이용한 구현
class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def isEmpty(self):
        return not self.items  #(self.items = None ?)




stk = stack()
print(stk)
print(stk.isEmpty())
stk.push(1)
stk.push(2)

stk.pop()

print(stk)







