num = int(input())

for i in range(num):
    input_data = input()
    bracket = []

    for j in input_data:
        if j == "(":
            bracket.append(j)
        elif j == ")":
            if len(bracket) != 0 and bracket[-1] == "(":
                bracket.pop()
            else:
                bracket.append(")")
                break

    if len(bracket) == 0:
        print("YES")
    else:
        print("No")


# 풀이2)'
a = int(input())
for _ in range(a):
    b = input()
    s = list(b)
    sum = 0

    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')