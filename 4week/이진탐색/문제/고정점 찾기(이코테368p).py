"""
고정점: 수열의 원소 중 index = value 것

ex) a = {-15, -4, 2, 8, 13}
    고정점: a[2] = 2

수열에 고정점 이 있으면 고정점 출력, 없으면 -1 출력

조건)
하나의 수열에 N개의 서로 다른 원소 포함
모든 원소 오름차순
시간 복잡도 O(nlongN)
"""

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    if array[mid] > mid:
        return binary_search(array, start, mid - 1)
    # 중간점이 가르키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, mid + 1, end)

    n = int(input())
    array = list(map(int, input().split()))

    # 이진 탐색(binary search) 수행
    index = binary_search(array, 0, n - 1)

    # 고정점이 없는 경우 -1 출력
    if index == None:
        print(-1)
    # 고정점이 있는 경우 해당 인덱스 출력
    else:
        print(index)






def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == mid:
        return mid

    if array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)

    n = int(input())
    array = list(map(int, input().split()))

    index = binary_search(array, 0, n - 1)

    if index == None:
        print(-1)
    else:
        print(index)
























from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력받기
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)

