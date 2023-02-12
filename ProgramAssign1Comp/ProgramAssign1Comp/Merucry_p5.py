import matplotlib.pyplot as plt

def write(filename, result):
    with open(filename, "w") as file:
        file.write(str(result))


vector_r = [-1, -2]
vector_s = [-3, 3]
vector_u = [2, -1]
vector_v = [3, 1]
vector_w = [1, 3]

vector_rs= [x1 + x2 for x1, x2 in zip(vector_r, vector_s)]
vector_sw= [x1 + x2 for x1, x2 in zip(vector_s, vector_w)]
vector_uv= [x1 + x2 for x1, x2 in zip(vector_u, vector_v)]


vectors = [vector_rs, vector_sw, vector_uv]
for vector in vectors:
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('5 Vectors in Standard Position')
plt.show()
