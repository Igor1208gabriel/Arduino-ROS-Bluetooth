import serial
from std_msgs.msg import String
from rclpy.node import Node
import rclpy 

def conectar(porta, bw):
  while(1):
    try:
      conexao=serial.Serial(porta, bw)
      print("conectado")
      conexao.flushInput()
      return conexao
    except:
      break

class Pub(Node):
  def __init__(self, conexao, nome):
    super().__init__("Publisher")
    self.pub = self.create_publisher(String, nome, 10)
    self.publicar = self.create_timer(0.05, self.chamada_timer)
    self.bt = conexao
  
  def chamada_timer(self):
    enviar = String()
    mensagem = self.bt.readline().decode()
    self.get_logger().info("Recebi uma mensagem via Bluetooth!")

    if(mensagem): 
      enviar.data = mensagem
      self.pub.publish(enviar)
      self.get_logger().info(f'Enviei: "{mensagem}"') #comentar

    else:
      self.get_logger().info("Nenhuma mensagem! Aguardando até receber alguma")





def main(args = None):
  rclpy.init(args=args)
  bt = conectar("/dev/rfcomm0", 9600)
  no = Pub(bt, "Receber")
  rclpy.spin(no)

if __name__ == "__main__":
  main()