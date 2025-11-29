import copy

class BitMatrix:

    def __init__(self, M:int=1, N:int=1):
       self._M = M
       self._N = N
       self._bits = 2 ** (M*N) - 1
       # quantity = M * N
       # while self._bits < quantity:
       #     self._bits <<= 1

    def get_bits(self):
        return bin(self._bits)

    def print(self):
        for y in range(self._N):
            for x in range(self._M):
                # print(self._bits >> (y * self._N + x) & 1, end=' ')
                print(self.get_bit(x, y), end=' ')
            print()

    def set_bit(self, x:int, y:int, val:bool):
        if x in range(self._M) and y in range(self._N):
            if val:
                self._bits |= 1 << (y*self._M + x)
            else:
                self._bits &= ~(1 << (y*self._M + x))

    def get_bit(self, x:int, y:int):
        if x in range(self._M) and y in range(self._N):
            return (self._bits >> (y * self._M + x)) & 1
        else:
            return 0

    def copy(self):
            new_matrix = BitMatrix(self._M, self._N)
            new_matrix._bits = copy.deepcopy(self._bits)
            return new_matrix

    def trasnpose(self):
        buf = self.copy()
        self._M, self._N = self._N, self._M
        for y in range(self._N):
            for x in range(self._M):
                self.set_bit(x, y, buf.get_bit(y, self._M - x - 1))

    def count_ones(self):
        res = 0
        bits = int(self._bits)
        while bits > 0:
            res += bits & 1
            bits >>= 1
        return res


x = BitMatrix(3, 3)
# x.set_bit(0, 1, 0)
# x.set_bit(1, 2, 0)

print(x.count_ones())
