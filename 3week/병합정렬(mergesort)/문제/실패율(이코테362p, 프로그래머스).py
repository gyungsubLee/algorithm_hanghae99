# 문제)https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    fail_rate = {}
    total_user = len(stages)

    for stage in range(1, N+1):
        if total_user != 0:
            fail_user = stages.count(stage) # count() 문자열 내부에서 특정 문자의 개수 카운팅함.
            fail_rate[stage] = fail_user/total_user
            total_user -= fail_user # +=, -= : 좌변 값에 우변값을 더함, 뺌
        else:
            fail_rate[stage] = 0

    return sorted(fail_rate, key=lambda x:fail_rate[x], reversed=True)
    #  result는 dictionary이므로 sorted에 result를 그냥 넘기면 result의 keys가 들어갑니다.
    #  keys는 생략이 가능합니다. 거기에 lambda는 기준을 result[x]: 즉 value로 정렬한다는 뜻입니다. 그래서 key가 출력되게 됩니다.