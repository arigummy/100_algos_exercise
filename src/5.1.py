sum = int(input("Enter sum: "))
orig_data = list(map(int, input("Enter data:\n").split()))
data = sorted(orig_data)

close = data[0] + data[-1]

l_ptr = 0
r_ptr = len(data) - 1
res1 = data[0]
res2 = data[-1]

while l_ptr != r_ptr and close != sum:
    x = data[l_ptr] + data[r_ptr]
    if abs(sum - x) < abs(sum - close):
        close = x
        res1 = data[l_ptr]
        res2 = data[r_ptr]
    if x > sum: r_ptr -= 1
    if x < sum: l_ptr += 1

a = orig_data.index(res1)
b = orig_data.index(res2)

l_res = min(a, b)
r_res = max(a, b)

if close == sum:
    print(f"[{l_res}]: {orig_data[l_res]}, [{r_res}]: {orig_data[r_res]}")
else:
    print(f"Dont find any match, but closer sum is {close}:")
    print(f"[{l_res}]: {orig_data[l_res]}, [{r_res}]: {orig_data[r_res]}")
