#=================================================================================================================================
from random import uniform
from math import sqrt
#=================================================================================================================================
max_iterations = 20 # You can increase this value to increase the number of attempts of the algorithm to find the optimal solution.
#=================================================================================================================================
def ObjectiveFunction(p):
    # Measures the current particle's status and returns it.
    return sqrt(p.position_x**2 + p.position_y**2)
#=================================================================================================================================
class Particle:
    def __init__(self, position_x, position_y):
        # Particle class for maintaining particle properties.
        # Note that the amount of w, c1, c2 is considered fixed but can be changed.
        self.position_x = position_x
        self.position_y = position_y
        self.past_position_x = position_x
        self.past_position_y = position_y
        self.personal_best_position_x = self.position_x
        self.personal_best_position_y = self.position_y
        self.objective = ObjectiveFunction(self)
        self.personal_best_objective = self.objective
        self.personal_w  = 0.01
        self.personal_c1 = 0.05
        self.personal_c2 = 0.05
#=================================================================================================================================
particels = [] 
# Create a list of particles and add 12 hypothetical points to it.
particels.append(Particle(+50, +50))
particels.append(Particle(+50, -50))
particels.append(Particle(-50, +50))
particels.append(Particle(-50, -50))
particels.append(Particle(+75, +75))
particels.append(Particle(+75, -75))
particels.append(Particle(-75, +75))
particels.append(Particle(-75, -75))
particels.append(Particle(0,   +75))
particels.append(Particle(0,   -75))
particels.append(Particle(+75,   0))
particels.append(Particle(-75,   0))
#=================================================================================================================================
def GlobalBest():
    # Finds and returns the particle with the best memory among all particles.
    result = particels[0]
    for p in particels:
        if p.objective < result.objective:
            result = p
    return result
#=================================================================================================================================
def ParticelsMove(p):
    # Updates the next position of a particle based on the PSO algorithm.
    p.position_x += (p.personal_w * (p.past_position_x - p.position_x))\
    +(p.personal_c1 * uniform(0, 1) * (p.personal_best_position_x - p.position_x))\
    +(p.personal_c2 * uniform(0, 1) * (global_best.position_x - p.position_x))

    p.position_y += (p.personal_w * (p.past_position_y - p.position_y))\
    +(p.personal_c1 * uniform(0,1) * (p.personal_best_position_y - p.position_y))\
    +(p.personal_c2 * uniform(0,1) * (global_best.position_y - p.position_y))

    p.objective = ObjectiveFunction(p)
    
    if p.objective < p.personal_best_objective:
        p.personal_best_objective = p.objective
#=================================================================================================================================
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
#=================================================================================================================================
distances = [[(x**2 + y**2) for x in range(-100, 100, 4)]
                            for y in range(-100, 100, 4)]
cmap = plt.get_cmap('summer')
norm = plt.Normalize(vmin=0, vmax=max(map(max, distances)))

# Create a visually appealing plot to display the output.
plt.imshow(distances, extent=[-100, 100, -100, 100], cmap=cmap, origin='lower', norm=norm)
#=================================================================================================================================
for i in range(max_iterations):
    global_best = GlobalBest()
    plt.clf()
    for p in particels:
        if p == global_best:
            continue
        ParticelsMove(p)
        plt.imshow(distances, extent=[-100, 100, -100, 100], cmap=cmap, origin='lower', norm=norm)
        plt.scatter(p.position_x, p.position_y, color='black', marker='o', s=10)
    
    # Display the updated particle positions and the global best in the output.
    plt.imshow(distances, extent=[-100, 100, -100, 100], cmap=cmap, origin='lower', norm=norm)
    plt.scatter(global_best.position_x, global_best.position_y, color='red', marker='o', s=10)
    plt.gca().xaxis.set_major_formatter(NullFormatter())
    plt.gca().yaxis.set_major_formatter(NullFormatter())
    plt.grid(True, color='black', zorder=-1)
    plt.title(label = f"GLOBAL BEST OBJECTIVE: {global_best.objective:f}", pad = 20)
    plt.pause(1) #You can modify this value to control particle speed.
plt.show()
#=================================================================================================================================