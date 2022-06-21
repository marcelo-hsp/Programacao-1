class Cliente():
    __Nome = None
    __Endereco = None
    __Data = None
    __Salario: float
    def __init__(self):
        self.__Nome = ""
        self.__Endereco = ""
        self.__Data = ""
        self.__Salario = 0.0
    
    def Leitura(self):
        self.__Nome = input("Digite o nome do cliente: ")
        self.__Endereco = input("Digite o endereço do cliente: ")
        self.__Data = input("Digite a data de nascimento do cliente: ")
        self.__Salario = float(input("Digite o salário do cliente: "))
    
    def toString(self):
        Str = ""
        Str += "Nome: %s\n" % self.__Nome
        Str += "Endereço: %s\n" % self.__Endereco
        Str += "Data: %s\n" % self.__Data
        Str += "Salário: %f\n" % self.__Salario
        return Str
    
    def __del__(self):
        self.__Nome = ""
        self.__Endereco = ""
        self.__Data = ""
        self.__Salario = 0.0