# ArmBot — 6‑DOF ROS 2 Manipulator

A compact, easy-to-debug 6‑degree-of-freedom manipulator designed for ROS 2 workflows and MoveIt integration. The model is implemented in XACRO so common parameters (link lengths, diameters, base size) can be changed in one place and propagate through the URDF.

**Design highlights:**
- **Kinematics:** All joints rotate about their local Z axes; the arm traces an S-shaped path in the XY plane while maintaining tool height for simpler kinematic reasoning.
- **Geometry:** Repeated link segments (250 mm) with uniform tube diameter (Ø100 mm) and a short riser (150 mm) on a sturdy base (Ø250 × 80 mm).
- **Parametric model:** URDF is authored in XACRO — change a parameter once, update the whole robot.

**Repository layout (high level):**
- `src/ArmBot_description/` — robot description package (XACRO, meshes, launch files)
- `src/ArmBot_moveit/` — MoveIt configuration and planners
- `install/`, `build/`, `log/` — colcon build artifacts (generated)

## Prerequisites
- Ubuntu or macOS with ROS 2 (matching the workspace) installed and sourced.
- `colcon` for building the workspace.

On macOS / zsh, you can source the workspace with:

```
source install/setup.zsh
```

Or for bash:

```
source install/setup.bash
```

## Build and launch
1. Build the workspace (from repository root):

```
colcon build --symlink-install
```

2. Source the generated setup file (pick the shell you use):

```
source install/setup.zsh   # zsh
source install/setup.bash  # bash
```

3. Visualize the robot model (example):

```
ros2 launch ArmBot_description display.launch.py
```

Replace the launch name above with any available launch files in `src/ArmBot_description/launch` or `src/ArmBot_moveit/launch` for MoveIt demos.

## Customization
- The URDF is generated from XACRO files in `src/ArmBot_description/ArmBot_description/urdf` (or similar). Typical parameters you may change:
	- `link_length` — length of each repeated segment
	- `link_diameter` — tube outer diameter
	- `base_diameter`, `base_height` — base dimensions
- After editing XACRO parameters, rebuild the workspace and re-launch the display to see updates.

## Troubleshooting
- If meshes fail to load, confirm paths in XACRO and that `package.xml` exposes the `share` folder.
- For runtime errors, source the correct `install/setup.*` before launching.

## Next steps / Suggestions
- Add example MoveIt planning demos (pick-and-place, joint trajectory playback).
- Add unit/integration tests or a GitHub Actions workflow to build the workspace automatically.

