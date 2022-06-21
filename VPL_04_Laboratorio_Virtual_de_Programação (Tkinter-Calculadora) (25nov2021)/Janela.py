from tkinter import *


class Janela(Tk):
    __Lb_valor1=None
    __Lb_valor2=None
    __Lb_result=None
    __Et_valor1=None
    __Et_valor2=None
    __Et_result=None
    __Bt_adic=None
    __Bt_sub=None
    __Bt_mult=None
    __Bt_div=None

    def __init__(self, titulo):
        super().__init__()
        super().title(titulo)
        super().geometry("350x150+50+50")
        super().configure(bg="orange")
        self.inicialize()

    def action_exit(self):
        self.destroy()

    def action_Bt_adic(self):
        num1 = float(self.__Et_valor1.get())
        num2 = float(self.__Et_valor2.get())
        result = num1 + num2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f" % result)
        
    def action_Bt_sub(self):
        num1 = float(self.__Et_valor1.get())
        num2 = float(self.__Et_valor2.get())
        result = num1 - num2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f" % result)
    
    def action_Bt_mult(self):
        num1 = float(self.__Et_valor1.get())
        num2 = float(self.__Et_valor2.get())
        result = num1 * num2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f" % result)

    def action_Bt_div(self):
        num1 = float(self.__Et_valor1.get())
        num2 = float(self.__Et_valor2.get())
        result = num1 / num2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f" % result)

    def inicialize(self):
        self.__Lb_valor1 = Label(self, text="Valor1:", width=13, bg="yellow")
        self.__Lb_valor2 = Label(self, text="Valor2:", width=13, bg="yellow")
        self.__Lb_result = Label(self, text="Resultado:", width=13, bg="yellow")
        self.__Et_valor1 = Entry(self, width=30)
        self.__Et_valor2 = Entry(self, width=30)
        self.__Et_result = Entry(self, width=30)
        
        self.__Bt_adic = Button(self, text="Add", command=self.action_Bt_adic)
        self.__Bt_sub = Button(self, text="Sub", command=self.action_Bt_sub)
        self.__Bt_mult = Button(self, text="Mult", command=self.action_Bt_mult)
        self.__Bt_div = Button(self, text="Div", command=self.action_Bt_div)
        
        self.__Lb_valor1.grid(row=0, column=0, padx=2, pady=5)
        self.__Lb_valor2.grid(row=1, column=0, padx=2, pady=5)
        self.__Et_valor1.grid(row=0, column=1, padx=2, pady=2, columnspan=4)
        self.__Et_valor2.grid(row=1, column=1, padx=2, pady=2, columnspan=4)
        
        self.__Bt_adic.grid(row=2, column=1, padx=2, pady=2)
        self.__Bt_sub.grid(row=2, column=2, padx=2, pady=2)
        self.__Bt_mult.grid(row=2, column=3, padx=2, pady=2)
        self.__Bt_div.grid(row=2, column=4, padx=2, pady=2)
        
        self.__Lb_result.grid(row=3, column=0, padx=2, pady=2)
        self.__Et_result.grid(row=3, column=1, padx=2, pady=2, columnspan=4)
        
        self.protocol("WM_DELETE_WINDOW", self.action_exit)

##################################################
