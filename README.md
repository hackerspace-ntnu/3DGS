# 3DGS
This is a simple 3D gaussian splatting pipeline project as a part of ShaderGruppa. 

This is a simple 3D Gaussian Splatting pipeline project as a part of ShaderGruppa.

## Mathematical conventions

- Vectors are column vectors.
- World to camera:
  `p_cam = R p_world + t`
- Perspective projection:
  `u = fx * x / z + cx`
  `v = fy * y / z + cy`
- Angles are measured in radians.
- Quaternion order: `(w, x, y, z)`.
- Image origin: top-left.
- Image x-axis increases to the right.
- Image y-axis increases downward.
- Colors are represented as floating-point RGB values in `[0, 1]`.