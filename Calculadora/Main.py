from tkinter import *
import math

# Inicializa a janela principal
calculadora = Tk()
calculadora.title("Calculadora Trigonométrica")

# Labels e entradas para os catetos
CatetoAdjacente = Label(calculadora, text="Insira o cateto adjacente:")
CatetoAdjacente.pack(side=LEFT)

InputCA = Entry(calculadora, bd=5)
InputCA.pack()

CatetoOposto = Label(calculadora, text="Insira o cateto oposto:")
CatetoOposto.pack(side=LEFT)

InputCO = Entry(calculadora, bd=5)
InputCO.pack()

label_resultado = Label(calculadora, text="")
label_resultado.pack(pady=10)

def pegar_valor():
    ca = float(InputCA.get())
    co = float(InputCO.get())
    return ca, co

def calculo(ca, co):
    
    hipotenusa = math.sqrt(ca**2 + co**2)
    
    seno = co / hipotenusa
    cosseno = ca / hipotenusa
    tangente = co / ca
    AnguloCos = math.degrees(cosseno)
    AnguloSeno = math.degrees(seno)
    AnguloTan = math.degrees(tangente)
    
    resultado_texto = (f"Hipotenusa: {hipotenusa:.2f}\n"
                       f"Seno: {seno:.2f}\n"
                       f"Cosseno: {cosseno:.2f}\n"
                       f"Tangente: {tangente:.2f}\n"
                       f"Angulo Seno: {AnguloSeno:.2f}°\n"
                       f"Angulo Cosseno: {AnguloCos:.2f}°\n"
                       f"Angulo Tangente: {AnguloTan:.2f}°")
                           
    label_resultado.config(text=resultado_texto)
    label_resultado.pack(side=BOTTOM)

def calcular():
    """Função que obtém os valores e chama a função de cálculo."""
    ca, co = pegar_valor()  
    calculo(ca, co) 

botao = Button(calculadora, text="Calcular", command=calcular)
botao.pack(pady=5)

calculadora.mainloop()