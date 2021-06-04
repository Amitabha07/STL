import trimesh
import numpy as np
from scipy.spatial.transform import Rotation

pi = np.pi
class MoveSTL():
    def __init__(self, file_path):
        self.mesh = trimesh.load(file_path)

    def resize(self, ratio=0.001):
        self.mesh.vertices *= ratio

    def move(self, x, y, z):
        self.mesh.vertices[:, 0] += x
        self.mesh.vertices[:, 1] += y
        self.mesh.vertices[:, 2] += z

    def rotate(self, wx, wy, wz):
        R = Rotation.from_rotvec(np.array([wx*pi/180, wy*pi/180, wz*pi/180]))
        r = R.as_matrix()
        T = np.identity(4)
        T[:3, :3] = r
        self.mesh.apply_transform(T)

    
