
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='pharmabot', executable='task_manager'),
        Node(package='pharmabot', executable='scheduler'),
        Node(package='pharmabot', executable='robot_nav'),
        Node(package='pharmabot', executable='watchdog'),
    ])
