# 문제)https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    command = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    road = set() # set(): 중복 자동제거
    cur_x, cur_y = (0, 0)

    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            # 굳이 2개를 넣고 나누는 이유는?
            road.add((cur_x, c
                      2next_y, cur_x, cur_y))
            #?? 왜 나오지?
            cur_x, cur_y = next_x, next_y
    return len(road) // 2