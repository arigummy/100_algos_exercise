data = [
    [1, 2, 3],
    [4, 7, 5]
]

class SimpleMatrix:

    def __init__(self, data):
        self._data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self._data])

    def __repr__(self) -> str:
        return f"SimpleMatrix({self._data})"

    def rotate(self, pi=0.5):
        if (pi) % 0.5 != 0: return
        neg = False if pi >= 0 else True
        for x in range(int(abs(pi) / 0.5)):
            self._transpose(negative=neg)

    def flip_h(self):
        for i in range(self.rows):
            self._data[i] = self._data[i][::-1]

    def flip_v(self):
        self._data = self._data[::-1]

    def _transpose(self, negative=False):
        buf = [[0 for x in range(self.rows)] for y in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                x_i = self.rows - i - 1 if not negative else i
                x_j = j if not negative else self.cols - j - 1
                buf[j][i] = self._data[x_i][x_j]
        self.rows, self.cols = self.cols, self.rows
        self._data = buf

x = SimpleMatrix(data)

x.flip_v()
print(x)
