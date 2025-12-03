class Circle_buf:
    def __init__(self, size=0) -> None:
        self._size = size
        self._data = [0 for x in range(size)]
        self._position = 0

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index):
        if index >= self._size: raise IndexError("Index is out of range")
        return self._data[(self._position + index + self._size) % self._size]

    def add(self, value):
        self._data[self._position] = value
        self._position += 1
        if self._position == self._size: self._position = 0

    def __iter__(self):
        for i in range(self._size):
            yield self._data[(self._position + i + self._size) % self._size]

    def clear(self):
        for i in range(self._size):
            self._data[i] = 0
        self._position = 0

    def __str__(self):
        res = []
        for e in self:
            res.append(e)
        return f"{res}"

if __name__ == '__main__':
    buf = Circle_buf(10)

    for i in range(len(buf)+3):
        buf.add(i)

    print(buf)
    # print(buf[0])
    # print(buf[-1])
    buf.clear()
    print(buf)
