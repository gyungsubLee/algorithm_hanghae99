# 영상 설명 참조) https://www.youtube.com/watch?v=DEXpIZpfqiQ&t=82s
# 코드 참조)https://velog.io/@minjung-s/circular-queue
"""
동작하는 원리는 투 포인터와 비슷하다.
 enQueue()하여 요소를 삭제할 자리, deQueue하여 요소를 추가할 자리를 따로 저장한다.
 nQueue()를 하게 되면 rear 포인터가 앞으로 이동하고, deQueue()를 하게 되면 front포인터가 앞으로 이동한다.
 이렇게 enQueue와 deQueue를 반복하게 되면 서로 동그랗게 연결되어 있기 때문에 투 포인터가 빙글빙글 돌면서 이동하는 구조가 된다.
 만약 rear 포인터와 front 포인터가 같은 위치를 가르키게 된다면 여유공간이 없는 상황으로 공간 부족 에러를 발생시킨다.
"""

class CircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    # enQueue(): rear 포인터 이동
    def enQueue(self, value: int):
        if self.q[self.p2] is None:
            self.q[self.p2] = value #rear이 가르키는 자리에 value삽입
            self.p2 = (self.p2 + 1) % self.maxlen # 다음 자리로 p2포인터 이동. 최대 길이가 넘어가면 나머지 값으로 자리를 갖는다.
            return True
        else:
            return False

    # deQueue: front 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False #이미 내보낼 것이 없는 상태 -> False
        else:
            self.q[self.p1] = None # 삭제
            self.q1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        # p1이 가르키는 맨앞의 요소 반환
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        #맨 뒤의 요소를 반환(p2는 이미 뒤에 삽입될 자리를 가르키고 있기 때문에 p2-1dl 맨 뒤의 요소를 가르킨다.
        return -1 if self.q[self.p2 -1] is None else self.q[self.p2 -1]

    def isEmpty(self) -> bool:
        # p1, p2가 가르키는 자리가 같고, 그 안의 요소가 존재하지 않는다면 큐는 비어있습니다.
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isfull(self) -> bool:
        # p1, p2가 가르키는 자리가 같고, 그 안의 요소가 존재하면 공간이 다 찬 것이다.
        return self.p1 == self.p2 and self.q[self.p1] is not None