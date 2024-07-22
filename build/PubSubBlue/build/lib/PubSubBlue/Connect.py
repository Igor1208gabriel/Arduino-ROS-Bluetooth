from time import sleep
import serial as se

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