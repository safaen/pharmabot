import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random, json, time

class TaskManager(Node):
    def __init__(self):
        super().__init__('task_manager')
        self.pub = self.create_publisher(String, 'tasks', 10)
        self.timer = self.create_timer(3.0, self.generate)

    def generate(self):
        task = {
            "id": int(time.time()),
            "priority": random.choice(["CRITICAL","URGENT","STANDARD"]),
            "location": random.choice(["ICU","Pharmacy","RoomA","RoomB"]),
            "deadline": time.time() + 10
        }

        msg = String()
        msg.data = json.dumps(task)
        self.pub.publish(msg)

        self.get_logger().info(f"📦 Task: {task}")

def main():
    rclpy.init()
    node = TaskManager()
    rclpy.spin(node)
    rclpy.shutdown()
