# Expected and actual coverage of Rainbow table over limited AES 

import matplotlib.pyplot as plt
import csv
plt.rcParams.update({'font.size': 22})
plt.grid(color='grey', linestyle='-', linewidth=1)
points_file = open("../data/rainbow_points.dat")

key_size = 24.0
N = 2**key_size
graph = []
rainbow_points = []

for row in csv.reader(points_file):
    rainbow_points.append(int(row[0])/N)

key_size = 24.0
m_set = 2**8
graph = []

def pr(m, t):
    return 1 - (2/(2+(m*t**2/2**key_size)))**2

for t in range(1200):
    next_pr = pr(m_set, t)
    if t == 1000:
        print next_pr
    graph.append(next_pr)

plt.plot(graph)
plt.xlabel('t')
plt.ylabel('P_R')
plt.show()

plt.grid(color='grey', linestyle='-', linewidth=1)

plt.plot(rainbow_points)
plt.xlabel('Rows')
plt.ylabel('Coverage')
plt.show()