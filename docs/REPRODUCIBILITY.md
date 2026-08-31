# Reproducibility

This repository preserves a ROS 2 robot-description concept, but it does not currently provide a verified clean-workspace launch path.

## Current blocker

`ros2_ws/src/ArmBot_description/ArmBot_description/urdf/ArmBot.xacro` includes `ArmBot.ros2control`. The tracked file in the same directory is `ArmBot.ros2control.xml`. Xacro processing must resolve that include before either committed launch definition can construct a robot description, so a clean Xacro expansion and clean launch are not verified.

This documentation does not rename, replace, or otherwise repair the source file. The mismatch is a known repository condition.

## Workspace root and historical context

The workspace root is `ros2_ws`:

```text
ros2_ws/
|-- src/ArmBot_description/ArmBot_description/
|-- build/
|-- install/
`-- log/
```

The committed logs record colcon activity from paths below `/root/workspaces/ms1242_robotics_fall2025/challenge_hw1/ros2_ws` with Python 3.12. Those artifacts are historical evidence of an environment that included ROS 2 Jazzy-era packages; they do not establish that the repository can be built or launched today, on another machine, or from a clean checkout.

The committed `build/`, `install/`, and `log/` directories are generated outputs. They contain absolute paths, cached package metadata, executable remnants, and logs from previous work. Do not copy them into a new workspace as installation instructions or use them as evidence of current runtime behavior.

## Dependencies and scope

The package manifest declares Xacro, RViz, robot state publisher, and joint-state publisher dependencies. The Gazebo launch file also uses `ros_gz_sim` and `ros_gz_bridge`, but those dependencies are not declared in the committed manifest. The bridge configuration maps only `/clock`.

There is no committed source MoveIt package, no controller configuration, and no hardware interface. Historical generated files that mention `ArmBot_moveit` cannot substitute for source code or a repeatable planning workflow.

## Future clean-workspace validation checklist

When the source blocker and dependency declarations have been deliberately addressed, a contributor can record a new validation with all of the following:

1. State the ROS distribution, operating system, Python version, and relevant Gazebo packages.
2. Start from a fresh checkout and a clean `ros2_ws` workspace without reusing the committed generated outputs.
3. Record the exact Xacro expansion command and its complete output.
4. Build from `ros2_ws`, retaining the complete colcon output and any dependency resolution details.
5. Record the exact display or Gazebo launch command and its complete output.
6. Distinguish model rendering from control, planning, or hardware claims; do not claim those capabilities unless new, direct evidence exists.
7. Provide asset provenance for any added meshes, images, or derived artifacts.

Use the [reproducibility issue form](../.github/ISSUE_TEMPLATE/reproducibility.md) to report either a clean-workspace result or a discrepancy. See [EVIDENCE.md](EVIDENCE.md) for the current evidence boundary.
