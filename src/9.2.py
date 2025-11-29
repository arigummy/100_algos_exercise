tasks = [[5, 7, 2], [1, 3, 5], [4, 6, 8], [2, 5, 3]]

tasks = sorted(tasks, key=lambda x: x[1])
print(tasks)
dp = [0]

for i in range(len(tasks)):

    max_not_inter = 0
    for x in range(i):
        if tasks[x][1] <= tasks[i][0]:
            max_not_inter = x+1

    dp.append(max(dp[i], tasks[i][2] + dp[max_not_inter]))

print(dp)

max_sum = dp[len(dp)-1]
res = []

for i in range(len(tasks)):
    if dp[i+1] != dp[i]: res.append(tasks[i])

print(res)
