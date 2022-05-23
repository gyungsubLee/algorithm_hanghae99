
arr = []
for i in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])


#다른사람 풀이2)
data = []
for i in range(int(input())):
	x, y = map(int,input().split())
	data.append((x,y))

data.sort(key = lambda x : (x[1], x[0]))

for d in data:
	print(d[0], d[1])

# # 다른사람 풀이3)
import sys

input = sys.stdin.readline()

N = int(input())

arr = [] #2차원리스트
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([y, x]) #y 우선 정렬

arr.sort()

for y, x in arr:
    print(x, y)



