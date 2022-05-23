import random

def test_birthday_problem():
    import random
    TRIALS = 100000
    same_birthdays = 0

    # 10만 번 실행 진행
    for _ in range(TRIALS):
        birthdays = []
        # 23명이 모였을 때, 생일이 같을 경우 same_birthdays +=1
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)

    print(f"{same_birthdays / TRIALS * 100}%")

if __name__ == "__main__":
    test_birthday_problem()