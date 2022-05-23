# 다중할당? -> 파이썬 특유의 문법, 이 문제의 경우 다중 할당이 아닐 시 오류가 난다고 하는데...?
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val, None)



def insertionSortList(head):
    cur = parent = ListNode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        cur = parent
    return cur.next

t = [4, 2, 1, 3]
l1 = LinkedList()
for e in t:
    l1.append(e)
insertionSortList(l1)


