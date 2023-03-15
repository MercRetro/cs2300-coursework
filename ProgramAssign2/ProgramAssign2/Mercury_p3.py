#Write a program to determine the linear map used to map a source 
#triangle to a target triangle given the vertices of both triangles. 
#You may use the shortcut method for finding an inverse of a 2x2 matrix in this part.

# Prompt the user to enter the vertices of the source triangle
source = []
for i in range(3):
    point = []
    for j in range(2):
        coord = float(input(f"Enter coordinate ({i+1},{j+1}) of source triangle: "))
        point.append(coord)
    source.append(point)

# Prompt the user to enter the vertices of the target triangle
target = []
for i in range(3):
    point = []
    for j in range(2):
        coord = float(input(f"Enter coordinate ({i+1},{j+1}) of target triangle: "))
        point.append(coord)
    target.append(point)

# Construct the matrix A
A = [[source[0][0], source[1][0], source[2][0]],
     [source[0][1], source[1][1], source[2][1]],
     [1, 1, 1]]

# Construct the matrix B
B = [[target[0][0], target[1][0], target[2][0]],
     [target[0][1], target[1][1], target[2][1]],
     [1, 1, 1]]

# Calculate the inverse of matrix A
det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
if det == 0:
    print("The matrix is not invertible.")
else:
    invA = [[A[1][1]/det, -A[0][1]/det, 0],
        [-A[1][0]/det, A[0][0]/det, 0],
        [(A[1][0]*A[2][1]-A[2][0]*A[1][1])/det, (A[2][0]*A[0][1]-A[0][0]*A[2][1])/det, det]]

    # Calculate the linear map
    linear_map = [[0, 0], [0, 0], [0, 0]]
    for i in range(3):
        for j in range(2):
            for k in range(3):
                linear_map[i][j] += invA[i][k] * B[k][j]

    # Print the linear map
    print("The linear map that maps the source triangle to the target triangle is:")
    for row in linear_map:
        print(row) 