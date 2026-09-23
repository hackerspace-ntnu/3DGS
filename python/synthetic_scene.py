import numpy as np

img_width = 640
img_height = 480

#camera rotation aligned with real world coordinates
R = np.identity(3) 

# we can calculate t using t = -RC where C is the center of the camera position in real life
# no translation here
t= [0,0,0] 



def world_to_cam(R:np.ndarray,t: np.ndarray,point: np.ndarray) -> np.ndarray:
    return R @ point + t

def cam_to_pixels(point:np.ndarray, fx:int, fy:int, cx: int, cy:int) -> np.ndarray: 
    """
    projects a 3D point onto the 2D image plane
    """
    u = fx * point[0]/point[2] -cx
    v = fy * point[1]/point[2] -cy
    return np.array(u,v)



