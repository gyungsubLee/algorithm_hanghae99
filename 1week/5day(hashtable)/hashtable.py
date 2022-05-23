"""
-해시테이블(해시맵)
키를 값에 매핑할 수 있는 구조
연관 배열 추상 자료형(ADT)를 구현하는 자료구조이다.

헤시 테이블의 가장 큰 특징은 대부분의 연산이 분할 상환 분석에 따른 시간 복잡도가 O(1)이라는 점이다.
덕분에 데이터 양에 관계 없이 빠른 성늘을 기대할 수 있다는 장점이 있다.

-해시 함수
임의 크기의 데이터를 고정 크기 값으로 매핑하는데 사용할 수 있는 함수
해시 테이블의 핵심은 해시 함수이다. 
여기서 입력값은 ABC, 1234BC, AF32B 로 각각 3글자, 6글자, 5글자이지만,
화살표로 표시한 해시 함수를 통과하면 2바이트의 고정 크기 값으로 매핑된다.

ABC -> A1
1324BC -> CB
AF32B -> D5

이러한 해쉬 함수를 사용하는 것을 '해싱'이라 하며
해싱은 정보를 가능한 빠르게 저장하고 검색하기 위해 사용하는 중요한 기법 중 하나다.

해싱은 최적의 검색이 필요한 분야에 사용되며, 심볼 데이터 등의 자료 구조를 구현하기에도 적합하다.


@@모듈러 연산 (잘 이해 안됨)@@
h(x) = x mod m
 h(x): 입력값 x의 해시 함수를 통해 생성된 결과
 m: 해시 테이블의 크기, 일반적으로 2의 제곱수에 가깝지 않는 소수를 선택한다
 -> 매우 단순한 방법이지만, 실무에서는 이미 많은 키 세트가 충분히 랜덤한 상태고, 실제로 잘 동작한다.
"""
import collections

"""
-성능이 좋은 해쉬 함수
 해쉬 함수 값의 충돌의 최소화
 쉽고 빠른 연산
 해시 테이블 전체에 해시 값이 균일하게 분포
 사용할 키의 모든 정보를 이용하여 해싱
 해시 테이블 사용 효율이 높을 것
"""

"""
- 로드 팩터(load Factor)
해시 테이블에 저장된 데이터의 개수 n을 버킷의 개수 k로 나눈 것이다.

load factor = n/k

로드 팩터 비율에 따라 해시 함수를 재작성해야 될지 또는 해시 테이블의 크기를 조정해야 할 지를 결정한다.
자바10에서는 해시맵의 디폴트 로드 팰터를 0.75로 정했으며 '시간과 공간 비용의 적잘한 절충안'이라고 얘기한다.

일반적으로 로드 팩터가 증가할 수록 해시 테이블 서응은 점점 감소하게 된다.
why)
자바10의 경우 0.75를 넘어설 경우 동적 배열처럼 해시 테이블의 공간을 재할당한다.
"""

"""
- 충돌 시 대처: 2가지

#개별 체이닝
충돌 발생 시 연결리스트로 연결한다.
1. 키의 해시 값 계산
2. 해시 값을 이용한 배열의 인덱스 구성
3. 같은 인덱스가 있다면 연결 리스트로 연결
-> 잘 구현한다면 대부분의 탐색은 O(1)이지만, 최악의 경우, 즉 모든 해시 충돌이 발생했다고 가정할 경우에는 O(n)이 된다.

#오픈 어드레싱
충돌 발생 시 탐사를 통해 빈 공간을 찾아나서는 방식
"""

# 해쉬테이블(Hash Table)
# F(key) -> Hashcode -> index -> value

# 해쉬맵 디자인
class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후  종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결리스트 처리
        p = self.table[index]
        while p:
            # 이미 존재하는 경우 업데이트하고 빠져나간다.
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return

        #노드가 존재할 때까지 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        #연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

# 문제1 생일)

def test_hashtable():
    ht = MyHashMap()

    ht.put(1, 1)
    ht.put(2, 2)
    assert ht.get(1) == 1
    assert ht.get(3) == -1

    ht.put(2, 1)
    assert ht.get(2) == 1

    ht.remove(2)
    assert ht.get(2) == -1

def test_birthday_problem():
    import random
    TRIALS = 100000
    same_birthdays = 0

    # 10만 번 실행 진행
    for _ in range(TRIALS):
        birthdays = []
        # 23명이 모였을 때, 생일이 같을 경우 same_birthdays +=1
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)

    print(f"{same_birthdays / TRIALS * 100}%")

if __name__ == "__main__":
    test_birthday_problem()
    test_hashtable()



"""
참조 영상)https://www.youtube.com/watch?v=xls6jEZNA7Y
        https://www.youtube.com/watch?v=Vi0hauJemxA&t=312s

데이터 충돌

풀이1)
개별 체이닝(연결리스트)
같은 데이터끼리 같은 인덱스에 할당하고 개수를 파악하여 빈도수를 선별
-> 시간복잡도, 공간복잡도가 효율적이지 않음.
    why) 같은 key(data)를 해쉬 code로 변환 후 같은 인덱스에 연결리스트로 추가한다. 
         -> 연결리스트 조회: 시간복잡도O(n), 
풀이2)
데이터를 다른 버킷 자리에 넣는다. (linear Pribibg

문제) Resizing: 테이블이 할당된 공간(버킷)을 다 써 element들이 들어갈 자리가 없기 때문에
               테이블의 크기를 늘려준 다음 기존의 데이터를 다시 해시함수에 보내버리고 다시 받아와 정렬을 하는 것을 말한다.
                -> 시간복잡도 증가.

1. key의 개수 만큼의 value의 배열(버킷) 생성
2. 
"""
     