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
import RPi.GPIO as GPIO
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

from std_msgs.msg import Bool



class Encoder_Reader(Node):
      def __init__(self):
        enc1 = 2
        enc2 = 3

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(enc1, GPIO.IN)
        GPIO.setup(enc2, GPIO.IN)
        super().__init__('Encoder_Reader')
        
        self.publisher_=self.create_publisher(
            Bool,
            '/Enc',
            10

        )
        self.timer_ = self.create_timer(0.5, self.publish_gpio_status)
        def publish_gpio_status(self):
            gpio_status = Bool()
            gpio_status.data = GPIO.input(enc1)
            self.publisher_.publish(gpio_status)
        
        #3=left+/right- #4=up+/down-
       

def main(args=None):
    rclpy.init(args=args)
    gpio_publisher = Encoder_Reader()
    rclpy.spin(gpio_publisher)
    gpio_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
