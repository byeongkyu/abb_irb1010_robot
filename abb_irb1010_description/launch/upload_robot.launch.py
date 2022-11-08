import os
from os import environ

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, Shutdown
from launch.substitutions import LaunchConfiguration, Command, TextSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    ld = LaunchDescription()

    environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '0'
    rviz_config_file = os.path.join(get_package_share_directory('abb_irb1010_description'), 'rviz', 'view_robot.rviz')

    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'ignore_timestamp': False,
            'robot_description':
                Command([
                    'xacro ',
                    PathJoinSubstitution([
                        get_package_share_directory('abb_irb1010_description'),
                        'urdf/robot.urdf.xacro',
                    ]),
                ]),
            'use_sim_time': True,
        }]
    )

    ld.add_action(rsp_node)
    return ld