import numpy as np
from parse import parse
from matplotlib import pyplot as plt

posx = lambda particle: particle[0][0]
posy = lambda particle: particle[0][1]
velx = lambda particle: particle[1][0]
vely = lambda particle: particle[1][1]

def get_size(particles):
    xmin = min(map(posx, particles))
    xmax = max(map(posx, particles))
    ymin = min(map(posy, particles))
    ymax = max(map(posy, particles))

    return (
        max(map(posx, particles)) - min(map(posx, particles)),
        max(map(posy, particles)) - min(map(posy, particles)),
    )

total_steps = 0
def advance(particles, steps):
    global total_steps
    for particle in particles:
        particle[0][0] += velx(particle) * steps
        particle[0][1] += vely(particle) * steps
    total_steps += steps

def minimize(particles):
    speed = 1
    while True:
        width_before, height_before = get_size(particles)
        size_before = width_before * height_before

        advance(particles, speed)

        width_after, height_after = get_size(particles)
        size_after = width_after * height_after
        
        if size_before < size_after:
            advance(particles, -1)
            return

        # Tune the speed
        bump = int(-np.log((size_before - size_after) / size_after))
        if bump > 3:
            speed += bump
        elif speed > 1:
            speed -= 1


def get_field(particles):
    width, height = get_size(particles)
    field = np.zeros((width + 5, height + 5))

    for particle in particles:
        field[posx(particle) - min(map(posx, particles)) + 1, posy(particle) - min(map(posy, particles)) + 1] = 1
    return field

def show_field(particles):
    plt.figure()
    plt.imshow(np.transpose(get_field(particles)))
    plt.show()

# Main program

particles = [parse("position=<{}, {}> velocity=<{}, {}>", line.strip()) for line in open("2018day10.data")]
particles = [[[int(posx), int(posy)], [int(velx), int(vely)]] for posx, posy, velx, vely in particles]

minimize(particles)
show_field(particles)
print(total_steps)