#Write a program to convert between implicit and parametric equations of a line. 
#You should ask the user which form they will be entering, prompt them to enter 
#the specific values for the chosen equation, and then display the corresponding converted equation.

# Prompt the user for the form of the equation
type = input("Enter I for implicit, P for parametric: ")

# If the user enters an invalid equation type, display an error message and exit the program
if type != "I" and type != "P":
    print("Invalid equation type. Please enter 'I' or 'P'.")
    exit()

# If the user enters an implicit equation, prompt them to enter the values of A, B, and C
if type == "I":
    A = float(input("Value of A: "))
    B = float(input("Value of B: "))
    C = float(input("Value of C: "))

    # Convert the implicit equation to parametric form
    if B != 0:
        slope = -A / B
        y_int = -C / B
        print("The parametric equation is: x = t, y = ", slope, "t + ", y_int)
    else:
        print("The equation is not in standard form, please try again with valid values")

# If the user enters a parametric equation, prompt them to enter the values of x1, y1, m, and t
if type == "P":
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    m = float(input("Enter m: "))
    t = float(input("Enter t: "))

    # Convert the parametric equation to implicit form
    A = m
    B = -1
    C = y1 - m * x1
    print("The implicit equation is: ", A, "x + ", B, "y + ", C, " = 0")