#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        # for i in x:
        #     print(i, end=" ")
        # print("\n")
        print(" ".join(x))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
