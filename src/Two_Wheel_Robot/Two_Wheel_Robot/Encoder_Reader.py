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
import gpiod
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from std_msgs.msg import Int32
from std_msgs.msg import Int32MultiArray



class Encoder_Reader(Node):
    def __init__(self):
        
        
        super().__init__('Encoder_Reader')
        asdf=gpiod.chip(0)
        self.chip = gpiod.chip(1)
        enc1 = 20
        enc2 = 21
        self.line = self.chip.get_line(98)
        self.asdf_line=asdf.get_line(9)
        
        self.count=0
        config=gpiod.line_request()
        config2=gpiod.line_request()
        config.consumer="Encoder_Reader"
        config2.consumer="Encoder_Reader"
        config.request_type=gpiod.line_request.DIRECTION_INPUT
        config2.request_type=gpiod.line_request.DIRECTION_INPUT
        self.line.request(config)
        self.asdf_line.request(config2)
        self.encoder_pub = self.create_publisher(Int32MultiArray, 'encoder_value', 10)
        
        self.timer_ = self.create_timer(0.1, self.read_encoder)

    def read_encoder(self):
        value=Int32MultiArray
        value[0]= self.line.get_value()
        value[1]= self.asdf_line.get_value()
        self.encoder_pub.publish(Int32MultiArray(data=value))

    #def __del__(self):
    #    self.chip.__del__()
    
    
    
    

       

def main(args=None):
    rclpy.init(args=args)
    gpio_publisher = Encoder_Reader()
    rclpy.spin(gpio_publisher)
    gpio_publisher.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()
