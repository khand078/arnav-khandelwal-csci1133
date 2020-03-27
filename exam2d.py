def square_diagonal(test_matrix):
    for i in range(len(test_matrix)):
        for j in range(len(test_matrix)):
            test_matrix[i][j] = test_matrix[i**2][j**2]
    return test_matrix
