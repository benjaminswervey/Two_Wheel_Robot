# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


class MinimalSubscriber(Node):
    max_abs_speed=1.25#m/s
    max_abs_turn=3.141592653589#rad/s
    wheel_radius=0.0325#m
    track_width=0.2#m

    def __init__(self):
        super().__init__('JoyToSpeed')
        
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher_=self.create_publisher(
            Twist,
            '/cmd_vel',
            10

        )

    def listener_callback(self, msg):
        #3=left+/right- #4=up+/down-
        Axes=msg.axes
        Drive_Cmd=Axes[4]
        Turn_Cmd=Axes[3]
        Desired_Drive=Drive_Cmd*self.max_abs_speed
        Desired_Turn=Turn_Cmd*self.max_abs_turn
        msg = Twist()
        linear=Vector3()
        linear.x=Desired_Drive
        angle=Vector3()
        angle.z=Desired_Turn
        msg.linear=linear
        msg.angular=angle
        self.publisher_.publish(msg)
        right_vel=Desired_Drive+Desired_Turn*self.track_width/2
        left_vel=Desired_Drive-Desired_Turn*self.track_width/2
        right_omega=right_vel/self.wheel_radius
        left_omega=left_vel/self.wheel_radius

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
