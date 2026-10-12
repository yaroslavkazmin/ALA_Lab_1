import math
import  numpy as np
import matplotlib.pyplot as plt

lynx = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]]).T

def plot_display (X, title="fig"):
    plt.plot(X[0, :], X[1, :])
    plt.title(title)
    plt.show()

def stretch(X, a, b):
    X_copy = X.copy()
    A = np.array([[a, 0], [0, b]])
    transformed = A @ X_copy
    print(f"stretched \n {A}")
    return transformed

def shear(X, a, b):
    X_copy = X.copy()
    A = np.array([[1, a], [b, 1]])
    transformed = A @ X_copy
    print(f"sheared \n {A}")
    return transformed

def reflection(X, a, b):
    X_copy = X.copy()
    A = np.array([[(a**2-b**2)/(a**2+b**2), 2*a*b/(a**2+b**2)], [2*a*b/(a**2+b**2), (b**2-a**2)/(a**2+b**2)]])
    transformed = A @ X_copy
    print(f"reflection \n {A}")
    return transformed

def rotation(X, rad):
    X_copy = X.copy()
    r = math.radians(rad)
    A = np.array([[math.cos(r), 0-math.sin(r)], [math.sin(r), math.cos(r)]])
    transformed = A @ X_copy
    print(f"rotation \n {A}")
    return transformed

# plot_display(lynx)
#
# lynx_stratched = stretch(lynx, 2, 0.25)
# plot_display(lynx_stratched)
#
# lynx_sheared = shear(lynx, 2, 0.3)
# plot_display(lynx_sheared)
#
# lynx_reflection = reflection(lynx, 1, 1)
# plot_display(lynx_reflection)
#
# lynx_rotated = rotation(lynx, math.radians(45))
# plot_display(lynx_rotated)

str_she_rot = rotation(shear(stretch(lynx, 1.5, 0.5), 1.5, 0.5), 90)
plot_display(str_she_rot)

she_rot_str = stretch(rotation(shear(lynx, 1.5, 0.5), 90), 1.5, 0.5)
plot_display(she_rot_str)

rot_str_she = shear(stretch(rotation(lynx, 90), 1.5, 0.5), 1.5, 0.5)
plot_display(rot_str_she)