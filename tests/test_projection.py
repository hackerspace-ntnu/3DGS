import numpy as np
import pytest as pyt
from scipy.spatial.transform import Rotation
from python.synthetic_scene import world_to_cam, cam_to_pixels

# Image size
img_width = 640
img_height = 480

# Rotation by 90 degrees in the positive direction around the z-axis
R_90 = Rotation.from_euler("z", 90, degrees=True).as_matrix()

# Arbitrary translation vector used for testing
t_test = np.array([1, 2, 3])

# Cartesian test points in world coordinates
points_world = np.array([
    [0.0, 0.0, 3.0],
    [0.5, 0.0, 4.0],
    [-0.5, 0.2, 5.0],
])

# Expected positions after a 90 degree rotation around the z-axis
points_rotated = np.array([
    [0.0, 0.0, 3.0],
    [0.0, 0.5, 4.0],
    [-0.2, -0.5, 5.0],
])

# Focal lengths in pixel units
fx, fy = 500, 250

# Principal point, here chosen as the center of the image
cx, cy = img_width/2, img_height/2

# Camera-space point on the optical axis
point_optical_axis = np.array([0.0, 0.0, 3.0])

# Camera-space points displaced horizontally and expected pixel coordinates
points_horizontal = np.array([
    [1.0, 0.0, 5.0],
    [-1.0, 0.0, 5.0],
])

expected_horizontal_pixels = np.array([
    [420, 240],
    [220, 240],
])

# Camera-space point displaced vertically and expected pixel coordinate
point_vertical = np.array([0.0, 1.0, 5.0])
expected_vertical_pixel = np.array([320, 290])

# Camera-space points with equal x but different depths
points_depth = np.array([
    [1.0, 0.0, 5.0],
    [1.0, 0.0, 10.0],
])

expected_depth_pixels = np.array([
    [420, 240],
    [370, 240],
])

# Camera-space points with invalid depth
points_invalid_depth = np.array([
    [1.0, 0.0, 0.0],
    [1.0, 0.0, -1.0],
])

# Expected values for the full world-to-pixel pipeline test
point_world_full_test = np.array([1, 1, 5])
point_cam_full_test = np.array([0, 3, 8])
expected_pixel_full_test = np.array([320, 333.75])


# world to cam tests:

@pyt.mark.parametrize("point", points_world)
def test_identity(point):
    result = world_to_cam(
        R=np.identity(3),
        t=np.array([0, 0, 0]),
        point=point,
    )
    assert result == pyt.approx(point)


@pyt.mark.parametrize("point", points_world)
def test_translation(point):
    result = world_to_cam(
        R=np.identity(3),
        t=t_test,
        point=point,
    )
    assert result == pyt.approx(point + t_test)


@pyt.mark.parametrize(
    "point, point_rotated",
    zip(points_world, points_rotated),
)
def test_rotation(point, point_rotated):
    result = world_to_cam(
        R=R_90,
        t=np.array([0, 0, 0]),
        point=point,
    )
    assert result == pyt.approx(point_rotated)


# cam to pixels tests:

@pyt.mark.parametrize("point_cam", [point_optical_axis])
def test_optical_axis_proj(point_cam):
    result = cam_to_pixels(
        point=point_cam,
        fx=fx,
        fy=fy,
        cx=cx,
        cy=cy,
    )
    assert result == pyt.approx((cx, cy))


@pyt.mark.parametrize(
    "point_cam, expected_pixel",
    zip(points_horizontal, expected_horizontal_pixels),
)
def test_horizontal_displacement(point_cam, expected_pixel):
    result = cam_to_pixels(
        point=point_cam,
        fx=fx,
        fy=fy,
        cx=cx,
        cy=cy,
    )
    assert result == pyt.approx(expected_pixel)


@pyt.mark.parametrize(
    "point_cam, expected_pixel",
    [(point_vertical, expected_vertical_pixel)],
)
def test_vertical_displacement(point_cam, expected_pixel):
    result = cam_to_pixels(
        point=point_cam,
        fx=fx,
        fy=fy,
        cx=cx,
        cy=cy,
    )
    assert result == pyt.approx(expected_pixel)


@pyt.mark.parametrize(
    "point_cam, expected_pixel",
    zip(points_depth, expected_depth_pixels),
)
def test_depth_displacement(point_cam, expected_pixel):
    result = cam_to_pixels(
        point=point_cam,
        fx=fx,
        fy=fy,
        cx=cx,
        cy=cy,
    )
    assert result == pyt.approx(expected_pixel)


@pyt.mark.parametrize("point_cam", points_invalid_depth)
def test_invalid_depth(point_cam):
    with pyt.raises(ValueError, match="invalid z-value"):
        cam_to_pixels(
            point=point_cam,
            fx=fx,
            fy=fy,
            cx=cx,
            cy=cy,
        )


@pyt.mark.parametrize(
    "point_world, t, R, point_cam, expected_pixel",
    [
        (
            point_world_full_test,
            t_test,
            R_90,
            point_cam_full_test,
            expected_pixel_full_test,
        )
    ],
)
def test_full_pipeline(point_world, t, R, point_cam, expected_pixel):
    p_cam = world_to_cam(
        R=R,
        t=t,
        point=point_world,
    )

    result = cam_to_pixels(
        point=p_cam,
        fx=fx,
        fy=fy,
        cx=cx,
        cy=cy,
    )

    assert p_cam == pyt.approx(point_cam)
    assert result == pyt.approx(expected_pixel)