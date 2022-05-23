import sys
input = sys.stdin.readline

n = int(input())
coordinate_list = []

for i in range(n):
    coordinate_list.append(list(map(int, input().split())))
# sorted_coordinate = sorted(coordinate_list, key=lambda x:(x[0], x[1]))
#     -> 오름차순만 쓰기 때문에 sort()만 써도 됨.

coordinate_list.sort()
for i in range(n):
    print(coordinate_list[i][0], coordinate_list[i][1])

#다른 사람 풀이
import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[0], x[1]))
for i in so:
    print(i[0], i[1])