delta = list(map(int, input("ENTER:\n").split()))

capital = [1 + 0.01 * x for x in delta]
capital.insert(0, 1)
print(capital)

cur_max = global_max = capital[0]
max_l = max_r = 0

cur_max_l = cur_max_r = 0

for i in range(1, len(capital)):
    prod = capital[i] * cur_max
    if prod > capital[i]:
        cur_max = prod
        cur_max_r += 1
    else:
        cur_max = capital[i]
        cur_max_l = cur_max_r = i
    if cur_max > global_max:
        max_l, max_r = cur_max_l, cur_max_r
        global_max = cur_max

profit = (global_max - 1) * 100
print(f"Max profit: {profit:.2f}%")
print(f"Days from {max_l-1} to {max_r}")




# print(global_max)
