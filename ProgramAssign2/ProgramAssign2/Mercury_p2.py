#Given a 2x2 matrix (you will need to prompt the user to enter),
#first determine if an inverse to the matrix exists and if so, 
#calculate the inverse using gauss elimination.  

# Prompt the user to enter the 2x2 matrix
# Prompt the user to enter a 2x2 matrix
matrix = []
for i in range(2):
    row = []
    for j in range(2):
        elem = float(input(f"Enter element ({i+1},{j+1}): "))
        row.append(elem)
    matrix.append(row)

# Calculate the determinant of the matrix
det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Check if the matrix has an inverse
if det == 0:
    print("The matrix does not have an inverse.")
else:
    # Apply Gauss elimination method to find the inverse
    inv_matrix = [[matrix[1][1]/det, -matrix[0][1]/det],
                  [-matrix[1][0]/det, matrix[0][0]/det]]
    
    # Print the inverse matrix
    print("The inverse of the matrix is:")
    for row in inv_matrix:
        print(row)