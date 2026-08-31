# Architecture

ArmBot is a robot-description package, not a complete robot system. Its committed authored source is located at `ros2_ws/src/ArmBot_description/ArmBot_description`.

## Model tree

`ArmBot.xacro` defines a serial tree with seven links:

```text
base_link
`-- Revolute 1 (continuous, 0 0 1)
    `-- link_1_1
        `-- Revolute 2 (revolute, 1 0 0)
            `-- link_2_1
                `-- Revolute 3 (continuous, 0 0 1)
                    `-- link_3_1
                        `-- Revolute 4 (revolute, -1 0 0)
                            `-- link_4_1
                                `-- Revolute 5 (continuous, 0 0 1)
                                    `-- link_5_1
                                        `-- Revolute 6 (continuous, 1 0 0)
                                            `-- link_6_1
```

Continuous joints have no `<limit>` element in the committed source.

| Joint | Type | Axis | Lower | Upper | Effort | Velocity |
| --- | --- | --- | --- | --- | --- | --- |
| `Revolute 1` | continuous | `0 0 1` | no `<limit>` element | no `<limit>` element | no `<limit>` element | no `<limit>` element |
| `Revolute 2` | revolute | `1 0 0` | `-1.570796` | `1.570796` | `100` | `100` |
| `Revolute 3` | continuous | `0 0 1` | no `<limit>` element | no `<limit>` element | no `<limit>` element | no `<limit>` element |
| `Revolute 4` | revolute | `-1 0 0` | `-2.181662` | `2.181662` | `100` | `100` |
| `Revolute 5` | continuous | `0 0 1` | no `<limit>` element | no `<limit>` element | no `<limit>` element | no `<limit>` element |
| `Revolute 6` | continuous | `1 0 0` | no `<limit>` element | no `<limit>` element | no `<limit>` element | no `<limit>` element |

The Xacro source contains fixed mesh origins, inertial values, joint origins, and axes. It contains no exposed Xacro properties for geometry changes.

## Assets and authored files

- `urdf/ArmBot.xacro` is the main model source.
- `urdf/materials.xacro` supplies the `silver` material.
- `urdf/ArmBot.gazebo` supplies Gazebo material, friction, and self-collision tags for the base and links, plus a gravity tag for `base_link`.
- `meshes/` contains `base_link.stl` and six link STL files. Each is referenced by the Xacro model using a package lookup and a `0.001` scale.
- `config/display.rviz` and `config/gazebo.rviz` are RViz configurations.
- `launch/display.launch.py` expresses a display flow using Xacro processing, robot state publication, a joint-state publisher, and RViz.
- `launch/gazebo.launch.py` expresses a Gazebo flow using `ros_gz_sim`, `ros_gz_bridge`, robot state publication, and a spawn request.

## Integration boundaries

The display and Gazebo launch definitions process `ArmBot.xacro` before launching their nodes. That processing is currently blocked by an include-name mismatch: the model requests `urdf/ArmBot.ros2control`, while the committed file is `urdf/ArmBot.ros2control.xml`.

The committed ros2_control fragment only contains the enclosing robot XML element. It does not define hardware, joints, command/state interfaces, controllers, or controller-manager integration. The Gazebo bridge configuration contains only a Gazebo-to-ROS `/clock` mapping. These files express neither a controllable robot nor an end-to-end simulation integration.

`gazebo.launch.py` references `ros_gz_sim` and `ros_gz_bridge`, while the committed package manifest does not declare those dependencies. The source package also contains no MoveIt package or planning configuration. Generated references to `ArmBot_moveit` under `build/`, `install/`, and `log/` are historical artifacts rather than source architecture.

For verification limits and historical evidence, see [REPRODUCIBILITY.md](REPRODUCIBILITY.md) and [EVIDENCE.md](EVIDENCE.md).
