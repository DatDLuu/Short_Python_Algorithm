#given a matrix
#given an array of rows and columns to delete
#create submatrix


def subMatrix (matrix,rows_to_del,columns_to_del):

    if not rows_to_del and not columns_to_del:
        return matrix
    return [[matrix[i][j] for j in range(len(matrix[0])) if j not in columns_to_del]
                          for i in range(len(matrix)) if i not in rows_to_del]