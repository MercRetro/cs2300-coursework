import math
from pickle import TRUE
import numpy as np
myFile1 = '3D_test_input_1.txt'
myFile2 = 'pa3_test_input_1.txt'

def read_lines(myFile):
    with open(myFile, 'r') as f:
        lines = f.readlines()
        x = 0
        for line in lines:
            x = x + 1
    return x 
    
def read_points(myFile):
    with open(myFile, 'r') as f:
        lines = f.readlines()
        points = []
        for line in lines:
            coords = line.strip().split()
            point = [float(coord) for coord in coords]
            points.append(point)
        return points

def compute_area(points):

    x1, x2, x3 = points[0][:3]
    y1, y2, y3 = points[1][:3]

    return abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)) / 2

def compute_distance(points, linent):
    if lineCnt == 2:
        # 2D case

        x1, x2, x3 = points[0]
        y1, y2, y3 = points[1]

        a = y1 - y2
        b = x2 - x1
        c = x1*y2 - x2*y1
        d = math.sqrt(a**2 + b**2)
        return abs(a*x3 + b*y3 + c) / d
    else:
        # 3D case
        x1, x2, x3 = points[0]
        y1, y2, y3 = points[1]
        z1, z2, z3 = points[2]


        a = y1*(z2-z3) + y2*(z3-z1) + y3*(z1-z2)
        b = z1*(x2-x3) + z2*(x3-x1) + z3*(x1-x2)
        c = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
        d = -x1*(y2*z3-y3*z2) - x2*(y3*z1-y1*z3) - x3*(y1*z2-y2*z1)
        e = math.sqrt(a**2 + b**2 + c**2)
        return abs(a*x3 + b*y3 + c*z3 + d) / e

lineCnt = read_lines(myFile1)
points = read_points(myFile1)
area = compute_area(points)
distance = compute_distance(points, lineCnt)
print("{:.4f}".format(area))
print("{:.4f}".format(distance))

lineCnt = read_lines(myFile2)
points = read_points(myFile2)
area = compute_area(points)
distance = compute_distance(points, lineCnt)

print("{:.4f}".format(area))
print("{:.4f}".format(distance))
