data = [1, 3, 5, 2, 3, 1, 4, 2, 6, 5, 7]

k = 4

Ex = 0
Ex2 = 0

for i in range(k):
    Ex += data[i]
    Ex2 += data[i] ** 2

for i in range(len(data) - k):
    disp = (Ex2 - (Ex ** 2 / k)) / (k - 1)
    print(f"Window {i} with disp = {disp:.3}: ", end='')
    for j in range(k):
        if data[i+j] > disp:
            print(f"{data[i+j]}", end='')
            print(", ", end='') if j == k - 1 else print(" ", end='')
    print()
    Ex -= data[i]
    Ex += data[i+k]
    Ex2 -= data[i] ** 2
    Ex2 += data[i] ** 2
