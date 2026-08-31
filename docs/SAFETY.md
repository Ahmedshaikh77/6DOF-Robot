# Safety scope

ArmBot is documented as a concept and robot-description asset set. It is not documented as a hardware-ready robot, a control system, or a safety-qualified simulation.

## What the repository contains

The committed material includes a Xacro/URDF description, STL meshes, RViz and Gazebo launch definitions, a minimal Gazebo bridge mapping, CAD screenshots, RViz screenshots, and historical generated workspace artifacts. These items support inspection of the model assets and their documented structure.

## What is not established

The repository contains no evidence of actuator selection, hardware interfaces, controller configuration, joint command/state interfaces, emergency-stop design, limit-switch design, braking, electrical protection, wiring, calibration, payload analysis, structural validation, collision validation, risk assessment, or physical testing.

The ros2_control fragment is otherwise empty, and the bridge configuration maps only `/clock`. The current Xacro include-name mismatch also prevents a verified clean expansion and launch. A visual model, a historical screenshot, or a historical build log must not be read as proof of safe behavior or operational readiness.

## Required interpretation

- Do not connect this description to hardware or use it to command equipment.
- Do not infer safe motion, reachable workspace, joint limits beyond those explicitly recorded in the Xacro source, load capacity, or collision clearance.
- Do not present the project as production, educational-lab, or physical-deployment guidance without independently engineered controls and validation.
- Treat any future control or hardware work as a separate engineering effort with appropriate hazard analysis, applicable standards review, testing, and qualified supervision.

When filing an issue or proposing a change, describe only observed evidence and avoid representing model assets as a control or hardware capability. See [EVIDENCE.md](EVIDENCE.md) for the claim boundary.
