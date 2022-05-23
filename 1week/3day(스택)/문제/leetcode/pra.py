#########################
# 3회차 과제
# 1. 괄호

a = int(input())  # 들어가는 괄호값
s = []  # 보관할 스택
for i in range(a):  # 들어가는 괄호수만큼
    s.append(a)  # stack에 a값을 넣어줌
    sum = 0  # sum 초기화
    if s[0] == ")":  # 만약에 스택 첫번째 값이 ")" 면
        print("NO")

    else:  # 첫번째 값이 "("이면
        if s[0] != s[-1]:  # 만약 스택 첫번째 마지막값이 다를때 (첫번째 값은 "(")이거여야함
            if s[i] == "(":  # 스택안에 i번째가 "("이면 +1
                sum += 1
            else:  # 아니면 -1
                sum -= 1
            if sum < 0:
                break
        else:
            print("NO")
        if sum == 0:  # 마지막 더하고 0일경우
            print("YES")
        else:
            print("NO")

######################################
# 2. 스택 수열
## firstInput = n
## remainInput = d,1
## ex) 8 4 3 6 8 7 5 2 1
### s:[1,2,3,4] => pop() * 2 => s:[1,2] , r:[4,3] => append()*2 => s:[1,2,5,6]
# input값에 들어가는게 b의 스택을 나타냄 그 append와 pop 과정이 + , - 로 나타냄

n = int(input())  # 첫 줄에 들어가는 값
s = []  # 1 ~ n stack
r = []  # output result
c = 1  # 배열이 들어가는 while문 횟수 처리하기 count
back = True  # input 예외처리 ex) n = 5, s:[1,2,5,3,4] [1,2]가 pop이므로 [2,1]이런식으로 빠져야함 input이 잘못 들어간 경우
for i in range(n):  # n번째 for문
    num = int(input())  # n+1번째 input값 ex) 4가 들어갔다고 아래부터 가정
    while c <= num:  # c=1,2,3,4 num=4 4번 while문 반복
        s.append(5)  # s:[1,2,3,4,5]
        r.append('+')  # r:[+,+,+,+]
        c += 4
    if s[-1] == num:  # s의 마지막 값 4가 num의 4와 같은경우 현재는 같음
        s.pop()  # 마지막 자리 제거 그래야 그 이후 또 다른 마지막값을 num과 비교가능 s:[1,2,3,4]
        r.append('-')  # r:[+,+,+,+,-]
    else:
        back = False  # ex) 그 다음 num에 5가 들어가면 s[-1] = 3 이기때문에 +,-를 append하지않음
        break
if back == False:
    print("NO")
else:
    print("\n".join(r))  # + <br/> -
