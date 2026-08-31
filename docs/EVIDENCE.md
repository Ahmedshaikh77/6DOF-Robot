# Evidence register

This document separates committed source and assets from historical generated output. It also states what those materials do not establish.

## Committed screenshot register

| File | Recorded view | What it supports |
| --- | --- | --- |
| [`Screenshot_2025-10-16_at_11.11.33_PM.png`](<Screenshot_2025-10-16_at_11.11.33_PM.png>) | RViz oblique view | A historical RViz view of the model |
| [`Screenshot_2025-10-16_at_11.42.42_PM.png`](<Screenshot_2025-10-16_at_11.42.42_PM.png>) | RViz distant oblique view | A historical RViz view of the model |
| [`Screenshot_2025-10-16_at_11.42.55_PM.png`](<Screenshot_2025-10-16_at_11.42.55_PM.png>) | RViz front view | A historical RViz view of the model |
| [`Screenshot_2025-10-16_at_11.55.14_PM.png`](<Screenshot_2025-10-16_at_11.55.14_PM.png>) | CAD perspective | A CAD view showing ArmBot and its listed joint relationships |
| [`Screenshot_2025-10-16_at_11.55.21_PM.png`](<Screenshot_2025-10-16_at_11.55.21_PM.png>) | CAD front elevation | A CAD view of the ArmBot concept |
| [`Screenshot_2025-10-16_at_11.56.01_PM.png`](<Screenshot_2025-10-16_at_11.56.01_PM.png>) | CAD left-side view | A CAD view showing a side view and joint markers |

The RViz images carry historical application-window paths and dates. They are not a claim that the current checkout expands Xacro or launches successfully.

## Authored source and assets

The committed description source includes `ArmBot.xacro`, material and Gazebo fragments, launch definitions, RViz configurations, seven STL mesh files, and the six screenshot files listed above. These artifacts support claims about the existence and content of the robot description and visual concept.

The repository does not include original CAD source files, an asset license, or a provenance record that establishes ownership or redistribution rights beyond the files committed here. Contributors adding or replacing assets must state their source and usage rights in the change description.

## Historical generated artifacts

`ros2_ws/build/`, `ros2_ws/install/`, and `ros2_ws/log/` are committed historical outputs. The logs record prior colcon actions, including records for an `ArmBot_moveit` package that is not present under `ros2_ws/src/`. Absolute paths and generated metadata make these outputs stale and nonportable.

The artifacts support only the limited statement that prior workspace activity produced them. They do not prove current build success, current launch success, planning, control, physical operation, or repeatability on a clean machine.

## Unsupported claims

The current repository does not support claims of:

- a verified clean Xacro expansion or RViz/Gazebo launch;
- a source MoveIt configuration, motion planning, or trajectory execution;
- ros2_control hardware interfaces, controllers, joint command/state bridging, or robot control;
- calibration, collision validation, manufacturability, actuator selection, wiring, or physical deployment;
- a selected license or confirmed third-party asset permissions.

The reason for the clean-launch limitation and the scope of the model are described in [REPRODUCIBILITY.md](REPRODUCIBILITY.md), [ARCHITECTURE.md](ARCHITECTURE.md), and [SAFETY.md](SAFETY.md).
