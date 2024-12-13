def multiplying_matrices(matrix1, matrix2):
    rows_1 = len(matrix1)
    cols_1 = len(matrix1[0])
    cols_2 = len(matrix2[0])



    if rows_1 != cols_2:
        return "Error, number of rows in matrix1 must be equal to number of colums in matrix2"
    else:

        outcome_matrix = [[0 for _ in range(rows_1)] for _ in range(cols_2)]

        for i in range(rows_1):
            for j in range(cols_2):
                for k in range(cols_1):
                    outcome_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

        return outcome_matrix


example_matrix1 = [[1, 2, 3], [2, 3, 4]]
example_matrix2 = [[1, 2], [3, 4], [5, 6]]

print(multiplying_matrices(example_matrix1, example_matrix2))