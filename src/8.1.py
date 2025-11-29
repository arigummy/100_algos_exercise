cave = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0]
]
M = len(cave)
N = len(cave[0])

start_point = 0, M - 1
finish_point = N - 1, 0

def is_floor(point):
    if point[0] not in range(0, N): return False
    if point[1] not in range(0, M): return False
    if cave[point[1]][point[0]]: return False
    return True

class Vile_Mold:
    def __init__(self, start_point):
        self._start = start_point

    def run(self):
        if self._grow(self._start): print("Yeees! This Vile Mold got out :)")
        else: print("Oh no... Thie Vile Mold died :(")

    def _grow(self, point):
        # print("Game was started!!!")
        stack = [point]
        visited = set()

        while stack:
            x, y = stack.pop()
            if (x, y) not in visited:
                visited.add((x, y))
                if finish_point == (x, y): return True
                if is_floor((x, y)): stack.append((x+1, y))
                if is_floor((x, y)): stack.append((x-1, y))
                if is_floor((x, y)): stack.append((x, y+1))
                if is_floor((x, y)): stack.append((x, y-1))

        return False

mold = Vile_Mold(start_point)
mold.run()
