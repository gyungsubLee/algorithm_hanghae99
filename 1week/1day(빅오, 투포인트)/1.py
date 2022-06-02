# palindrome: 양쪽이 대칭 되는 문자열 ex)abcba

# 참조)https://programmers.co.kr/learn/courses/30/lessons/12904
# point: Manacher알고리즘
#문자열 배열에서 i번째 문자를 중심으로 하는 가장 긴 팰린드롬 길이를 반지름 r을 저장하여 사용한다.
# O(n)

# 문제) 주어진 문자열이 palindrome인지 확인해라.

# 풀이1)리스트로 변환
# point)
# isalnum(): 영문자, 숫자 여부 판별
# lower(): 모두 소문자 변환
# list.pop(i): i번째 요소를 꺼내 그 요소를 return한다. (list에서 그 요소는 사라진다.)
#           :()일 경우, 맨 마지막 요소를 출력한다.(list에서는 맨 마지막 요소가 삭제됨.)
def isPalindrome(self, s: str) -> bool:
    s = "A man, a plan, a canal: panama"
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1 :
        if strs.pop(0) != strs.pop():
            return False

    return True

