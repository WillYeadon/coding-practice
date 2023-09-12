class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Why bother using this min stack? Well if you just have one stack and then
# use return min(self.stack) you have to look through a potentially very
# long stack e.g. O(n) whereas you can make it effectively constant time if
# you return self.minStack[-1]. To make self.minStack[-1] the minimum you
# need to make sure the last value is always the min hence the extra lines in 
# push. For the first instance need if self.minStack then just overwrite