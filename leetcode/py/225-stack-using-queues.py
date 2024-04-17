class MyStack:
    def __init__(self):
        self.data = [] 

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return len(self.data) == 0