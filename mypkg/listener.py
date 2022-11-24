import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg)

rclpy.init()
node = Node("listener")
sub = node.create_subscription(Person, "person", cb, 10)

rclpy.spin(node)
