import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas.
from tkinter import messagebox  # Importa a classe messagebox para exibir mensagens de erro e informações.
import random  # Importa a biblioteca random para gerar números aleatórios.

# Definindo as características de cada tipo de loteria
lottery_types = {
    "Mega Sena": {"range": (1, 60), "count": 6},  # Mega Sena: números de 1 a 60, sorteia 6 números.
    "Quina": {"range": (1, 80), "count": 5},      # Quina: números de 1 a 80, sorteia 5 números.
    "Lotofácil": {"range": (1, 25), "count": 15}, # Lotofácil: números de 1 a 25, sorteia 15 números.
}

def gerar_numeros(tipo):
    """Gera números aleatórios para o tipo de loteria escolhido."""
    range_start, range_end = lottery_types[tipo]["range"]  # Extrai o intervalo de números da loteria escolhida.
    count = lottery_types[tipo]["count"]  # Obtém a quantidade de números a serem sorteados.
    return random.sample(range(range_start, range_end + 1), count)  # Retorna uma amostra aleatória de números.

def validar_numeros(numeros_usuario, tipo):
    """Valida os números informados pelo usuário."""
    range_start, range_end = lottery_types[tipo]["range"]  # Extrai o intervalo de números da loteria escolhida.
    count = lottery_types[tipo]["count"]  # Obtém a quantidade de números esperada.
    
    if len(numeros_usuario) != count:  # Verifica se o número de entradas do usuário é igual ao esperado.
        raise ValueError(f"Você deve inserir exatamente {count} números.")  # Lança um erro se não for igual.
    
    for numero in numeros_usuario:  # Itera sobre os números fornecidos pelo usuário.
        if numero < range_start or numero > range_end:  # Verifica se cada número está dentro do intervalo permitido.
            raise ValueError(f"Números devem estar entre {range_start} e {range_end}.")  # Lança um erro se fora do intervalo.

def comparar_numeros(numeros_sorteados, numeros_usuario):
    """Compara os números sorteados com os números do usuário."""
    acertos = set(numeros_sorteados).intersection(set(numeros_usuario))  # Encontra a interseção entre os números sorteados e os do usuário.
    return len(acertos), acertos  # Retorna a quantidade de acertos e os próprios acertos.

def jogar():
    """Função principal para executar o jogo."""
    tipo = var_tipo_loteria.get()  # Obtém o tipo de loteria selecionado pelo usuário.
    
    try:
        numeros_sorteados = gerar_numeros(tipo)  # Gera os números sorteados com base no tipo escolhido.
        
        # Obtendo os números do usuário
        numeros_usuario_input = entry_numeros.get()  # Captura a entrada do usuário como uma string.
        numeros_usuario = list(map(int, numeros_usuario_input.split(',')))  # Converte a string em uma lista de inteiros.

        # Validando os números do usuário
        validar_numeros(numeros_usuario, tipo)  # Valida os números informados pelo usuário.

        # Comparando os números
        acertos_count, acertos = comparar_numeros(numeros_sorteados, numeros_usuario)  # Compara os números sorteados com os do usuário.

        # Exibindo resultados
        resultado = f"Números sorteados: {sorted(numeros_sorteados)}\n"  # Formata a saída dos números sorteados em ordem crescente.
        resultado += f"Seus números: {sorted(numeros_usuario)}\n"  # Formata a saída dos números do usuário em ordem crescente.
        resultado += f"Quantidade de acertos: {acertos_count}\n"  # Adiciona a quantidade de acertos ao resultado.

        if acertos_count == lottery_types[tipo]["count"]:  # Verifica se o usuário acertou todos os números.
            resultado += "Parabéns! Você acertou todos os números!"  # Mensagem de parabéns se todos os números foram acertados.

        messagebox.showinfo("Resultados", resultado)  # Exibe uma caixa de mensagem com os resultados.

    except ValueError as e:  
        messagebox.showerror("Erro", str(e))  # Exibe uma mensagem de erro se houver um problema na validação dos números.
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")  # Exibe uma mensagem genérica para outros erros inesperados.

# Criando a janela principal
root = tk.Tk()  
root.title("Simulador de Loteria")  # Define o título da janela principal.

# Variável para armazenar o tipo de loteria escolhido
var_tipo_loteria = tk.StringVar(value="Mega Sena")  # Inicializa a variável com o valor padrão "Mega Sena".

# Frame para seleção do tipo de loteria
frame_tipo_loteria = tk.Frame(root)  
frame_tipo_loteria.pack(pady=10)  

tk.Label(frame_tipo_loteria, text="Escolha o tipo de loteria:").pack()  
# Cria um rótulo pedindo ao usuário para escolher um tipo de loteria.

for tipo in lottery_types.keys():  
    tk.Radiobutton(frame_tipo_loteria, text=tipo, variable=var_tipo_loteria, value=tipo).pack(anchor=tk.W)
    # Cria botões de opção (radiobuttons) para cada tipo de loteria disponível.

# Frame para entrada dos números do usuário
frame_entrada = tk.Frame(root)  
frame_entrada.pack(pady=10)  

tk.Label(frame_entrada, text="Insira seus números (separados por vírgula):").pack()  
# Cria um rótulo pedindo ao usuário para inserir seus números.

entry_numeros = tk.Entry(frame_entrada, width=30)  
entry_numeros.pack(pady=5)  
# Cria um campo de entrada onde o usuário pode digitar seus números.

# Botão para jogar
btn_jogar = tk.Button(root, text="Jogar", command=jogar)  
btn_jogar.pack(pady=10)  
# Cria um botão que inicia o jogo quando clicado.

# Inicia a aplicação
root.mainloop()  
# Inicia o loop principal da interface gráfica, permitindo que a janela permaneça aberta e responda às interações do usuário.