# ArmBot: six-joint ROS 2 robot-description concept

ArmBot is a CAD-to-ROS 2 robot-description portfolio project containing a seven-link, six-joint Xacro/URDF model, STL meshes, RViz and Gazebo launch definitions, and CAD/RViz screenshots.

> **Current status:** a verified clean launch is blocked because `ArmBot.xacro` includes `ArmBot.ros2control`, while the committed source file is named `ArmBot.ros2control.xml`. The repository is therefore a robot-description concept and evidence archive, not a currently runnable or controlled manipulator.

## Portfolio highlights

- A committed Xacro model defines `base_link` and six successive links with visual, collision, and inertial data.
- Seven committed STL files provide the base and link meshes used by the model.
- Launch definitions express RViz display and Gazebo simulation intent.
- Six committed images record CAD views and historical RViz views of the concept.
- Historical colcon logs and generated build/install artifacts record prior workspace activity; they are not portable runtime proof.

## Joint definition

The table below transcribes the six joints in [`ArmBot.xacro`](ros2_ws/src/ArmBot_description/ArmBot_description/urdf/ArmBot.xacro). Continuous joints have no `<limit>` element in the committed source.

| Joint | Type | Parent -> child | Axis | Lower | Upper | Effort | Velocity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Revolute 1` | continuous | `base_link` -> `link_1_1` | `0 0 1` | no `<limit>` element | no `<limit>` element | no `<limit>` element | no `<limit>` element |
| `Revolute 2` | revolute | `link_1_1` -> `link_2_1` | `1 0 0` | `-1.570796` | `1.570796` | `100` | `100` |
| `Revolute 3` | continuous | `link_2_1` -> `link_3_1` | `0 0 1` | no `<limit>` element | no `<limit>` element | no `<limit>` element | no `<limit>` element |
| `Revolute 4` | revolute | `link_3_1` -> `link_4_1` | `-1 0 0` | `-2.181662` | `2.181662` | `100` | `100` |
| `Revolute 5` | continuous | `link_4_1` -> `link_5_1` | `0 0 1` | no `<limit>` element | no `<limit>` element | no `<limit>` element | no `<limit>` element |
| `Revolute 6` | continuous | `link_5_1` -> `link_6_1` | `1 0 0` | no `<limit>` element | no `<limit>` element | no `<limit>` element | no `<limit>` element |

The axes are deliberately recorded as authored: the model mixes Z, X, and negative-X rotation axes. Its dimensions and transforms are fixed values in the Xacro source; it does not expose geometry parameters for link lengths, diameters, or base dimensions.

## Architecture and repository map

The ROS 2 workspace is `ros2_ws`, not the repository root:

```text
6DOF-Robot/
|-- README.md
|-- docs/                         # reference documents and committed screenshots
`-- ros2_ws/
    |-- src/ArmBot_description/ArmBot_description/
    |   |-- urdf/                 # model, Gazebo, and ros2_control fragments
    |   |-- meshes/               # base plus six link STL files
    |   |-- launch/               # display.launch.py and gazebo.launch.py
    |   `-- config/               # RViz profiles and Gazebo bridge configuration
    |-- build/                    # historical generated artifacts
    |-- install/                  # historical generated artifacts
    `-- log/                      # historical colcon output
```

There is no committed source MoveIt package. References to `ArmBot_moveit` occur only in historical generated build/install/log artifacts and do not demonstrate a current MoveIt configuration or planning workflow.

Read the focused references for the [model architecture](docs/ARCHITECTURE.md), [reproducibility boundary](docs/REPRODUCIBILITY.md), [evidence register](docs/EVIDENCE.md), and [safety scope](docs/SAFETY.md).

## Evidence gallery

These images are committed historical artifacts. The RViz images show a recorded visualization state, and the CAD images show the ArmBot concept in its CAD environment; neither is current runtime, control, or hardware proof.

| Historical RViz views | Historical CAD views |
| --- | --- |
| ![Historical RViz oblique view of the ArmBot model on a grid](<docs/Screenshot_2025-10-16_at_11.11.33_PM.png>) | ![Historical CAD perspective view of ArmBot with the six joint relationships listed](<docs/Screenshot_2025-10-16_at_11.55.14_PM.png>) |
| ![Historical RViz distant oblique view of the ArmBot model](<docs/Screenshot_2025-10-16_at_11.42.42_PM.png>) | ![Historical CAD front elevation of the ArmBot concept](<docs/Screenshot_2025-10-16_at_11.55.21_PM.png>) |
| ![Historical RViz front view of the ArmBot model](<docs/Screenshot_2025-10-16_at_11.42.55_PM.png>) | ![Historical CAD left-side view of the ArmBot concept with joint markers](<docs/Screenshot_2025-10-16_at_11.56.01_PM.png>) |

## Historical reproduction context

The committed logs record colcon activity from a ROS 2 Jazzy-era workspace using Python 3.12 and paths under `/root/workspaces/ms1242_robotics_fall2025/challenge_hw1/ros2_ws`. They show that the description package and a now-absent `ArmBot_moveit` package were built in that historical environment. Generated `build/`, `install/`, and `log/` directories retain machine-specific paths and stale outputs, so they must not be treated as a clean checkout or a supported installation.

For the precise blocker, workspace location, dependency caveats, and a future clean-workspace validation checklist, see [Reproducibility](docs/REPRODUCIBILITY.md).

## Known limitations and safety scope

- The Xacro include-name mismatch prevents a verified clean Xacro expansion and clean launch.
- The committed `ArmBot.ros2control.xml` is an otherwise empty robot XML fragment; no control interfaces or controller configuration are provided.
- The Gazebo bridge configuration maps only `/clock`; it does not establish actuator, joint-state, or command bridging.
- `gazebo.launch.py` uses `ros_gz_sim` and `ros_gz_bridge`, but the package manifest does not declare them.
- No source MoveIt package, planner configuration, trajectory execution, calibration, actuator selection, wiring, mechanical validation, or physical deployment evidence is committed.

ArmBot is concept/simulation documentation only. It is not a hardware design, control system, or safety-qualified robot. See [SAFETY.md](docs/SAFETY.md) before interpreting the model beyond the committed description assets.

## Contributing and support

Please read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md), and [SUPPORT.md](SUPPORT.md). The issue templates request enough context to distinguish a model, documentation, or reproduction report while preserving the project's evidence boundary.

## Authorship and license status

Authored by Muhammad Ahmed. No license is currently provided; reuse terms for both code and model assets have not been selected.
