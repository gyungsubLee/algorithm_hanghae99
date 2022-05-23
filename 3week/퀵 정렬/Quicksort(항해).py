"""
[1, 6, 2, 9, 4]  # 정렬되지 않은 배열

1단계: [1, 6, 2, 9, 4]
      마지막 원소인 4를 pivot으로 삼습니다.
	    pivot보다 작은 집합의 인덱스 i를 -1로 설정합니다.
			(i=-1)

2단계: [1, 6, 2, 9, 4]
			j를 0에서부터 3까지 살펴봅니다.
			j가 0이므로 지금 살펴보고 있는 값은 1 입니다.
      1는 pivot(4)보다 작습니다.
			i를 1 증가시켜 0으로 만듭니다.
			i 와 j 의 위치를 바꿉니다.
      i와 j가 동일하므로 아무 일도 일어나지 않습니다.
			(i=0, j=0)

3단계: [1, 6, 2, 9, 4]
			j를 1 증가시켜 1로 만듭니다.
		  지금 살펴보고 있는 값은 6 입니다.
      6은 pivot(4)보다 큽니다.
			넘어갑니다.
			(i=0, j=1)

4단계: [1, 6, 2, 9, 4]
			j를 1 증가시켜 2로 만듭니다.
		  지금 살펴보고 있는 값은 2 입니다.
      2는 pivot(4)보다 작습니다.
			i를 1 증가시켜 1로 만듭니다.
			i(1) 와 j(2) 의 위치를 바꿉니다.
			배열은 [1, 2, 6, 9, 4]가 됩니다.
			(i=0, j=2)

5단계: [1, 2, 6, 9, 4]
			j를 1 증가시켜 3으로 만듭니다.
		  지금 살펴보고 있는 값은 9 입니다.
      9는 pivot(4)보다 큽니다.
			넘어갑니다.
			(i=1, j=3)

6단계: j를 0부터 3까지 모두 살펴보았습니다.
		  i는 pivot보다 작은 집합의 범위를 나타내므로, i+1과 pivot의 위치를 바꿉니다.
	    배열은 [1, 2, 4, 9, 6] 이 됩니다.

7단계: [1, 2]와 [9, 6]을 대상으로 1~6단계를 반복합니다.
      결과적으로 [1, 2, 4, 6, 9]가 됩니다.
			정렬이 끝났습니다.
"""

def quicksort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe]
        i = ps - 1
        for j in range(ps, pe):
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]

        part[i + 1], part[pe] = part[pe], part[i + 1]
        return i + 1

    if start >= end:
        return None

    p = partition(lst, start, end)
    quicksort(lst, start, p - 1)
    quicksort(lst, p + 1, end)
    return lst

assert quicksort([4, 6, 2, 9, 1], 0, 1) == [4, 6, 2, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 2) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 3) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 4) == [1, 2, 4, 6, 9]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 1) == [2, 3, 1, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 2) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 3) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 4) == [1, 2, 3, 3, 5, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 5) == [1, 2, 2, 3, 3, 5, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 6) == [1, 2, 2, 3, 3, 3, 5]


