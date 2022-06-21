import sys
from Roupa import Roupa

clothe=Roupa()
clothe.Leitura()
clothe.Calcula_Total()
print(clothe.toString())
del(clothe)
sys.exit(0)
