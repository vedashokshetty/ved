# Function defining the differential equation dy/dx = (y - x)^2
def f(x, y):
    return (y - x) ** 2
x0 = 0
y0 = 0
h = 0.1
n_steps = 7
x_values = [x0]
y_values = [y0]

for i in range(n_steps):

    x_next = x_values[-1] + h
    y_next = y_values[-1] + h * f(x_values[-1], y_values[-1])
    x_values.append(x_next)
    y_values.append(y_next)
print("Step\t x\t\t y")
for i in range(len(x_values)):
    print(f"{i}\t {x_values[i]:.2f}\t {y_values[i]:.6f}")
