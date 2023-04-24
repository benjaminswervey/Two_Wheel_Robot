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
from gpiozero import Button
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from gpiozero import DigitalInputDevice
from std_msgs.msg import Bool



class Encoder_Reader(Node):
    def __init__(self):
        
        
        super().__init__('Encoder_Reader')
        enc1 = 20
        enc2 = 21
        self.count=0
        self.encpin1=DigitalInputDevice(enc1)
        self.encpin2=DigitalInputDevice(enc2)

        self.publisher_=self.create_publisher(
            int,
            '/Enc',
            10

        )
        self.timer_ = self.create_timer(0.5, self.publish_gpio_status)
        self.encpin1.when_activated=self.AddOne
    def publish_gpio_status(self):
        self.publisher_.publish(self.count)
    
    def update_encoder_count(self):
        if(self.encpin1.value==self.encpin2.value):
            self.count+=1
        else:
            self.count-=1
        self.publisher_.publish(self.count)
    
    

       

def main(args=None):
    rclpy.init(args=args)
    gpio_publisher = Encoder_Reader()
    rclpy.spin(gpio_publisher)
    gpio_publisher.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()
