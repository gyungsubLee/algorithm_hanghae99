"""
# keypoint) sorted, lambda

example_list = [(0, 3), (1, 2), (2, 7), (3, 5), (4, 1)]

# sorted 함수 내에  key = lambda ~~ 를 통해서 비교할 대상을 정해주면 됨.
example_sorted_list = sorter(example_list, key=lambda x : x[1])
  -> [(4, 1), (1, 2), (0, 3), (3, 5), (2, 7)]

#두번째 숫자 기준으로 내림차순 정렬: 비교대상에 '-'붙이기
example_sorted_list = sorter(example_list, key=lambda x :-x[1])
   -> [(2, 7), (3, 5), (0, 3), (1, 2), (4, 1)]
"""

#문제) input: [이름, 국어, 영수, 수학]
#      1. 국어 내림차순
#      2. 국어 점수 동일, 영어 오름차순
#      3. 국어, 영어 점수 동일, 수학 내림차순
#      4. 모든 점수가 같다면, 이름 오름차순


N = int(input())

score_list = []
for i in range(N):
    [name, kor, eng, math] = map(str, input().split())
    score_list.append([name, int(kor), int(eng), int(math)])


sorted_score_list = sorted(score_list, key=lambda x :(-x[1], x[2], -x[3], x[0]))

for score in sorted_score_list:
    print(score[0]) #name 출력