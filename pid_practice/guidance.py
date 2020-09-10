#!/usr/bin/env python

"""Python rocket control node using PID controller.

Author: Nathan Sprague & ???
Version:

"""
import rclpy
import rclpy.node

from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3

from jmu_ros2_util import pid


class GuidanceNode(rclpy.node.Node):
    def __init__(self):
        super().__init__('guidance_node')

        self.create_subscription(Point, 'location', self.location_callback, 10)
        self.create_subscription(Point, 'target_event', self.target_callback,
                                 10)

        self.thrust_pub = self.create_publisher(Vector3, 'thrust', 10)

        # Set an arbitrary initial target
        self.target = Point()
        self.target.x = 240.0
        self.target.y = 100.0
        self.target.z = 0.0

        # THESE SHOULD BE READ FROM PARAMETERS!
        p_gain = -1.0
        i_gain = -1.0
        d_gain = -1.0

        log_str = "P gain: {}, I gain: {}, D gain: {}"
        self.get_logger().info(log_str.format(p_gain, i_gain, d_gain))

    def location_callback(self, location):
        thrust = Vector3()

        if location.y < self.target.y:
            thrust.y = 20.0

        self.thrust_pub.publish(thrust)

    def target_callback(self, target_msg):
        self.target = target_msg


def main():
    rclpy.init()
    thruster_node = GuidanceNode()
    rclpy.spin(thruster_node)

    thruster_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
