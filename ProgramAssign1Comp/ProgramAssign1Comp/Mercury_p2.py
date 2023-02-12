def read(file_name):    # Read a matrix from a file
    with open(file_name, "r") as file:
        matrix = []
        for line in file:
            row = [int(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

def sum(Mat1, Mat2):    # Calculate the sum of two matrices
    result = []
    for i in range(len(Mat1)):
        row = []
        for j in range(len(Mat1[0])):
            row.append(Mat1[i][j] + Mat2[i][j])
        result.append(row)
    return result

def write(file_name, matrix):    # Write a matrix to a file
    with open(file_name, "w") as file:
        for row in matrix:
            file.write(" ".join(str(x) for x in row) + "\n")

# Get the names of the input matrices from the user
matrix1_name = input("Enter the name of first matrix (exclude .txt): ")
matrix2_name = input("Enter the name of second matrix (exlude .txt): ")

# Read the input matrices from the files
Mat1 = read(matrix1_name + ".txt")
Mat2 = read(matrix2_name + ".txt")

# Check if the matrices can be summed
if len(Mat1) != len(Mat2) or len(Mat1[0]) != len(Mat2[0]):
    print("Error: the matrices cannot be summed because they have different dimensions")
else:
    # Calculate the sum of the matrices
    result = sum(Mat1, Mat2)

    # Write the result to an output file
    output_name = "mgoodwin_p2_out" + matrix1_name[-1] + matrix2_name[-1] + ".txt"
    write(output_name, result)