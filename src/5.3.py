data = list(map(int, input("ENTER DATA:\n").split()))
data.sort()

res = []

for i in range(len(data) - 2):
    left = i + 1
    right = len(data) - 1
    while left != right:
        sum = data[i] + data[left] + data[right]
        if sum < 0: left += 1
        elif sum > 0: right -= 1
        else:
            res.append({i:data[i], left:data[left], right:data[right]})
            break

print(res)
