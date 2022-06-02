"""
이코테 92P

기출: 2019 국가 교육기관 코딩 테스트

큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 떄 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

Q. 순서대로 2, 4, 5, 4 ,6으로 이루어진 배열이 있을 떄 M이 8이고, K가 3이라고 가정하자.
 이 경우 특정한 인덱스의 수가 연속해서 3번 더해질 수 있으므로 큰 수의 법칙에 따른 결과 6 + 6 + 6 + 5 + 6+ 6+ 6+ 5 = 46이됨.


입력 예시

5 8 3

2 4 5 4 6

출력 예시

46


입력 조건

1. 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.

2. 둘쨰줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10,000 이하의 수로 주어진다.

3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.

출력 조건

위 문제에서 제시한 큰 수의 법칙에 따라 더해진 답을 출력한다.
"""

# 풀이1)
n, m , k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() # 입력 받은 수 정렬|(내림차순[작은수 - 큰수])
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1 

print(result)


# 풀이2)
n, m , k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() # 입력 받은 수 정렬|(내림차순[작은수 - 큰수])
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째 큰 수 더하기

print(result)