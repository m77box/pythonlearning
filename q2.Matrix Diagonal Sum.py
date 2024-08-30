# Question 2: Matrix Diagonal Sum

def diagonal_sum(matrix, n):
    principal = 0
    secondary = 0
    for i in range(0, n):
        principal += matrix[i][i]
        secondary += matrix[i][n - i - 1]
    print(principal)
    print(secondary)

array = [[1,2,3],[4,8,6],[7,8,100]]
print(diagonal_sum(array, 3))



    # Calculate the primary diagonal sum
    # Calculate the secondary diagonal sum
    # Return the total sum

#
# print(diagonal_sum([1,2,3]))
# print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# Expected: 30 (1 + 5 + 9 + 3 + 5 + 7)


