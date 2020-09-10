from launch import LaunchDescription
from launch_ros.actions import Node

from launch import LaunchContext
from launch.actions import SetEnvironmentVariable


def generate_launch_description():
    # By default (in Dashing) log messages are buffered and do not
    # immediately appear on the screen.  This is a hack to change that
    # behavior.
    lc = LaunchContext()
    SetEnvironmentVariable('RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED',
                           '1').visit(lc)

    return LaunchDescription([
        Node(
            package="pid_practice",
            node_executable="guidance",
            node_name="guidance_node",
            output="screen",
            parameters=[
                {"p_gain": -1.0,
                 "i_gain": -1.0,
                 "d_gain": -1.0}
            ]
        ),
        Node(
            package="rocketbot",
            node_executable="rocketbot_node",
            node_name="rocketbot_node",
            output="screen")

    ])
