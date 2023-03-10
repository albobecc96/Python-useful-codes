import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def random_walk_3d(num_steps):
    # genera i passi casuali
    steps = np.random.randn(num_steps, 3)
    # calcola le posizioni successive
    positions = np.cumsum(steps, axis=0)
    return positions

# numero di passi del random walk
num_steps = 1000

# esegui il random walk
positions = random_walk_3d(num_steps)

# disegna la traiettoria del random walk
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[:,0], positions[:,1], positions[:,2])
plt.show()