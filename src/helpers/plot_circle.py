import math
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})
plt.grid(color='grey', linestyle='-', linewidth=1)

a = []
b = []
n = 64
for i in range(1, n+1):
    a.append(math.cos(i*2*math.pi/n))
    b.append(math.sin(i*2*math.pi/n))

plt.plot(a, b)  # Line
plt.plot(a, b, 'ro') # Points
plt.show()