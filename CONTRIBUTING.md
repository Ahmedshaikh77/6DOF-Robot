# Contributing

Thank you for helping improve the ArmBot robot-description portfolio. Contributions should make claims more accurate, preserve existing assets, and keep the project's concept-only scope clear.

## Before opening a change

- Work from `ros2_ws` when examining the ROS 2 package.
- State the ROS distribution, operating system, and Python version used for any reproduction work.
- Use a clean workspace; do not rely on committed `build/`, `install/`, or `log/` artifacts as a setup.
- Include the exact Xacro command or launch command and complete relevant output when reporting a result.
- Separate observed behavior from expected behavior.
- State the provenance and intended usage rights for added meshes, images, or derived assets.
- Do not imply a verified launch, MoveIt workflow, control interface, safety property, or hardware capability unless the change adds direct, reviewable evidence.

## Scope for contributions

Documentation corrections, source-model corrections, and reproducibility reports are welcome. Changes to generated outputs, screenshots, or STL meshes need a clear rationale and provenance. Do not add a license unless the owner has selected terms that cover both code and model assets.

## Pull requests

Use the pull-request template. Explain the affected files, the evidence behind every public claim, and the validation performed. For reproduction work, include the clean-workspace context and label historical evidence separately from a newly observed result.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) and review the [Safety scope](docs/SAFETY.md).
