import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import json

class RobotNav(Node):
    def __init__(self):
        super().__init__('robot_nav')

        self.sub = self.create_subscription(
            String,
            'scheduled_tasks',
            self.navigate,
            10
        )

        self.pub = self.create_publisher(PoseStamped, '/goal_pose', 10)

    def navigate(self, msg):
        task = json.loads(msg.data)

        locations = {
            "ICU": (8.0, 2.0),
            "Pharmacy": (-8.0, 2.0),
            "RoomA": (3.0, -3.0),
            "RoomB": (-3.0, -3.0)
        }

        x, y = locations.get(task["location"], (0.0, 0.0))

        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.orientation.w = 1.0

        self.pub.publish(goal)

        self.get_logger().info(f"🚀 Robot vers {task['location']}")

def main():
    rclpy.init()
    node = RobotNav()
    rclpy.spin(node)
    rclpy.shutdown()
