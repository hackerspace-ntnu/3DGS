# 3DGS
This is a simple 3D gaussian splatting pipeline project as a part of ShaderGruppa. 


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

## Machine workflow

- Laptop: primary development, NumPy reference implementations, testing, and CPU debugging.
- RTX 3060 Ti desktop: CUDA development and GPU experiments when required.
- University V100/A100: application for access still pending.

## Data

Real datasets are not tracked by Git. See `data/README.md` for the expected local data layout.