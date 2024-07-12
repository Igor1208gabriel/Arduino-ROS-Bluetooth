import serial
import rclpy
from rclpy.node import Node
from std_msgs.msg import String



def conectar(porta, bw):
  while(1):
    try:
      conexao=serial.Serial(porta, bw)
      print("conectado")
      conexao.flushInput()
      return conexao
    except:
      break

class no_subscriber(Node):

    def __init__(self, conexao):
        super().__init__("Subscriber")
        self.sub = self.create_subscription(String, "Receber", self.ouvindo, 10)
        self.conexao = conexao
        self.sub 
    
    def ouvindo(self, mensagem):
        self.get_logger().info(f"Ouvi: {mensagem.data}")
        enviar = mensagem.data[::-1]
        self.get_logger().info("Enviando uma mensagem via Bluetooth!")
        self.conexao.write(("\n"+enviar).encode())




def main(args=None):                
    rclpy.init(args=args)
    conexao = conectar("/dev/rfcomm0", 9600)
    novo_no = no_subscriber(conexao)
    rclpy.spin(novo_no)

if __name__ == "__main__":
    main()