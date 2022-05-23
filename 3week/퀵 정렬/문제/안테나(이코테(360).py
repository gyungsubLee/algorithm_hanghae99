import sys

input = sys.stdin.readline

n =int(input())
arr = sorted(list(map(int, input().split())))

print(arr[(n-1)//2]) # 중강 값일 때, 최솟값을 가진다. (짝수는 중복된 2개 값의 거리합은 같다.)



