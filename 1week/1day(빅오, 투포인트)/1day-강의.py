# 점근 표기법
# 빅오 표기법 O(N), 최악의 성능이 나올 때, 연산 시간 계산 시 사용
# 빅오메가, 최선의 성능이 올 때 ...(잘 안씀)

# 문제1) 문자열 중 가장 많이 쓰인 알파벳을 찾아라.
import string
from pprint import pprint
text = 'hello, this is sparta'
counter = {}

    # 풀이1)21 번 연산 O(n)
for char in text:
    if not char.isalpha():
        continue
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1
pprint(counter)

    # for문 2중첩 드물다. 올바른 풀이가 아니니 다시 생각해라.
    # 풀이2)26 * 21 번 연산
    # O(n^2) (^:제곱, **:제곱근)
counter2 = {}
for lo in string.ascii_lowercase:
    for char in text:
        if lo == char:
            if lo in counter2:
                counter2[lo] += 1
            else:
                counter2[lo] = 1
pprint(counter2)

# 문제2) 숫자 배열, 특정 숫자 존재 유무 확인
# O(n)
arr = [3, 5, 6, 1, 2, 4]

def is_number_exist(num, arr):
    for el in arr:
        if num == el:
            return True
    return False

#공간 복잡도는 흔치 않다. C언어를 사용하지 않는 이상 잘 안나옴.(인베디드?)


# 문제3)
# point) 
# string.ascii_lowercase:알파벳(1 ~ 26까지)
# range(i) -> [0, 1, ... i-1, i] 배열 만듬.
# ord: 알파벳(대소문자) -> 숫자로 바꿔줌. [아스키 코드]
#                   ex) a -> 97, a -> 98 ...
# join([str(num) for num in result] 

# 풀이1)
def get_idx_naive(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    print(' '.join([str(num) for num in result]))

#풀이2)
def get_idx(word):
    # point 1. ord: 알파벳(대소문자) -> 숫자로 바꿔줌.
                     # a -> 97, a -> 98 ...
    # point 2. O(n^2) -> O(n)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97 
        # result[idx]는 해당 알파벳의 index를 가르킨다.
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))

get_idx_naive('baekjoon')
get_idx('baekjoon')

# 정리)
# 시간복잡도: 빅오, O(n) 최악의
# 공간복잡도

# 마음자짐)
# 모르는게 당연하다. 견디고 이겨내라.
# 막히면 천천히 생각해서 온전히 이해해라.
# 꼭 구현을 해라.

# 강의가 짧아도 내용이 짧은게 아니다.

