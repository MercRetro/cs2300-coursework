# Read matrix A and vector b from file
myFile1 = 'pa3_test_input_1.txt'
myFile2 = 'test_input_2.txt'


def my_function(myFile):
    with open(myFile, "r") as f:
        #split lines to read
        line1 = f.readline().split()
        line2 = f.readline().split()

        #get each value
        a11 = float(line1[0])
        a12 = float(line1[1])
        a21 = float(line2[0])
        a22 = float(line2[1])

        #turn values into matrix A
        A = [[a11, a12], [a21, a22]]
        # Read the third number in both lines and turn them into a vector b
        b = [[float(line1[2])], [float(line2[2])]]
        
        trace = a11 + a22
        det = a11*a22 - a12*a21
        discriminant = (trace**2 - 4*det)**0.5
        if discriminant < 0:
            print("No real eigenvalues")
        else: 

            #eigenvales 1 and 2
            lambda1 = (A[0][0] + A[1][1] + ((A[0][0] + A[1][1])**2 - 4*(A[0][0]*A[1][1] - A[0][1]*A[1][0]))**(1/2))/2
            lambda2 = (A[0][0] + A[1][1] - ((A[0][0] + A[1][1])**2 - 4*(A[0][0]*A[1][1] - A[0][1]*A[1][0]))**(1/2))/2
            # Construct the diagonal matrix D
            Lambda = [[lambda1, 0], [0, lambda2]]
            for row in Lambda:
                print("{:.4f} {:.4f}".format(row[0], row[1]))


            # find the eigenvector corresponding to lambda1
            X1 = [A[0][1]/(lambda1 - A[0][0]), 1]
            # normalize X1
            norm1 = (X1[0]**2 + X1[1]**2)**0.5
            X1 = [X1[0]/norm1, X1[1]/norm1]
            # find the eigenvector corresponding to lambda2
            X2 = [A[0][1]/(lambda2 - A[0][0]), 1]
            # normalize X2
            norm2 = (X2[0]**2 + X2[1]**2)**0.5
            X2 = [X2[0]/norm2, X2[1]/norm2]

            R = [[X1[0], X2[0]], [X1[1], X2[1]]]
            for row in R:
                print("{:.4f} {:.4f}".format(row[0], row[1]))

            #get R transpose
            RT = [[R[0][0], R[1][0]], [R[0][1], R[1][1]]]
            #get R by Lambda
            R_lambda = [[R[0][0]*Lambda[0][0]+R[0][1]*Lambda[1][0], R[0][0]*Lambda[0][1]+R[0][1]*Lambda[1][1]],
            [R[1][0]*Lambda[0][0]+R[1][1]*Lambda[1][0], R[1][0]*Lambda[0][1]+R[1][1]*Lambda[1][1]]]
            #get R Lambda R Transpose
            R_lambda_RT = [[R_lambda[0][0]*RT[0][0]+R_lambda[0][1]*RT[1][0], R_lambda[0][0]*RT[0][1]+R_lambda[0][1]*RT[1][1]],
            [R_lambda[1][0]*RT[0][0]+R_lambda[1][1]*RT[1][0], R_lambda[1][0]*RT[0][1]+R_lambda[1][1]*RT[1][1]]]
            for row in R_lambda_RT:
                print("{:.4f} {:.4f}".format(row[0], row[1]))

my_function(myFile1)
my_function(myFile2)
