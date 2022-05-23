"""
[1, 2, 3, 5]  # 정렬된 배열 A
[4, 6, 7, 8]  # 정렬된 배열 B
[] # 두 집합을 합칠 빈 배열 C


        ↓
1단계 : [1, 2, 3, 5]
        ↓
       [4, 6, 7, 8]
        1과 4를 비교합니다!
        1 < 4 이므로 1을 C 에 넣습니다.
     C:[1]

           ↓
2단계 : [1, 2, 3, 5]
        ↓
       [4, 6, 7, 8]
        2와 4를 비교합니다!
        2 < 4 이므로 2를 C 에 넣습니다.
     C:[1, 2]


              ↓
3단계 : [1, 2, 3, 5]
        ↓
       [4, 6, 7, 8]
        3과 4를 비교합니다!
        3 < 4 이므로 3을 C 에 넣습니다.
     C:[1, 2, 3]

                 ↓
3단계 : [1, 2, 3, 5]
        ↓
       [4, 6, 7, 8]
        5와 4를 비교합니다!
        5 > 4 이므로 4을 C 에 넣습니다.
     C:[1, 2, 3, 4]

                 ↓
3단계 : [1, 2, 3, 5]
           ↓
       [4, 6, 7, 8]
        5와 6을 비교합니다!
        5 < 6 이므로 5을 C 에 넣습니다.
     C:[1, 2, 3, 4, 5]

엇, 이렇게 되면 A 의 모든 원소는 끝났습니다!

그러면 B에서 안 들어간 원소인
       [6, 7, 8] 은 어떡할까요?
하나씩 C 에 추가해주면 됩니다.
     C:[1, 2, 3, 4, 5, 6, 7, 8] 이렇게요!

그러면 A 와 B를 합치면서 정렬할 수 있었습니다.
"""


def merge(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    # i는 index이며 0부터 시작하기 때문에 array의 길이와 같으면 array의 마지막 요소를 벗어남.
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2

    L = lst[:mid]
    R = lst[mid:]

    L_sort = mergesort(L)
    R_sort = mergesort(R)
    return merge(L_sort, R_sort)


#파이썬 내장함수 sort가 있다.
      #sort와 sorted의 차이 
        # sort는 현재의 리스트는 오름차순(defalt)으로 정렬 (reverse 시 내림차순)
        # sorted는 현재의 리스트는 복사해 새로운 리스트를 만든 후 오름차순 정렬

#팀정렬(Tim sort)이라고 하는데,
# 이 정렬 알고리즘은 Insertion sort와 Merge sort를 결합하여 만든 정렬이다.
arr.sort()
sorted()


