"""
[4, 6, 2, 9, 1]  # 정렬되지 않은 배열

1단계 : [4, 6, 2, 9, 1]
        4와 6과 2와 9와 1을 차례차례 비교합니다.
	      그 중 가장 작은 1과 맨 앞 자리인 4를 교체합니다!
       [1, 6, 2, 9, 4] 이렇게요!

자, 그러면 이제 가장 작은 숫자인 1이 맨 앞으로 왔습니다.
가장 작은 걸 가장 맨 앞으로 옮기기로 했으니까요!
그러면, 맨 앞자리를 제외하고 다시 한 번 반복하면 됩니다.

2단계 : [1, 6, 2, 9, 4]
           6과 2와 9와 4를 차례차례 비교합니다.
           그 중 가장 작은 2와 두번째 앞 자리인 6을 교체합니다!
       [1, 2, 6, 9, 4] 이렇게요!

3단계 : [1, 2, 6, 9, 4]
              6과 9와 4를 차례차례 비교합니다.
              그 중 가장 작은 4와 세번째 앞 자리인 6을 교체합니다!
       [1, 2, 4, 9, 6] 이렇게요!

4단계 : [1, 2, 4, 9, 6]
                 9와 6을 비교합니다!
                 그 중 가장 작은 6과 네번째 앞 자리인 9을 교체합니다!
       [1, 2, 4, 6, 9] 이렇게요!


자, 모두 정렬이 되었습니다! 어떠신가요? 감이 좀 오시나요?
버블 정렬보다 훨씬 더 적은 비교를 하는 것 같지만,
실제로는 각 배열을 계속해서 탐색하는 방식이라 2중 반복문을 사용해야 합니다!
"""

def selectionsort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimun = iter
        # 최솟값 우선 정렬이기 때문에 이미 정렬된 최소값을 제외시키면서 for문을 돌린다.
        for cur in range(iter + 1, len(lst)):
            if lst[cur] < lst[minimun]:
                minimun = cur

        if minimun != iter:
            lst[minimun], lst[iter] = lst[iter], lst[minimun]
    return lst


assert selectionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert selectionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

"""
def selectionsort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimun = iter
        for cur in range(iter + 1, len(lst)):
            if lst[cur] < lst[minimun]:
                minimun = cur

        if minimun != iter:
            lst[minimun], lst[iter] = lst[iter], lst[minimun]
    return lst
"""
