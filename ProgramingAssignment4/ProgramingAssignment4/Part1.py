import numpy as np

def parallel_projection(point, plane_point, plane_normal, projection_direction):
    # Project point onto plane
    d = np.dot(plane_normal, plane_point)
    t = (d - np.dot(plane_normal, point)) / np.dot(plane_normal, projection_direction)
    projected_point = point + t * projection_direction
    return projected_point

def perspective_projection(point, plane_point, plane_normal):
    # Compute projection direction as vector from point to origin
    projection_direction = -point
    # Project point onto plane
    d = np.dot(plane_normal, plane_point)
    t = (d - np.dot(plane_normal, point)) / np.dot(plane_normal, projection_direction)
    projected_point = point + t * projection_direction
    return projected_point

def parse_input_file(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    plane_point = np.array([float(x) for x in lines[0].split()[:3]])
    plane_normal = np.array([float(x) for x in lines[0].split()[3:6]])
    if len(lines[0].split()) == 9:
        projection_direction = np.array([float(x) for x in lines[0].split()[6:]])
    else:
        projection_direction = None
    points = []
    for line in lines[1:]:
        points.extend([np.array([float(x) for x in line.split()[i:i+3]]) for i in range(0, 9, 3)])
    return plane_point, plane_normal, projection_direction, points

def write_output_file(output_file, projected_points):
    with open(output_file, 'w') as f:
        for i in range(0, len(projected_points), 3):
            f.write(' '.join([f'{x:.2f}' for x in projected_points[i]]) + ' ')
            f.write(' '.join([f'{x:.2f}' for x in projected_points[i+1]]) + ' ')
            f.write(' '.join([f'{x:.2f}' for x in projected_points[i+2]]) + '\n')

if __name__ == '__main__':
    # Parse input file
    plane_point, plane_normal, projection_direction, points = parse_input_file('input_1.txt')

    # Project points using parallel projection
    if projection_direction is not None:
        projected_points_parallel = [parallel_projection(p, plane_point, plane_normal, projection_direction) for p in points]
        # Write output file for parallel projection
        write_output_file('p1_output_11.txt', projected_points_parallel)

    # Project points using perspective projection
    projected_points_perspective = [perspective_projection(p, plane_point, plane_normal) for p in points]
    # Write output file for perspective projection
    write_output_file('p1_output_12.txt', projected_points_perspective)



    plane_point, plane_normal, projection_direction, points = parse_input_file('input_2.txt')

    # Project points using parallel projection
    if projection_direction is not None:
        projected_points_parallel = [parallel_projection(p, plane_point, plane_normal, projection_direction) for p in points]
        # Write output file for parallel projection
        write_output_file('p1_output_21.txt', projected_points_parallel)

    # Project points using perspective projection
    projected_points_perspective = [perspective_projection(p, plane_point, plane_normal) for p in points]
    # Write output file for perspective projection
    write_output_file('p1_output_22.txt', projected_points_perspective)

    