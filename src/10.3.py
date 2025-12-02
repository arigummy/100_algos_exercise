histogram = [2, 1, 5, 6, 2, 3] # res: 10
# histogram = [2, 2, 2] # res: 6
# histogram = [1, 3, 2, 1, 4, 2, 1] # res: 7

histogram.append(0)
histogram.insert(0, 0)

stack = [0]
max_area = 0


for i in range(1, len(histogram)):
    height = histogram[i]
    while height < histogram[stack[-1]]:
        max_area = max(max_area, histogram[stack.pop()] * (i - stack[-1] - 1))


    if height >= histogram[stack[-1]]:
        stack.append(i)



print(f"MAX area is {max_area}")
