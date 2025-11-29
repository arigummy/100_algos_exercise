times = [[1, 2], [2, 3], [3, 4], [4, 5]]     # case 1
times = [[1, 4], [2, 3]]                     # case 2
times = [[8, 10], [1, 3], [2, 6], [15, 18]]  # case 3
times = [[1, 1], [1, 1], [2, 2]]             # case 4

times = sorted(times, key=lambda x: x[0])

print(f"Start: {times}")

res = []

MAX = len(times)

i = 0
while i < MAX-1:
    print(f"{i}:    ", end=' ')
    if max(times[i][0], times[i+1][0]) <= min(times[i][1], times[i+1][1]):
        new = [min(times[i][0], times[i+1][0]), max(times[i][1], times[i+1][1])]
        times[i] = new
        del times[i+1]
        MAX -= 1
        i -= 1
    print(f"{times}  MAX = {MAX}")

    i += 1

print(f"Res:   {times}")
