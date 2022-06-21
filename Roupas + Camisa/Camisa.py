from Roupa import Roupa

class Camisa(Roupa):
    __Cam_Tipo: str
    __Cam_Botoes: int
    __Cam_Bolsos: int
    __Cam_Gola: bool
    
    def __init__(self):
        super().__init__()
        self.__Cam_Tipo = ""
        self.__Cam_Botoes = 0
        self.__Cam_Bolsos = 0
        self.__Cam_Gola = True
        
    def Leitura(self): 
        self.__Cam_Tipo = input("Digite o tipo da camisa: ")
        self.__Cam_Botoes = int(input("Digite a quantidade de botões: "))
        self.__Cam_Bolsos = int(input("Digite a quantidade de bolsos: "))
        self.gola = input("Digite [s] para camisa com gola e [n] para camisa sem gola: ")
        if self.gola.upper() == 'S':
            self.__Cam_Gola = True
        elif self.gola.upper() == 'N':
            self.__Cam_Gola = False
        else:
            print("Opção invalida.")
            self.__Cam_Gola = False
        super().Leitura()
        
    def toString(self):
        Str = "\nImpressão das Camisas\n"
        Str += "Tipo de camisa=%s\n" % self.__Cam_Tipo
        Str += "Quantidade de botões=%d\n" % self.__Cam_Botoes
        Str += "Quantidade de bolsos=%d\n" % self.__Cam_Bolsos
        Str += "Tem gola=%s\n" % self.__Cam_Gola
        Str += super().toString()
        return (Str)

    def __del__(self):
        super().__del__()
        print("Passei no destrutor da classe Camisa...")
        self.__Cam_Tipo = ""
        self.__Cam_Botoes = 0
        self.__Cam_Bolsos = 0
        self.__Cam_Gola = True
        
        