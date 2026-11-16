"""slam_online_async.launch.py — launch SLAM Toolbox in online_async mode.

Loads config/slam_params.yaml and starts the async SLAM node bound to
the /scan topic with use_sim_time=true (Webots is the clock source).

Usage:
  ros2 launch slam_mapping_tp slam_online_async.launch.py
  # then drive the robot with:
  ros2 run teleop_twist_keyboard teleop_twist_keyboard
"""
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    params_file = os.path.join(
        get_package_share_directory('slam_mapping_tp'),
        'config', 'slam_params.yaml')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    slam_node = Node(
        parameters=[
            params_file,
            {'use_sim_time': use_sim_time},
        ],
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        remappings=[('/scan', '/scan'), ('/map', '/map')],
    )

    # RViz with the SLAM view config
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', os.path.join(
            get_package_share_directory('slam_mapping_tp'),
            'config', 'slam_config.rviz')],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen',
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        slam_node,
        rviz_node,
    ])
