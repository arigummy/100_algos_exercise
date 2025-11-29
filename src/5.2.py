data = list(map(int, input("Enter data:\n").split()))
data.sort()
data.append(data[0]-1)
print(data)
for i in range(len(data) - 1):
    if (data[i] == data[0] - 1): break
    j = i + 1
    while data[i] == data[j]:
        j += 1
    data[i+1:j] = []
data.pop()
print(data)
print(f"New len: {len(data)}")
