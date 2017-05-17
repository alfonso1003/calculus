from viz import *

h = 0.1 # s
g = 9.81 # m / s2
acceleration = numpy.array([0., -g])
initial_speed = 20. # m / s

@show_plot
def trajectory():
    angles = numpy.linspace(20., 70., 6)

    num_steps = 30
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])

    for angle in angles:
        ###Your code here.
        angle_rad = angle * (math.pi / 180.0)
        x[0] = [0,0]
        v[0] = [initial_speed * math.cos(angle_rad), 
                initial_speed * math.sin(angle_rad)]

        for step in range(num_steps):
            x[step + 1] = x[step] + h *  v[step]
            v[step + 1] = v[step] + h * acceleration

        matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    return x, v

trajectory()
