def derivative(x, f):
    h = 1./10000000.
    rise = f(x + h) - f(x)
    run = h
    slope = rise / run
    return slope

def integral(x_1, x_2, f):
    x_1 = float(x_1)
    x_2 = float(x_2)
    width = (x_2 - x_1) / 1000000.
    sum = 0
    for i in xrange(1000000):
        height = f(x_1 + i * width)
        area = height * width
        sum += area
    return sum

def square(x):
    return x**2

print derivative(2, square) # 4.00000009115
print integral(0, 1, square) # 0.333332833333

print derivative(2, lambda x: x**3) # 12.0000005843
print integral(0, 1, lambda x: x**3) # 0.2499995
