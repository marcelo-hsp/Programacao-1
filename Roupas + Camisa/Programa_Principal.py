import sys
from Camisa import Camisa

obj_camisa=Camisa()
obj_camisa.Leitura()
obj_camisa.Calcula_Total()
print(obj_camisa.toString())
del(obj_camisa)
sys.exit(0)