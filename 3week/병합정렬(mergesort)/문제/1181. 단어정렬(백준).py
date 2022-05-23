#파이썬의 sort() 함수는 오름차순으로 정렬해주는 함수

# 풀이1)
arr = []
for _ in range(int(input())):
     arr.append(input())

set_word = list(set(arr))
set_word.sort()
set_word.sort(key=len) #(key=lambda x: len(x))
print(set_word)

#sys 기존 input()보다 10배는 빠르다.
import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    # sys.stdin.readline()은'\n\'을 포함하는 입력이기 때문에 연속으로 값을 입력받는 for문에서 에러가 발생
    # 따라서 .strip()입력
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)

