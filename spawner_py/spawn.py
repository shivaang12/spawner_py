# Copyright 2019 Shivang Patel

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import rclpy
from gazebo_msgs.srv import SpawnEntity


def request_spawn(xml: str):
    rclpy.init()
    node = rclpy.create_node('spawn_entity')
    client = node.create_client(SpawnEntity, 'spawn_entity')
    if not client.service_is_ready():
        client.wait_for_service()
    request = SpawnEntity.Request()
    request.xml = xml
    request.initial_pose.position.x = 0.0
    request.initial_pose.position.y = 0.0
    request.initial_pose.position.z = -0.1
    print("Sending Request!")
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        print('response: %r' % future.result())
    else:
        raise RuntimeError('exception while calling service: %r' % future.exception())
    node.destroy_node()
    rclpy.shutdown()

def main():
    if len(sys.argv) < 2:
        print('usage: ros2 run my_package my_node.py -- example.urdf')
        sys.exit(1)
    f = open(sys.argv[1], 'r')
    request_spawn(f.read())