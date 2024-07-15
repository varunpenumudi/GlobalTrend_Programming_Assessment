def get_transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # Filling transpose matrix with zeros
    transpose_matrix = []

    for col in range(cols):
        new_row = []

        for row in range(rows):
            new_row.append(matrix[row][col])

        transpose_matrix.append(new_row)

    return transpose_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [12, 5, 6]
    ]
    transpose = get_transpose(matrix)
    # printing transpose matrix
    print("[", *transpose, sep="\n  ")
    print(']')
