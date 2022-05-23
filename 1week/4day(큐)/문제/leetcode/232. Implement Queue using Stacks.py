# 링크)https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # output값이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    # 의문점) output값이 다 나가기 전에 push가 들어오면?
    # -> pop시 output에 저장된 value 값이 나감, push 시 input에 저장되었다가 output이
    #    None일 시 다시 output에 들어간다.
    #    한마디로 전혀 상관없는 쓸데없는 고민이다.

    def empty(self) -> bool:
        return self.input == [] and self.output == []