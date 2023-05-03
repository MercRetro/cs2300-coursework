def is_left_stochastic(matrix):
    n = len(matrix)
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if abs(col_sum - 1) > 1e-6:
            return False
    return True

def power_method(matrix):
    n = len(matrix)
    # initialize the vector with ones
    x = [1.0] * n
    # set the tolerance level for convergence
    tol = 1e-6
    # iterate until convergence is reached
    while True:
        # multiply the vector by the matrix
        y = [sum(matrix[i][j] * x[j] for j in range(n)) for i in range(n)]
        # normalize the result
        norm = max(abs(val) for val in y)
        y = [val / norm for val in y]
        # check for convergence
        if max(abs(y[i] - x[i]) for i in range(n)) < tol:
            return y, norm
        x = y

# read in the matrix from the input file
with open("input_3.txt", "r") as f:
    matrix = []
    for line in f:
        row = [float(val) for val in line.strip().split()]
        matrix.append(row)

with open("p3_output_3.txt", 'w') as n:
# check if the matrix is left stochastic
    if not is_left_stochastic(matrix):
        n.write("Invalid input")
    else:
        # apply the power method to find the dominant eigenvector and eigenvalue
        eigenvector, eigenvalue = power_method(matrix)
        # sort the indices of the eigenvector from highest to lowest rank
        indices = sorted(range(len(eigenvector)), key=lambda i: eigenvector[i], reverse=True)
        # output the eigenvector and sorted indices
        n.write(" ".join("{:.3f}".format(val) for val in eigenvector) + "\n")
        n.write(" ".join(str(index) for index in indices))