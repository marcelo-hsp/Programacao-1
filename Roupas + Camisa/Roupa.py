class Roupa():
    __Roupa_Marca: str
    __Roupa_Cor: str
    __Roupa_Tam: int
    __Roupa_Quant: int
    __Roupa_Preco: float
    __Total_Roupa: float
    
    def __init__(self):
        self.__Roupa_Marca = ""
        self.__Roupa_Cor = ""
        self.__Roupa_Tam = 0
        self.__Roupa_Quant = 0
        self.__Roupa_Preco = 0.0
        self.__Total_Roupa = 0.0
        self.Calcula_Total()
        
    def Leitura(self):
        self.__Roupa_Marca = input("Digite a marca da roupa: ")
        self.__Roupa_Cor = input("Digite a cor da roupa: ")
        self.__Roupa_Tam = int(input("Digite o tamanho da roupa: "))
        self.__Roupa_Quant = int(input("Digite a quantidade de roupas: "))
        self.__Roupa_Preco = float(input("Digite o preço da roupa: "))
    
    def Calcula_Total(self):
        self.__Total_Roupa = (self.__Roupa_Quant * self.__Roupa_Preco)
    
    def toString(self):
        
        Str=""
        Str += "\nImpressão das Roupas\n"
        Str += "Marca da roupa=%s\n" % self.__Roupa_Marca
        Str += "Cor da roupa=%s\n" % self.__Roupa_Cor
        Str += "Tamanho da roupa=%d\n" % self.__Roupa_Tam
        Str += "Quantidade de roupas=%d\n" % self.__Roupa_Quant
        Str += "Preço da peça de roupa=%5.2f\n" % self.__Roupa_Preco
        Str += "Total=%5.2f\n" % self.__Total_Roupa
        return (Str)
        
    def __del__(self):
        print("Passei no destrutor da classe Roupa...")
        self.__Roupa_Marca = ""
        self.__Roupa_Cor = ""
        self.__Roupa_Tam = 0
        self.__Roupa_Quant = 0
        self.__Roupa_Preco = 0.0
        self.__Total_Roupa = 0.0        