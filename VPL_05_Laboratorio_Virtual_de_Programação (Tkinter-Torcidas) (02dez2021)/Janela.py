from tkinter import *

class Janela(Tk):
    __Lb_flamengo=None
    __Lb_vasco=None
    __Lb_torcida_total=None
    __Lb_pr=None
    __Lb_sc=None
    __Lb_rs=None
    __Et_flamengo_pr=None
    __Et_flamengo_sc=None
    __Et_flamengo_rs=None
    __Et_vasco_pr=None
    __Et_vasco_sc=None
    __Et_vasco_rs=None
    __Et_total_flamengo=None
    __Et_total_vasco=None
    __Bt_calc=None

    def __init__(self, titulo):
        super().__init__()
        super().title(titulo)
        super().geometry("450x250+50+50")
        super().configure(bg="orange")
        self.inicialize()

    def action_Total_Flamengo(self):
        flaSc = float(self.__Et_flamengo_sc.get())
        flaPr = float(self.__Et_flamengo_pr.get())
        flaRs = float(self.__Et_flamengo_rs.get())
        totalFla = flaSc + flaPr + flaRs
        self.__Et_total_flamengo.delete(0, END)
        self.__Et_total_flamengo.insert(END, "%4.1f" % totalFla)

    def action_Total_Vasco(self):
        vascSc = float(self.__Et_vasco_sc.get())
        vascPr = float(self.__Et_vasco_pr.get())
        vascRs = float(self.__Et_vasco_rs.get())
        totalVasco = vascSc + vascPr + vascRs
        self.__Et_total_vasco.delete(0, END)
        self.__Et_total_vasco.insert(END, "%4.1f" % totalVasco)

    def action_exit(self):
        self.destroy()

    def action_Bt_calc(self):
        self.action_Total_Flamengo()
        self.action_Total_Vasco()
        
    def inicialize(self):
        self.__Lb_flamengo = Label(self, text="Flamengo", width=15, bg="yellow")
        self.__Lb_vasco = Label(self, text="Vasco", width=15, bg="yellow")
        self.__Lb_pr = Label(self, text="Paraná", width=12, bg="yellow")
        self.__Lb_sc = Label(self, text="Santa Catarina", width=12, bg="yellow")
        self.__Lb_rs = Label(self, text="Rio G. do Sul", width=12, bg="yellow")
        self.__Et_flamengo_pr = Entry(self, width=16)
        self.__Et_flamengo_sc = Entry(self, width=16)
        self.__Et_flamengo_rs = Entry(self, width=16)
        self.__Et_vasco_pr = Entry(self, width=16)
        self.__Et_vasco_sc = Entry(self, width=16)
        self.__Et_vasco_rs = Entry(self, width=16)
        self.__Bt_calc = Button(self, text="Calcular", command=self.action_Bt_calc)
        self.__Lb_torcida_total = Label(self, text="Torcida total:", width=15, bg="yellow")
        self.__Et_total_flamengo = Entry(self, width=16)
        self.__Et_total_vasco = Entry(self, width=16)
        
        self.__Lb_flamengo.grid(row=0, column=1, padx=4, pady=4)
        self.__Lb_vasco.grid(row=0, column=2, padx=4, pady=4)
        self.__Lb_pr.grid(row=1, column=0, padx=4, pady=4, sticky=W)
        self.__Lb_sc.grid(row=2, column=0, padx=4, pady=4, sticky=W)
        self.__Lb_rs.grid(row=3, column=0, padx=4, pady=4, sticky=W)
        self.__Et_flamengo_pr.grid(row=1, column=1, padx=4, pady=4, sticky=W)
        self.__Et_flamengo_sc.grid(row=2, column=1, padx=4, pady=4, sticky=W)
        self.__Et_flamengo_rs.grid(row=3, column=1, padx=4, pady=4, sticky=W)
        self.__Et_vasco_pr.grid(row=1, column=2, padx=4, pady=4, sticky=W)
        self.__Et_vasco_sc.grid(row=2, column=2, padx=4, pady=4, sticky=W)
        self.__Et_vasco_rs.grid(row=3, column=2, padx=4, pady=4, sticky=W)
        self.__Bt_calc.grid(row=4, column=1, padx=4, pady=4, sticky=W)
        self.__Lb_torcida_total.grid(row=5, column=0, padx=4, pady=4)
        self.__Et_total_flamengo.grid(row=5, column=1, padx=4, pady=4, sticky=W)
        self.__Et_total_vasco.grid(row=5, column=2, padx=4, pady=4, sticky=W)
        
        self.protocol("WM_DELETE_WINDOW", self.action_exit)
