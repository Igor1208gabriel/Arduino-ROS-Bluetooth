from time import sleep
import serial as se
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def connect(port, bd):
  #Function connects to the Bluetooth module given the port it's connected and the Arduino baud rate
  #Be careful not to change the baud rate on the .ino file or change it here too
  
  while(1):
    try:
      Connection = se.Serial(port, bd)
      print("Connected Sucessfully")
      Connection.flushInput()
      return Connection
    except:
      print("Could not connect. Retrying in 10s.")
      sleep(10)
      break

class PubAndSub(Node):
        #This node receives a String message through a topic named "send"
        #Encodes and sends the message via Bluetooth

    def __init__(self, Connection, TopicName):
        super().__init__("Subscriber")
        self.sub = self.create_subscription(String, TopicName, self.Hear, 10)
        self.Connection = Connection
        self.sub 
    
    def Hear(self, message):
        self.get_logger().info(f"I Heard: {message.data}")
        self.get_logger().info("Sending a message via Bluetooth")
        self.Connection.write(("\n"+message.data).encode())




def main(args=None):                
    rclpy.init(args=args)
    #Make sure the Bluetooth module is connected at "/dev/rfcomm0" (only on Linux) or change the code 
    Connection = connect("/dev/rfcomm0", 9600)
    TopicName = "Send"
    node = PubAndSub(Connection, TopicName)
    rclpy.spin(node)

if __name__ == "__main__":
    main()