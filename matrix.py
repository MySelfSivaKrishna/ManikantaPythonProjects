if __name__ == '__main__':
    total_matrix = [[4, 2, 1, 3], [3, 2, 0, 3], [2, 0, 0, 2], [5, 0, 4, 2]]

    Zero_location = []

    maxrowsize = len(total_matrix) - 1
    maxcolsize = len(total_matrix[0]) - 1
    min = 0
    perimeter = 0
    enemies = 0

for row in range(0, len(total_matrix)):
    for column in range(0, len(total_matrix[row])):
        if (total_matrix[row][column] == 0):
            Zero_location.append((row, column))

print(Zero_location)

for each in Zero_location:
    row_index = each.__getitem__(0)
    column_index = each.__getitem__(1)
    if (row_index - 1 >= min):
        if total_matrix[row_index - 1][column_index] != 0:
            perimeter = perimeter + 1
    else:
        perimeter = perimeter + 1
    if (row_index + 1 <= maxrowsize):
        if total_matrix[row_index + 1][column_index] != 0:
            perimeter = perimeter + 1
    else:
        perimeter = perimeter + 1
    if (column_index - 1 >= min):
        if total_matrix[row_index][column_index - 1] != 0:
            perimeter = perimeter + 1
    else:
        perimeter = perimeter + 1
    if (column_index + 1 <= maxcolsize):
        if total_matrix[row_index][column_index + 1] != 0:
            perimeter = perimeter + 1
    else:
        perimeter = perimeter + 1

enemies_matrix = total_matrix.copy()

for each in Zero_location:
    row_index = each.__getitem__(0)
    column_index = each.__getitem__(1)
    if (column_index - 1 >= min):
        if total_matrix[row_index][column_index - 1] != 0:
            enemies = enemies + enemies_matrix[row_index][column_index - 1]
            enemies_matrix[row_index][column_index - 1] = 0
    if (column_index + 1 <= maxcolsize):
        if total_matrix[row_index][column_index + 1] != 0:
            enemies = enemies + enemies_matrix[row_index][column_index + 1]
            enemies_matrix[row_index][column_index + 1] = 0
    if (row_index - 1 >= min):
        if total_matrix[row_index][column_index - 1] != 0:
            enemies = enemies + enemies_matrix[row_index - 1][column_index]
            enemies_matrix[row_index - 1][column_index] = 0
    if (row_index + 1 <= maxrowsize):
        if total_matrix[row_index][column_index + 1] != 0:
            enemies = enemies + enemies_matrix[row_index + 1][column_index]
            enemies_matrix[row_index + 1][column_index] = 0
    print(enemies_matrix)
    print('/n')

# print(perimeter)
print(perimeter, enemies)
