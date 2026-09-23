import numpy as np
import pytest as pyt
from scipy.spatial.transform import Rotation
from python.synthetic_scene import world_to_cam, cam_to_pixels

# Image size
img_width = 640
img_height = 480

# Rotation by 90 degrees in the positive direction around the z-axis
R_90 = Rotation.from_euler("z",90,degrees=True).as_matrix()

# Arbitrary test vector
t_test= np.array([1,2,3]) 

# Cartesian test points
points_world = np.array([
[0.0,  0.0, 3.0],
[ 0.5,  0.0, 4.0],
[-0.5,  0.2, 5.0],])

# calculated 90 degree rotations of test points
points_rotated = np.array([
[0.0, 0.0, 3.0],
[0.0, 0.5, 4.0],
[-0.2, -0.5, 5.0]
])


#focal length in x and y, in this case 500 pixels = 1 unit of measurement.
fx, fy = 500, 500

# where to optical axis intersects the image plane, here at the center of the plane
cx, cy = 320, 240

@pyt.mark.parametrize("point", points_world)
def test_identity(point):
    result = world_to_cam(R=np.identity(3), t=np.array([0,0,0]), point = point)
    assert result==pyt.approx(point)

@pyt.mark.parametrize("point", points_world)
def test_translation(point):
    result = world_to_cam(R=np.identity(3), t=t_test, point = point)
    assert result==pyt.approx(point + t_test)

@pyt.mark.parametrize( "point, point_rotated",zip(points_world, points_rotated))
def test_rotation(point,point_rotated):
    result = world_to_cam(R=R_90, t=np.array([0,0,0]), point = point)
    assert result == pyt.approx(point_rotated)


