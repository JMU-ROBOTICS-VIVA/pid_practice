from launch import LaunchDescription
from launch_ros.actions import Node

from launch import LaunchContext
from launch.actions import SetEnvironmentVariable


def generate_launch_description():

    return LaunchDescription([
        Node(
            package="pid_practice",
            executable="guidance",
            name="guidance_node",
            output="screen",
            parameters=[
                {"p_gain": -1.0,
                 "i_gain": -1.0,
                 "d_gain": -1.0}
            ]
        ),
        Node(
            package="rocketbot",
            executable="rocketbot_node",
            name="rocketbot_node",
            output="screen")

    ])
