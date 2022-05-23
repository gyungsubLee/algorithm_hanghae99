# 큐 란?
# 한쪽 끝으로 자료를 넣고, 반대쪽에서는 자료를 뺄 수 있는 선형구조

# 큐 형태
def test_queue():
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() is None
    assert queue.is_empty()

# 큐 구현
class Node:
    def __init__(self, item, next):
        self.item = item
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

        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None


# 큐 리스트 구현
class QueueByArray:
    def __init__(self):
            self.queue = []

    # 추가
    def push(self, value):
        self.queue.push(value)

    # 삭제
    def pop(self):
        # 큐 안에 데이터가 없을 때의 예외처리
        if not self.queue:
            return None

        # O(n)의 시간복잡도를 가진다.
        return self.queue.pop(0)

    # 조회
    def peek(self):
        return self.queue[0]

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
# 문제)카드2
# 큐 -> 파이썬에서 내장함수 deque를 사용

# Deque 객체의 내장 메소드
# append: 오른쪽 추가, appendleft:왼쪽 추가
# pop:오른쪽 제거, popleft: 왼쪽 제거
# 참조)https://docs.python.org/3/library/collections.html?







