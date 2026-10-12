import math
import  numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def read_off(filename):
    with open(filename, 'r') as f:
        if 'OFF' != f.readline().strip():
            raise ValueError('Not a valid OFF header')
        n_verts, n_faces, _ = map(int, f.readline().strip().split())
        vertices = [list(map(float, f.readline().strip().split())) for _ in range(n_verts)]
        faces = [list(map(int, f.readline().strip().split()))[1:] for _ in range(n_faces)]
    return np.array(vertices), faces

def plot_off(vertices, faces, title="3D Model"):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    mesh = Poly3DCollection([vertices[face] for face in faces], alpha=0.3, edgecolor='k')
    ax.add_collection3d(mesh)

    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='b', s=1)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    plt.title(title)
    plt.show()

def rotate_xy(X, rad):
    X_copy = X.copy()
    r = math.radians(rad)
    A = np.array([[math.cos(r), 0-math.sin(r), 0], [math.sin(r), math.cos(r), 0], [0, 0, 1]])
    transformed = (A @ X_copy.T).T
    print(f"roation xy \n {A}")
    return transformed

def rotate_yz(X, rad):
    X_copy = X.copy()
    r = math.radians(rad)
    A = np.array([[1, 0, 0], [0, math.cos(r), 0-math.sin(r)], [0, math.sin(r), math.cos(r)]])
    transformed = (A @ X_copy.T).T
    print(f"roation yz \n {A}")
    return transformed

def rotate_xz(X, rad):
    X_copy = X.copy()
    r = math.radians(rad)
    A = np.array([[math.cos(r), 0, 0 - math.sin(r)], [0, 1, 0], [math.sin(r), 0, math.cos(r)]])
    transformed = (A @ X_copy.T).T
    print(f"roation xz \n {A}")
    return transformed

vertices, faces = read_off("file.off")
plot_off(vertices, faces, title="3D Model")

rotated = rotate_xy(vertices, 90)
plot_off(rotated, faces, title="Rotated Model")

rotated_3x = rotate_xz(rotate_yz(rotate_xy(vertices, 45), 45), 45)
plot_off(rotated_3x, faces, title="Rotated Model 3X")