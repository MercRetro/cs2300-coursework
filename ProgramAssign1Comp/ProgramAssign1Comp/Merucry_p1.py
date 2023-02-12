Mercury = 7 #rows
Goodwin = 7 #columns
Mat1 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = 1
for i in range(Mercury):
    for j in range(Goodwin):
        Mat1[i][j] = value
        value += 1
with open("mgoodwin_mat1.txt", "w") as f:
    for row in Mat1:
        f.write(" ".join(str(x) for x in row) + "\n")


Mat2 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = 2
for i in range(Mercury):
    for j in range(Goodwin):
        Mat2[i][j] = value
        value += 3
with open("mgoodwin_mat2.txt", "w") as f:
    for row in Mat2:
        f.write(" ".join(str(x) for x in row) + "\n")


Mat3 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = 0.2
for j in range(Goodwin):
    for i in range(Mercury):
        Mat3[i][j] = value
        value += 0.2
with open("mgoodwin_mat3.txt", "w") as f:
    for row in Mat3:
        f.write(" ".join(str(x) for x in row) + "\n")


Rows = 4 #rows
Columns = 6 #columns
Mat4 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = 10
for i in range(Columns):
    for j in range(Rows):
        Mat4[i][j] = value
        value -= 2
with open("mgoodwin_mat4.txt", "w") as f:
    for row in Mat4:
        f.write(" ".join(str(x) for x in row) + "\n")


Mat5 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = -6
for i in range(Rows):
    for j in range(Columns):
        Mat5[i][j] = value
        value += 1.5
with open("mgoodwin_mat5.txt", "w") as f:
    for row in Mat5:
        f.write(" ".join(str(x) for x in row) + "\n")


Rows = 4 #rows
Columns = 6 #columns
Mat6 = [[0 for i in range(Mercury)] for j in range(Goodwin)]
value = -10
for i in range(Rows):
    for j in range(Columns):
        Mat6[i][j] = value
        value += 10
with open("mgoodwin_mat6.txt", "w") as f:
    for row in Mat6:
        f.write(" ".join(str(x) for x in row) + "\n")