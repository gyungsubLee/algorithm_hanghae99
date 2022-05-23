# 문제) https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

# input: progresses, speeds

# 처음 문제구현
#  -> for 문


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

ag1 = [93, 30, 55]
ag2 = [1, 30, 5]
solution(ag1, ag2)