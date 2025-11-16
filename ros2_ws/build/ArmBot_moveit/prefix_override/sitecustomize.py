import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/root/workspaces/ms1242_robotics_fall2025/challenge_hw1/ros2_ws/install/ArmBot_moveit'
