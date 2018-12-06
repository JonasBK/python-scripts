# Expected and actual coverage of Hellman tables over limited AES

import math
import matplotlib.pyplot as plt
import csv
plt.rcParams.update({'font.size': 22})
plt.grid(color='grey', linestyle='-', linewidth=1)
points_file = open("../data/hellman_points.csv")

key_size = 24.0
N = 2**key_size
no_tables = 2.0**8
graph = []
rainbow_points = []

for row in csv.reader(points_file):
    for e in row:
        if e: 
            rainbow_points.append(int(e)/N)

def ph(m, t):
    return 1 - math.exp(-math.sqrt(2*m*no_tables**2/2**key_size) * (math.exp(math.sqrt(2*m*t**2/2**key_size)) - 1) / (math.exp(math.sqrt(2*m*t**2/2**key_size)) + 1))

for i in range(17):
    next_ph = ph(2**i, 2**(16-i))
    graph.append(next_ph)

plt.plot(graph)
plt.xlabel('x \n (m = 2^x, t = 2^(16-x))')
plt.ylabel('P_H')
plt.show()

plt.grid(color='grey', linestyle='-', linewidth=1)

plt.plot(rainbow_points)
plt.xlabel('Number of tables')
plt.ylabel('Coverage')
plt.show()

