"""go2_sim.launch.py — launch Webots + the ROS2 bridge for the SLAM lab.

Brings up:
  * Webots with worlds/lab_world.wbt (headless optional via ``headless:=true``)
  * the webots_ros2 driver for the GO2_ROBOT, exposing:
      /scan              (sensor_msgs/LaserScan)
      /camera/image_raw  (sensor_msgs/Image)
      /odom              (nav_msgs/Odometry)
  * a base_footprint <-> base_link <-> odom static/odom chain
  * teleop_twist_keyboard is NOT started here — run it in a separate shell
    so the keystrokes don't get swallowed by the launch output.

Usage:
  ros2 launch slam_mapping_tp go2_sim.launch.py
  ros2 launch slam_mapping_tp go2_sim.launch.py headless:=true
"""
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    world_file = os.path.join(
        # fall back to a sensible relative path if the package isn't installed
        os.path.dirname(ThisLaunchFileDir()), '..', 'worlds', 'lab_world.wbt')

    headless = LaunchConfiguration('headless', default='false')

    # --- Webots + driver (from webots_ros2) ----------------------------
    webots_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('webots_ros2_core'),
                         'launch', 'webots_launch.py')),
        launch_arguments={
            'world': world_file,
            'mode': 'realtime',
            'publish_robot_description': 'true',
        }.items(),
    )

    # --- The Go2-like driver node ---------------------------------------
    # Bridges the Webots lidar/camera/odom/motors to ROS2 topics.
    # (For the real Unitree Go2 proto, swap 'go2_driver' for the unitree
    #  driver and remap /cmd_vel as needed — see docs/robot_swap_guide.md.)
    go2_driver = Node(
        package='webots_ros2_universal_robot',
        executable='universal_robot',
        name='go2_driver',
        parameters=[{'robot_description_topic': '/robot_description'}],
        remappings=[
            ('/scan', '/scan'),
            ('/camera/image_raw', '/camera/image_raw'),
            ('/odom', '/odom'),
            ('/cmd_vel', '/cmd_vel'),
        ],
    )

    # --- base_footprint static chain (SLAM Toolbox expects base_footprint)
    base_link_bf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='base_link_to_base_footprint',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint'],
    )

    return LaunchDescription([
        DeclareLaunchArgument('headless', default_value='false'),
        webots_launch,
        go2_driver,
        base_link_bf,
    ])
