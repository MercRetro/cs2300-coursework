def write(filename, result):
    with open(filename, "w") as file:
        file.write(str(result))

Mercury = 7 #rows
Goodwin = 7 #columns
Mat1 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = 1
for i in range(Mercury):
    for j in range(Goodwin):
        Mat1[i][j] = value
        value += 1

Mat2 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = 2
for i in range(Mercury):
    for j in range(Goodwin):
        Mat2[i][j] = value
        value += 3
Mat3 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = 0.2
for j in range(Goodwin):
    for i in range(Mercury):
        Mat3[i][j] = value
        value += 0.2
Rows = 4 #rows
Columns = 6 #columns
Mat4 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = 10
for i in range(Columns):
    for j in range(Rows):
        Mat4[i][j] = value
        value -= 2
Mat5 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = -6
for i in range(Rows):
    for j in range(Columns):
        Mat5[i][j] = value
        value += 1.5
Rows = 4 #rows
Columns = 6 #columns
Mat6 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = -10
for i in range(Rows):
    for j in range(Columns):
        Mat6[i][j] = value
        value += 10


for i in range(len(Mat1[0])):
    transposed_row = []
    for row in Mat1:
        transposed_row.append(row[i])
write("mgoodwin_p6_mat1.txt", transposed_row)

for i in range(len(Mat2[0])):
    transposed_row = []
    for row in Mat2:
        transposed_row.append(row[i])
write("mgoodwin_p6_mat2.txt", transposed_row)

for i in range(len(Mat3[0])):
    transposed_row = []
    for row in Mat3:
        transposed_row.append(row[i])
write("mgoodwin_p6_mat3.txt", transposed_row)

for i in range(len(Mat4[0])):
    transposed_row = []
    for row in Mat4:
        transposed_row.append(row[i])
write("mgoodwin_p6_mat4.txt", transposed_row)

for i in range(len(Mat5[0])):
    transposed_row = []
    for row in Mat5:
        transposed_row.append(row[i])
write("mgoodwin_p6_mat5.txt", transposed_row)

for i in range(len(Mat6[0])):
    transposed_row = []
    for row in Mat6:
        transposed_row.append(row[i])
write("mgoodwin_p6_mat6.txt", transposed_row)