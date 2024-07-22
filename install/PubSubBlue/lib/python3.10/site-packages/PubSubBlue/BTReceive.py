import serial as se
from std_msgs.msg import String
from rclpy.node import Node
import rclpy 
from Connect import connect


class Pub(Node):
  #This node publishes any Messages it receives via bluetooth to a String topic

  def __init__(self, Connection, TopicName):
    super().__init__("Receiver")
    self.pub = self.create_publisher(String, TopicName, 10)
    self.publicar = self.create_timer(0.05, self.CallbackTimer)
    self.bt = Connection
  
  def CallbackTimer(self):
    ToSend = String()
    Message = self.bt.readline().decode()
    self.get_logger().info("Received a Bluetooth Message")

    if(Message): 
      ToSend.data = Message
      self.pub.publish(ToSend)
      self.get_logger().info(f'I Sent: "{Message}"') #you can comment this line





def main(args = None):
  rclpy.init(args=args)
    #Make sure the Bluetooth module is connected at "/dev/rfcomm0" (only on Linux) or change the code 
  Connection = connect("/dev/rfcomm0", 9600)
  node = Pub(Connection, "Receive")
  rclpy.spin(node)

if __name__ == "__main__":
  main()