"""
[4, 6, 2, 9, 1]  # 정렬되지 않은 배열

1단계 : [4, 6, 2, 9, 1]
        4와 6을 비교합니다!
        4 < 6 이면 그대로 둡니다.

2단계 : [4, 6, 2, 9, 1]
           6과 2를 비교합니다!
           6 > 2 이므로 둘을 변경합니다!
       [4, 2, 6, 9, 1] 이렇게요!

3단계 : [4, 2, 6, 9, 1]
              6과 9를 비교합니다!
              6 < 9 이면 그대로 둡니다.

4단계 : [4, 2, 6, 9, 1]
                 9와 1를 비교합니다!
                 9 > 1 이므로 둘을 변경합니다!
       [4, 2, 6, 1, 9] 이렇게요!

자, 그러면 이제 한 바퀴를 돌렸죠?
이 과정에서 가장 큰 숫자인 9가 맨 뒤로 왔습니다.
큰 게 나오면 둘의 자리를 변경했으니 가장 맨 뒤에 갔다는 소리입니다!
그러면, 맨 뒷자리를 제외하고 다시 한 번 돌리면 됩니다!

5단계 : [4, 2, 6, 1, 9]
        4와 2을 비교합니다!
        4 > 2 이므로 둘을 변경합니다.
       [2, 4, 6, 1, 9] 이렇게요!

6단계 : [2, 4, 6, 1, 9]
           4와 6을 비교합니다!
           4 < 6 이면 그대로 둡니다.

7단계 : [2, 4, 6, 1, 9]
              6와 1을 비교합니다!
              6 > 1 이므로 둘을 변경합니다!
       [2, 4, 1, 6, 9] 이렇게요!

그러면 이제 두 번째로 큰 숫자인 6이 맨 뒤에서 두번쨰로 왔습니다!
여기까지만 비교하시면 됩니다. 6과 9을 비교할 필요는 없습니다.
다시 한 번 가볼게요!

8단계 : [2, 4, 1, 6, 9]
        2와 4을 비교합니다!
        2 < 4 이면 그대로 둡니다.

9단계 : [2, 4, 1, 6, 9]
           4와 1을 비교합니다!
           4 > 1 이므로 둘을 변경합니다!
       [2, 1, 4, 6, 9] 이렇게요!

자, 이제 세 번쨰로 큰 숫자인 4가 맨 뒤에서 세번째로 왔습니다!
마지막 비교만 하면 됩니다!

10단계 : [2, 1, 4, 6, 9]
         2와 1을 비교합니다!
         2 > 1 이므로 둘을 변경합니다!
        [1, 2, 4, 6, 9] 이렇게요!

자, 모두 정렬이 되었습니다! 어떠신가요? 감이 좀 오시나요?
"""

def bubblesort(lst):
    # 최댓값을 구하는 알고리즘을 len(lst) -1 만큼 반복한다.
    iters = len(lst) - 1
    for iter in range(iters):
        # 이미 구한 최댓값은 범위에서 제외한다.
        wall = iters - iter
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]
    return lst

assert bubblesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert bubblesort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]


"""
def bubblesort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        wall = iters - iter
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur + 1] = lst[cur + 1], len[cur]
    return lst
"""
