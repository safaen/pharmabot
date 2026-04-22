import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json, heapq

class Scheduler(Node):
    def __init__(self):
        super().__init__('scheduler')
        self.sub = self.create_subscription(String, 'tasks', self.add, 10)
        self.pub = self.create_publisher(String, 'scheduled_tasks', 10)
        self.queue = []

    def add(self, msg):
        task = json.loads(msg.data)

        priority = {"CRITICAL":0,"URGENT":1,"STANDARD":2}
        heapq.heappush(self.queue, (priority[task["priority"]], task))

        _, t = heapq.heappop(self.queue)

        out = String()
        out.data = json.dumps(t)
        self.pub.publish(out)

        self.get_logger().info(f"Scheduled: {task}")

def main():
    rclpy.init()
    node = Scheduler()
    rclpy.spin(node)
    rclpy.shutdown()
