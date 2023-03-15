#Write a program to find the eigenvalues and eigenvectors of a 2x2 matrix 
#(you will need to prompt the user to enter). 
#Output on the display the characteristic equation, the values of lambda and the dominate eigenvalue.

# Prompt the user to enter the 2x2 matrix
print("Enter the values of the 2x2 matrix: ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

# Calculate the determinant and trace of the matrix
det = a*d - b*c
tr = a + d

# Calculate the eigenvalues
lam1 = tr/2 + ((tr/2)**2 - det)**0.5
lam2 = tr/2 - ((tr/2)**2 - det)**0.5

# Calculate the eigenvectors
if b != 0:
    v1 = [lam1 - d, b]
    v2 = [lam2 - d, b]
else:
    v1 = [b, lam1 - a]
    v2 = [b, lam2 - a]

# Normalize the eigenvectors
norm1 = (v1[0]**2 + v1[1]**2)**0.5
norm2 = (v2[0]**2 + v2[1]**2)**0.5
v1 = [v1[0]/norm1, v1[1]/norm1]
v2 = [v2[0]/norm2, v2[1]/norm2]

# Output the results
print("\nThe characteristic equation is: L^2 -", tr, "L +", det, "= 0")
print("The eigenvalues are: Lamda1 =", lam1, "and Lamda2 =", lam2)
if abs(lam1) > abs(lam2):
    print("The dominant eigenvalue is L1 =", lam1)
    print("The corresponding eigenvector is:", v1)
else:
    print("The dominant eigenvalue is L2 =", lam2)
    print("The corresponding eigenvector is:", v2)