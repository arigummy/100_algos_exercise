class DS_Deque:
    def __init__(self):
        # self._max_size = value
        self._stack_in = []
        self._stack_out = []

    def push(self, value):
        self._stack_in.append(value)

    def pop(self):
        if not self._stack_out and self._stack_in:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())

        if self._stack_out: return self._stack_out.pop()
        else: return None

x = DS_Deque()

x.push(1)
x.push(13)

print(x.pop())
x.push(4)
print(x.pop())
print(x.pop())
