import math
import numpy as np

def part1(file1, file2):
    # read input file
    with open(file1, "r") as f:
        lines = f.readlines()

    # process input and compute distances
    distances = []
    for line in lines:
        nums = list(map(float, line.strip().split()))
        point_on_plane = nums[:3]
        normal_vector = nums[3:6]
        point = nums[6:]
    
        # compute constants of the plane equation
        A, B, C = normal_vector
        D = -(A * point_on_plane[0] + B * point_on_plane[1] + C * point_on_plane[2])
    
        # compute distance between point and plane
        distance = abs(A * point[0] + B * point[1] + C * point[2] + D) / math.sqrt(A**2 + B**2 + C**2)
        distances.append(distance)

    # write output file
    with open(file2, "w") as f:
        for distance in distances:
            f.write(f"{distance}\n")
part1("input_1.txt", "p2_output_11.txt")
part1("input_2.txt", "p2_output_12.txt")


#part 22
def line_plane_intersection(line_start, line_end, plane_point, plane_normal):
    # Compute the intersection point between a line and a plane
    line_direction = line_end - line_start
    denominator = np.dot(line_direction, plane_normal)
    if abs(denominator) < 1e-6:
        # Line is parallel to the plane
        return None
    t = np.dot(plane_point - line_start, plane_normal) / denominator
    intersection_point = line_start + t * line_direction
    return intersection_point

def is_point_inside_triangle(point, triangle):
    # Check if a point is inside a triangle
    v0 = triangle[0]
    v1 = triangle[1]
    v2 = triangle[2]
    u = v1 - v0
    v = v2 - v0
    n = np.cross(u, v)
    w = point - v0
    gamma = np.dot(np.cross(u, w), n) / np.dot(n, n)
    beta = np.dot(np.cross(w, v), n) / np.dot(n, n)
    alpha = 1 - gamma - beta
    return (0 <= alpha <= 1) and (0 <= beta <= 1) and (0 <= gamma <= 1) and (abs(alpha + beta + gamma - 1) < 1e-6)

def part2(file1, file2):
    # Read the input file
    with open(file1, 'r') as f:
        lines = f.readlines()

    # Parse the first line to get the line coordinates
    line_start = np.array([float(lines[0].split()[0]), float(lines[0].split()[1]), float(lines[0].split()[2])])
    line_end = np.array([float(lines[0].split()[3]), float(lines[0].split()[4]), float(lines[0].split()[5])])

    # Parse the triangles coordinates
    triangles = []
    for line in lines[1:]:
        vertices = [np.array([float(line.split()[i]), float(line.split()[i+1]), float(line.split()[i+2])]) for i in range(0, 9, 3)]
        triangles.append(vertices)

    # Check if each triangle intersects with the line
    intersections = []
    for i in range(len(triangles)):
        triangle = triangles[i]
        plane_point = triangle[0]
        plane_normal = np.cross(triangle[1] - triangle[0], triangle[2] - triangle[0])
        intersection_point = line_plane_intersection(line_start, line_end, plane_point, plane_normal)
        if intersection_point is not None and is_point_inside_triangle(intersection_point, triangle):
            intersections.append(intersection_point)
        else:
            intersections.append("Does not intersect.")

    # Write the output file
    with open(file2, 'w') as f:
        for intersection in intersections:
            f.write(str(intersection) + "\n")

part2("input_1.txt", "p2_output_21.txt")
part2("input_2.txt", "p2_output_22.txt")
