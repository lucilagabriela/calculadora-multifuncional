from tkinter import *
from tkinter import ttk
import tkinter as tk


class Historico:

    master = None
    calculos = []
    conversoes = []
    cotas = []

    style = None

    frame = None

    def __init__(self, master):
        self.master = master

    def addCalcItem(self, valor1, valor2, operador, result):
        self.calculos.append(
            {"valor1": valor1, "valor2": valor2, "operador": operador, "result": result}
        )

    def addConvItem(self, unidade, saida):
        self.conversoes.append({"unidade": unidade, "saida": saida})

    """def addCotasItem(self, dolar, euro, btc):
        self.cotas.append({"dolar": dolar, "euro": euro, "btc": btc})"""

    def addDolarItem(self, dolar):
        self.cotas.append({"dolar": dolar})

    def addEuroItem(self, euro):
        self.cotas.append({"euro": euro})

    def addBtcItem(self, btc):
        self.cotas.append({"btc": btc})

    def abrirJanelaDeHistorico(self):

        newWindow = Toplevel(self.master)

        newWindow.title("Historico")

        newWindow.geometry("403x653+490+20")

        Label(newWindow, text="Historico").pack()

        frameButtons = Frame(newWindow)

        frameButtons.pack(ipadx=60, ipady=20)

        Button(
            frameButtons,
            text="CALC",
            command=lambda: self.filtrar(0),
        ).pack(side=LEFT, expand=True)

        Button(
            frameButtons,
            text="CONV",
            command=lambda: self.filtrar(1),
        ).pack(side=LEFT, expand=True)

        Button(
            frameButtons,
            text="COTAS",
            command=lambda: self.filtrar(2),
        ).pack(side=LEFT, expand=True)

        Button(
            frameButtons,
            text="TUDO",
            command=lambda: self.filtrar(4),
        ).pack(side=LEFT, expand=True)

        canvas = Canvas(newWindow)
        canvas.pack(side=LEFT, expand=1, fill=BOTH)

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scrollbar = Scrollbar(newWindow, command=canvas.yview)
        scrollbar.pack(side=LEFT, fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.bind("<Configure>", on_configure)

        self.frame = Frame(canvas)
        canvas.create_window(
            (0, 0),
            window=self.frame,
            anchor="nw",
            width=400,
        )

        self.atualizarLista()

    def atualizarLista(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.listarCalculos()
        self.listarConversoes()
        self.listarCotas()

    def filtrar(self, indice):

        for widget in self.frame.winfo_children():
            widget.destroy()

        if indice == 0:
            self.listarCalculos()
        elif indice == 1:
            self.listarConversoes()
        elif indice == 2:
            self.listarCotas()
        else:
            self.atualizarLista()

    def listarCalculos(self):

        for cal in self.calculos:

            calFrame = tk.Frame(self.frame)
            calFrame.pack(fill=X, expand=True)

            Label(calFrame, font="Times 14", text=cal["valor1"]).pack(
                side=LEFT, expand=True
            )
            Label(calFrame, font="Times 14", text=cal["operador"]).pack(
                side=LEFT, expand=True
            )
            Label(calFrame, font="Times 14", text=cal["valor2"]).pack(
                side=LEFT, expand=True
            )
            Label(calFrame, font="Times 14", text="=").pack(side=LEFT, expand=True)
            Label(calFrame, font="Times 14", text=cal["result"]).pack(
                side=LEFT, expand=True
            )

    def listarConversoes(self):

        for conv in self.conversoes:
            convFrame = Frame(self.frame)
            convFrame.pack(fill=X, expand=True)
            Label(convFrame, font="Times 14", text=conv["unidade"]).pack(
                side=LEFT, expand=True
            )
            Label(convFrame, font="Times 14", text=conv["saida"]).pack(
                side=LEFT, expand=True
            )

    def listarCotas(self):

        for cota in self.cotas:
            cotaFrame = Frame(self.frame)
            cotaFrame.pack(fill=X, expand=True)

            if "dolar" in cota:
                Label(cotaFrame, font="Times 14", text="dolar: " + cota["dolar"]).pack(
                    side=LEFT, expand=True
                )

            if "euro" in cota:
                Label(cotaFrame, font="Times 14", text="euro: " + cota["euro"]).pack(
                    side=LEFT, expand=True
                )

            if "btc" in cota:
                Label(cotaFrame, font="Times 14", text="btc: " + cota["btc"]).pack(
                    side=LEFT, expand=True
                )
