# Read matrix A and vector b from file
myFile1 = 'pa3_test_input_1.txt'
myFile2 = 'test_input_2.txt'


def my_function(myFile):
        # Read the input file
        with open(myFile, 'r') as f:
            # Read the first line and convert the first two numbers into a 2x2 matrix
            line1 = f.readline().split()
            line2 = f.readline().split()
            A = [[float(line1[0]), float(line1[1])], [float(line2[0]), float(line2[1])]]
            # Read the third number in both lines and turn them into a vector b
            b = [[float(line1[2])], [float(line2[2])]]

            # Find the determinant of A
            det = A[0][0] * A[1][1] - A[0][1] * A[1][0]

            # Check if the system is inconsistent or underdetermined
            if det == 0 and b[0][0] != b[1][0]:
                print("System inconsistent")
            elif det == 0 and b[0][0] == b[1][0]:
                print("System underdetermined")
            else:
                # Find the solution for x
                invA = [[A[1][1] / det, -A[0][1] / det], [-A[1][0] / det, A[0][0] / det]]
                x = [[round(invA[0][0] * b[0][0] + invA[0][1] * b[1][0], 4)], [round(invA[1][0] * b[0][0] + invA[1][1] * b[1][0], 4)]]
                # Output the result
                print(x[0][0], x[1][0])

my_function(myFile1)
my_function(myFile2)
