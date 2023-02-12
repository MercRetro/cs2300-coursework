def read(file_name):
    # Read a matrix from a file
    with open(file_name, "r") as file:
        matrix = []
        for line in file:
            row = [int(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

def write(file_name, matrix):
    # Write a matrix to a file
    with open(file_name, "w") as file:
        for row in matrix:
            file.write(" ".join(str(x) for x in row) + "\n")

def multiply(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            element = 0
            for k in range(len(B)):
                element += A[i][k] * B[k][j]
            row.append(element)
        result.append(row)
    return result

# Get the names of the input matrices from the user
Mat1_name = input("Enter the name of the first input matrix: ")
Mat2_name = input("Enter the name of the second input matrix: ")

# Read the input matrices from the files
Mat1 = read(Mat1_name + ".txt")
Mat2 = read(Mat2_name + ".txt")

# Check if the matrices can be multiplied
if len(Mat1[0]) != len(Mat2):
    print("Error: the matrices cannot be multiplied because the number of columns in the first matrix is not equal to the number of rows in the second matrix")
else:
    # Calculate the product of the matrices
    result = multiply(Mat1, Mat2)

    # Write the result to an output file
    output = "mgoodwin_p3_out" + Mat1_name[-1] + Mat2_name[-1] + ".txt"
    write(output, result)
