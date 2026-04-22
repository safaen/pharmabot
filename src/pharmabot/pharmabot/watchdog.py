
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json,time

class Watchdog(Node):
    def __init__(self):
        super().__init__('watchdog')
        self.sub=self.create_subscription(String,'scheduled_tasks',self.check,10)

    def check(self,msg):
        t=json.loads(msg.data)
        if time.time()>t["deadline"]:
            self.get_logger().error("DEADLINE MISSED")

def main():
    rclpy.init()
    node=Watchdog()
    rclpy.spin(node)
    rclpy.shutdown()
