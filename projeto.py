# Projeto da disciplina de Linguagem de Programação, pelas alunas:
# Camilla Thais Bezerra Spinola (turma 3A) e Lucila Gabriela Gomes Costa (turma 3B).

from tkinter import *
from tkinter import ttk
from pip._vendor import requests

from historico import Historico

# Configurções da Janela:
master = Tk()
master.title("Calculadora Multifuncional")
master.iconbitmap(default="calcu.ico")
master.geometry("403x653+490+20")
master.wm_resizable(width=False, height=False)

# importante a imagem de fundo:
calculadoraImg = PhotoImage(file="novo fundo.png")

# Label da Janela:
labelCalculadora = Label(master, image=calculadoraImg)
labelCalculadora.place(x=0, y=0)

historico = Historico(master)

# Funções da calculadora:
def calcular(op):
    global resposta, nume1, nume2, x

    try:
        float(nume1.get())
        float(nume2.get())

        if op == 1:
            x = float(nume1.get()) + float(nume2.get())

            historico.addCalcItem(
                valor1=nume1.get(), valor2=nume2.get(), operador="+", result=x
            )

        elif op == 2:
            x = float(nume1.get()) - float(nume2.get())

            historico.addCalcItem(
                valor1=nume1.get(), valor2=nume2.get(), operador="-", result=x
            )

        elif op == 3:
            try:
                x = float(nume1.get()) / float(nume2.get())

            except ZeroDivisionError:
                x = 999999999999

            historico.addCalcItem(
                valor1=nume1.get(), valor2=nume2.get(), operador="/", result=x
            )

        elif op == 4:
            x = float(nume1.get()) * float(nume2.get())

            historico.addCalcItem(
                valor1=nume1.get(), valor2=nume2.get(), operador="*", result=x
            )

        return resposta.config(text=round(x, 4))

    except ValueError:
        resposta.config(text="Só Números", font="Times 25")


def zerar():
    nume1.delete(0, END)
    nume2.delete(0, END)


def pegar():
    resultado = float(x)
    nume1.delete(0, END)
    nume1.insert(END, resultado)


# Funções do Conversor de Unidades:
def converter():
    try:
        op1 = menu1.get()
        op2 = menu2.get()
        entrada = float(num1.get())

        pos_op1 = listaOp.index(op1)
        pos_op2 = listaOp.index(op2)

        calculo = (listaPotencias[pos_op1] / listaPotencias[pos_op2]) * entrada

        res = str(format(calculo, ".1E"))

        historico.addConvItem(unidade=str(entrada) + " " + op1, saida=res + " " + op2)

        resultado["text"] = res

    except ValueError:
        resultado["text"] = "só números!"
    except ZeroDivisionError:
        resultado["text"] = "falta a unidade!"


def limpar():
    num1.delete(0, END)
    resultado["text"] = ""


def limparConv():
    # resultadoMoeda.delete(" ", END)
    resultadoMoeda["text"] = ""


''' Funções do Cotador:
def cotacoes():
    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    )

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    texto = f"""
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}"""
    resultadoCotacoes["text"] = texto
    historico.addCotasItem(cotacao_dolar, cotacao_euro, cotacao_btc)
    '''

def cotar(cot):
    global resultadoMoeda, dolar, euro, bitcoin

    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    )

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    try:

        if cot == 1:
            texto = f"""
            Dólar: {cotacao_dolar}"""
            resultadoMoeda["text"] = texto
            historico.addDolarItem(cotacao_dolar)

        elif cot == 2:
            texto = f"""
            Euro: {cotacao_euro}"""
            resultadoMoeda["text"] = texto
            historico.addEuroItem(cotacao_euro)

        elif cot == 3:
            texto = f"""
            BTC: {cotacao_btc}"""
            resultadoMoeda["text"] = texto
            historico.addBtcItem(cotacao_btc)

        # return resultadoMoeda.config(text=round(x, 4))

    except ValueError:
        resultadoMoeda.config(text="Só Números", font="Times 25")

    """historico.addCotasItem(cotacao_dolar, cotacao_euro, cotacao_btc)"""


# Construindo a Calculadora:

# resposta:
resposta = Label(master, font="Times 30", text="0", bg="light salmon")
resposta.place(width=348, height=60, x=31, y=70)

# botão historico:
btHistorico = Button(
    master,
    text="histórico",
    font="Times 15",
    command=lambda: historico.abrirJanelaDeHistorico(),
    bg="dark salmon",
)
btHistorico.place(width=80, height=27, x=327, y=0)

# botão pegar a resposta:
btpegar = Button(
    master,
    text="calcular",
    font="Times 13",
    bg="dark salmon",
    command=pegar,
)

btpegar.place(width=65, height=20, x=30, y=130)

