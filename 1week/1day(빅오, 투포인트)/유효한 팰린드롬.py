# 가장 긴 팰린드롬(Manacher알고리즘, https://programmers.co.kr/learn/courses/30/lessons/12904)
# -> 주어진 문자열이 펠린드롬인지 판별

# palindrome: 양쪽이 대칭 되는 문자열 ex)abcba

# 풀이1)리스트로 변환
# point)
# isalnum(): 영문자, 숫자 여부 판별
# lower(): 모두 소문자 변환
# list.pop(ㅑ): i번째 요소를 꺼내 그 요소를 return한다. (list에서 그 요소는 사라진다.)
#               i 빈 값인 경우[ pop() ] list의 맨 마지막 요소를 꺼내 return 한다.
#  
import collections
import re

s = "A man, a plan, a canal: panama"

def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    #pop(0) -> O(n)
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

        return True
    # 1. while문 조건 값이 false일때까지 실행
    # 2. if문 리스트의 첫 요소와 끝 요소가 다르면 false return, 같으면 True return
    # 3. 다시 -> while (블록이 없으니 햇갈림)

#     의문점) "s: str" parmeter에 데이터 타입 제한?, "self"는 this 인가?, "-> bool"은 bool데이터타입 명시?
            # -> 타입힌트! 타입 명시 맞음. self는 this랑 비슷한 의미, 파이썬 자체에서 기본 객체로 주어짐. 가져다가 쓰기만 하면 됨.




# 풀이2)데크 자료형을 이용한 최적화
def isPalindrome2(self, s: str) -> bool:
    strs = collections.deque()

    s = "A man, a plan, a canal: panama"
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    #pop(0) -> O(n)
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft != strs.pop():
            return False

    return True
# Deque로 자료형 선언 -> popleft() 사용 -> 5배 이상 속도 향상
# 이유) 리스트의 pop(0) -> O(n), 데크의 popleft() -> O(1)
#      -> 추정) 리스트의 pop(): 스택(선입후출) -> pop(0)를 찾기위해 리스트의 0 요소를 찾는 알고리즘을 거쳐야한다.
#      -> 데크는 양방향이기때문에 앞으로 꺼내면 됨?


# 스택(stack): 선입후출
    # 데이터 입력:push, 출력:Pop

# 파이썬에서의 스택(Stack)
    # 데이터의 입력: push -> append()
    # 데이터의 출력: pop -> pop()
        # pop은 데이터 구조에서 맨 마지막에 있는 값을 뽑아서 준다고 이해, 즉 item을 return해주는 함수.
        # pop으로 뽑아낸 데이터는 원래 리스트 내에서 없어진다.

# 큐(Queue): 선입선출(한방향)
#   줄이라는 의미로, 파이썬의 자료구조에서 먼저 줄을 선 데이터가 먼저 return된다.

# 파이썬에서 큐(Queue)
#   데이터 입력: push -> append()
#   데이터 출력: get  -> pop()
#         pop(0)을 해서 맨앞의 데이터를 뽑아온다.

# 데크(Deque): 양방향
#  자료구조의 앞, 뒤 방향에서 element를 추가하거나 삭제할 수 있다.
#  collections 모듈에서 deque라는 method로 지원함.
#  시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는 데 최적화된 연산 속도를 제공
#  의문점) 중간 값을 넣고 빼는 경우는?



# 풀이3) 슬라이싱 사용
def isPalindrome3(self, s: str) -> bool:
    s = s.lower()
    # 정규식의 불필요 문자 필터링 ->
    s = re.sub('[^a-z0-9]', '', s)

    # 슬라이싱
    return s == s[::-1]

# 정규표현식 (re 모듈 필요),  re(regular expression의 약어)
# ^: 반대(not), -:범위 ex) [a-zA-Z]: 알파벳 모두
# [^a-z0-9] -> ?,  알파벳 소문자, 0-9 제거인가...

# re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
#  ex) re.sub('apple|orange', 'fruit', 'apple box orange tree')
#      -> 'fruit box fruit tree'

# 참조)https://wikidocs.net/4308#re


# 풀이4)c언어를 통한 해결
# ->아직 불가

# 가장 긴 팬린드롬 부분 문자열
# point
# expand:

def longestPalindrome(self, s: str) -> str:
    #팰린드롬 판별 및 투포인터 확장
    def expand(left: int, right: int) -> str:
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    #해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 and s == s[::-1]:
        return s

    result = ''
    #슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) -1):
        result = max(result,
                     expand(i, i+1),
                     expand(i, i+1),
                     key=len)
    return result
















