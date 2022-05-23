import collections
from typing import *

# 풀이1) 리스트 변형 -> 비교
# linkedlist -> list
# if문으로 앞뒤 문자 비교
from typing import List

class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def inpalindrome(self, head: Optional[ListNode]) -> bool:
    # array형태가 물리메모리가 연결되어있어 데이터를 찾는데 유용하다.
    # 따라서 linkedlist -> list
    lst : List = []
    while True:
        lst.append(head.val)
        if head.next == None:
           break
        head = head.next
    #[::-1] : 배열 역순으로 정렬
    return lst == lst[::-1]

l1 = []




