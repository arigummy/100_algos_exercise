dim = int(input("Enter N imension: "))

buf = [[0 for i in range(dim)] for y in range(dim)]

def get_dir(dir:int):
    A = (dir >> 1) & 1
    B = dir & 1
    x = (1-B) * (1 - 2 * A)
    y = B * (1 - 2 * A)

    return (x, y)

def in_area(x, y, dim, round):
    if x < (0 + round) or y < (0 + round): return False
    if x >= (dim - round) or y >= (dim - round): return False
    return True

rounds = -(dim // -2)

count = 1

for round in range(rounds):
    x = round
    y = round
    dir = 0
    while dir != 4:
        if dir == 3 and x == y == round: break
        buf[y][x] = count
        dx, dy = get_dir(dir)
        if in_area(x+dx, y+dy, dim, round):
            count += 1
            x += dx
            y += dy
        else:
            dir += 1

for i in range(dim):
    for j in range(dim):
        print(f"{buf[i][j]:^4}", end=' ')
    print()
