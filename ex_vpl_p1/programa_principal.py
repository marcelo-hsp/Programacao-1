import sys
from divida import Divida

objClienteDivida = Divida()
objClienteDivida.Leitura()
objClienteDivida.Calculo()
print(objClienteDivida.toString())
sys.exit(0)