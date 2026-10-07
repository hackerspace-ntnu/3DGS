import numpy as np


def world_to_cam(R:np.ndarray,t: np.ndarray,point: np.ndarray) -> np.ndarray:
    return R @ point + t

def cam_to_pixels(point:np.ndarray, fx:int, fy:int, cx: int, cy:int) -> np.ndarray: 
    """
    projects a 3D point onto the 2D image plane
    """
    if point[2]<=0:
        raise ValueError("invalid z-value")
    u = fx * point[0]/point[2] +cx
    v = fy * point[1]/point[2] +cy
    return np.array([u,v])



