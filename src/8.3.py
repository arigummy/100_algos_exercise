import copy

matrix = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 0, 1]
]

rows = len(matrix)
cols = len(matrix[0])

dp_matrix = copy.deepcopy(matrix)

for i in range(cols):
    dp_matrix[0][i] = matrix[0][i]

for i in range(rows):
    dp_matrix[i][0] = matrix[i][0]

for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][j]: dp_matrix[i][j] = min(dp_matrix[i-1][j], dp_matrix[i][j-1], dp_matrix[i-1][j-1]) + 1
        else: dp_matrix[i][j] = 0

# print(dp_matrix)

max_a = 0

for i in range(rows):
    for j in range(cols):
        max_a = max(dp_matrix[i][j], max_a)

print(f"Max square: {max_a**2}")
