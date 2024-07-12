import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/igor/Projeto_Arduino_Blue/install/PubSubBlue'