# Criação dos botões da calculadora:
bt1 = Button(
    master, text="+", font="Arial 30", command=lambda: calcular(1), bg="dark salmon"
)
bt2 = Button(
    master,
    text="-",
    anchor=S,
    font="Arial 30",
    command=lambda: calcular(2),
    bg="dark salmon",
)
bt3 = Button(
    master, text="/", font="Arial 30", command=lambda: calcular(3), bg="dark salmon"
)
bt4 = Button(
    master,
    text="*",
    anchor=N,
    font="Arial 30",
    command=lambda: calcular(4),
    bg="dark salmon",
)

# Posicionar botões da calculadora:
bt1.place(width=76, height=51, x=30, y=215)
bt2.place(width=76, height=51, x=120, y=215)
bt3.place(width=76, height=51, x=209, y=215)
bt4.place(width=76, height=51, x=298, y=215)

# Caixas de entrada
nume1 = Entry(master, font="Times 20", justify=CENTER, bg="peach puff")
nume1.place(width=142, height=55, x=29, y=152)
nume2 = Entry(master, font="Times 20", justify=CENTER, bg="peach puff")
nume2.place(width=142, height=55, x=240, y=152)

# Valores iniciais de entrada(move o cursor da entrada dos números)
nume1.insert(END, "")
nume2.insert(END, "")

# Botão de limpar "ac":
bt5 = Button(
    master,
    text="ac",
    font=("Times 18 bold"),
    bg="dark salmon",
    fg="black",
    command=zerar,
)
bt5.place(width=55, height=55, x=178, y=152)


# Construindo o Conversor de Unidades:

listaOp = [
    "Nenhuma",
    "Mili (m)",
    "Micro (u)",
    "Nano  (n)",
    "Pico  (p)",
    "Unidade",
    "Quilo (k)",
    "Mega  (M)",
    "Giga  (G)",
    "Tera  (T)",
]

listaPotencias = [
    10 * 0,
    10**-3,
    10**-6,
    10**-9,
    10**-12,
    1,
    10**3,
    10**6,
    10**9,
    10**12,
]

# resultados:
resultado = Label(master, text="saída", font=("Times 20"), bg="light salmon")
resultado.place(width=164, height=32, x=210, y=327)

# Caixa para inserir os números:
num1 = Entry(master, font=("Times 17 "), justify=CENTER, bg="peach puff")
num1.place(width=164, height=32, x=31, y=327)
num1.insert(END, "")

# Opções de medidas da caixa de entrada:
menu1 = ttk.Combobox(master, value=listaOp, justify="center", font=("Times 15"))
menu1.place(width=132, height=32, x=42, y=382)
menu1.current(5)

# Opções de medidas que será transformada:
menu2 = ttk.Combobox(master, value=listaOp, justify="center", font=("Times 15"))
menu2.place(width=132, height=32, x=230, y=382)
menu2.current(0)

# Botão de limpar "limpar":
bt1 = Button(
    master,
    text="limpar",
    font=("Times 17 bold"),
    bg="dark salmon",
    fg="black",
    command=limpar,
)
bt1.place(width=98, height=42, x=61, y=437)

# Botão de limpar "deletar":
bt6 = Button(
    master,
    text="deletar",
    font=("Times 15 bold"),
    bg="dark salmon",
    fg="black",
    command=limparConv,
)
bt6.place(width=100, height=38, x=300, y=610)

# Botão de Converter:
bt2 = Button(
    master,
    text="converter",
    font=("Times 16 bold"),
    bg="dark salmon",
    fg="black",
    command=converter,
)
bt2.place(width=98, height=42, x=246, y=437)

# Botões de moedas:
bt7 = Button(
    master,
    text="dólar",
    font=("Times 13 bold"),
    bg="dark salmon",
    fg="black",
    command=lambda: cotar(1),
)
bt7.place(width=100, height=35, x=50, y=535)
bt8 = Button(
    master,
    text="euro",
    font=("Times 13 bold"),
    bg="dark salmon",
    fg="black",
    command=lambda: cotar(2),
)
bt8.place(width=100, height=35, x=150, y=535)
bt9 = Button(
    master,
    text="bitcoin",
    font=("Times 13 bold"),
    bg="dark salmon",
    fg="black",
    command=lambda: cotar(3),
)
bt9.place(width=100, height=35, x=250, y=535)


# Construindo o Cotador das moedas:

# resultado das atualizações das cotações:
resultadoMoeda = Label(master, text="", font=("Times 10 bold"), bg="light salmon")
resultadoMoeda.place(width=155, height=64, x=125, y=580)


# Botão de Atualizar a cotação:
"""bt3 = Button(
    master,
    text="atualize",
    font=("Times 16 bold"),
    bg="dark salmon",
    fg="black",
    command=cotacoes,
)
bt3.place(width=150, height=35, x=125, y=536)"""


# eventos da tela master:
master.mainloop()
