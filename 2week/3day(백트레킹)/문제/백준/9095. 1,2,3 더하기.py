# 문제)https://www.acmicpc.net/problem/9095

# 풀이1) DFS
import sys

read = sys.stdin.readline

def dfs(num):
    if arr[num] > 0:
        return arr[num]
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        arr[num] = dfs(num - 1) + dfs(num - 2) + dfs(num - 3)
        return arr[num]

T = int(sys.stdin.readline())
for _ in range(T):
    l = int(read())
    arr = [0] * (l + 1)
    print(dfs(l))


# 풀이1-2)
input = sys.stdin.readline
T = int(input())
memo = {1:1, 2:2, 3:4}
def rep(n):
    if memo.get(n):
        return memo[n]
    memo[n] =  rep(n-3) + rep(n-2) + rep(n-1)
    return memo[n]
for _ in range(T):
    n = int(input())
    print(rep(n))



# 풀이2) 동저계획법
"""
규칙성을 찾아낸 뒤 DP를 이용하여 풀이하는 문제이다.
우선 숫자가 작은 경우 직접 개수를 세 규칙성을 찾는다.

1일 때 ->  1
2일 때 ->  2
3일 때 ->  4
4일 때 ->  7
5일 때 ->  13

이에 따라 점화식은   f(n) = f(n-1) + f(n-2) + f(n-3)  (n>3 인 경우)
"""

def sums(n):
    if n == 1:
        return (1)
    elif n == 2:
        return (2)
    elif n == 3:
        return (4)
    else:
        return sums(n - 1) + sums(n - 2) + sums(n - 3)  # 규칙을 찾아내는게 중요!


for i in range(n):
    a = int(input())
    print(sums(a))