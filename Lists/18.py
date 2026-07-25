# dynamic for loop for matrix , eg 4x5

matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
]

rows = len(matrix)
columns = len(matrix[0])

for i in range(0, rows):
    for j in range(0, columns):
        print(matrix[i][j], end=" ")
    print()