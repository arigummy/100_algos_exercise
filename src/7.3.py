from os import dup


data =  [1, 3, 2, 6, 1, 5, 2, 3, 2, "EOF"]

l_ptr = r_ptr = 0

max_l_ptr = max_r_ptr = 0
uniq = []

while r_ptr != len(data) - 1:

    while r_ptr < len(data)-1 and data[r_ptr] not in uniq:
        uniq.append(data[r_ptr])
        r_ptr += 1

    if r_ptr - l_ptr > max_r_ptr - max_l_ptr:
        max_l_ptr, max_r_ptr = l_ptr, r_ptr

    while l_ptr != r_ptr:
        uniq.remove(data[l_ptr])
        l_ptr += 1
        if data[l_ptr-1] == data[r_ptr]: break

    if r_ptr - l_ptr > max_r_ptr - max_l_ptr:
        max_l_ptr, max_r_ptr = l_ptr, r_ptr


print("RES: ")
for i in range(max_l_ptr, max_r_ptr):
    print(data[i], end=' ')
