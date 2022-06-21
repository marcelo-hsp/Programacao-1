from cliente import Cliente

class Divida(Cliente):
    __Num_Prest: int
    __Valor: float
    __Total: float
    def __init__(self):
        self.__Num_Prest = 0
        self.__Valor = 0.0
        self.__Total = 0.0
        self.Calculo()
    
    def Leitura(self):
        super().Leitura()
        self.__Num_Prest = int(input("Digite o número de prestações: "))
        self.__Valor = float(input("Digite o valor da prestação: "))
        self.Calculo()
    
    def Calculo(self):
        self.__Total = self.__Num_Prest * self.__Valor
    
    def toString(self):
        Str = ""
        Str += super().toString()
        Str += "Número de prestações: %d\n" % self.__Num_Prest
        Str += "Valor: %f\n" % self.__Valor
        Str += "Total: %f\n" % self.__Total
        return Str

    def __del__(self):
        self.__Num_Prest = 0
        self.__Valor = 0.0
        self.__Total = 0.0
        self.Calculo()

