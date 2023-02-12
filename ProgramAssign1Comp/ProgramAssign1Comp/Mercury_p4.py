import matplotlib.pyplot as plt

def write(filename, result):
    with open(filename, "w") as file:
        file.write(str(result))


vectors = [[-1, -2], [-3, 3], [2, -1], [3, 1], [1, 3]]

for vector in vectors:
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('5 Vectors in Standard Position')
plt.show()



def dotp(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result

vector_r = [-1, -2]
vector_s = [-3, 3]
vector_u = [2, -1]
vector_v = [3, 1]
vector_w = [1, 3]

result = dotp(vector_r, vector_s)
write("mgoodwin_p4_rs.txt", result)

result = dotp(vector_u, vector_v)
write("mgoodwin_p4_uv.txt", result)

result = dotp(vector_s, vector_v)
write("mgoodwin_p4_sv.txt", result)