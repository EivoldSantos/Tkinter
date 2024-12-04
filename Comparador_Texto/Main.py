import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas.
from tkinter import filedialog, messagebox  # Importa filedialog para abrir arquivos e messagebox para exibir mensagens.
import re  # Importa a biblioteca re para trabalhar com expressões regulares.
from collections import Counter  # Importa Counter para contar elementos de forma eficiente.

def analisar_texto(texto):
    """Analisa o texto e retorna as estatísticas."""
    # Contar palavras
    palavras = re.findall(r'\b\w+\b', texto.lower())  # Encontra todas as palavras no texto, convertendo para minúsculas.
    num_palavras = len(palavras)  # Conta o número total de palavras.

    # Contar frases
    frases = re.split(r'[.!?]+', texto)  # Divide o texto em frases usando pontuações como delimitadores.
    num_frases = len([frase for frase in frases if frase.strip()])  # Conta as frases não vazias.

    # Frequência de palavras
    frequencia_palavras = Counter(palavras)  # Conta a frequência de cada palavra no texto.

    # Palavra mais frequente
    palavra_mais_frequente = frequencia_palavras.most_common(1)  # Obtém a palavra mais frequente e sua contagem.
    palavra_frequente = palavra_mais_frequente[0] if palavra_mais_frequente else (None, 0)  # Define a palavra mais frequente ou None se não houver.

    # Contagem de tipos de caracteres
    letras = sum(c.isalpha() for c in texto)  # Conta o número total de letras no texto.
    numeros = sum(c.isdigit() for c in texto)  # Conta o número total de dígitos no texto.
    pontuacao = sum(not c.isalnum() and not c.isspace() for c in texto)  # Conta o número total de caracteres de pontuação.

    return {
        "num_palavras": num_palavras,  # Retorna o número total de palavras.
        "num_frases": num_frases,  # Retorna o número total de frases.
        "frequencia_palavras": frequencia_palavras,  # Retorna um dicionário com a frequência das palavras.
        "palavra_frequente": palavra_frequente,  # Retorna a palavra mais frequente e sua contagem.
        "letras": letras,  # Retorna o total de letras.
        "numeros": numeros,  # Retorna o total de números.
        "pontuacao": pontuacao  # Retorna o total de caracteres de pontuação.
    }

def carregar_arquivo():
    """Carrega o texto de um arquivo e atualiza a entrada."""
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])  # Abre um diálogo para escolher um arquivo .txt.
    if caminho_arquivo:  # Verifica se um arquivo foi selecionado.
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:  # Abre o arquivo para leitura com codificação UTF-8.
                texto = arquivo.read()  # Lê todo o conteúdo do arquivo.
                entry_texto.delete(1.0, tk.END)  # Limpa o campo de entrada antes de inserir novo texto.
                entry_texto.insert(tk.END, texto)  # Insere o texto lido no campo de entrada.
        except Exception as e:  # Captura qualquer erro que ocorra ao abrir ou ler o arquivo.
            messagebox.showerror("Erro", f"Não foi possível ler o arquivo: {e}")  # Exibe uma mensagem de erro.

def analisar():
    """Realiza a análise do texto inserido pelo usuário."""
    texto = entry_texto.get("1.0", tk.END).strip()  # Obtém o texto inserido pelo usuário e remove espaços em branco nas extremidades.

    if not texto:  # Verifica se algum texto foi inserido.
        messagebox.showwarning("Aviso", "Por favor, insira um texto ou carregue um arquivo.")  # Exibe um aviso se não houver texto.
        return
    
    resultado = analisar_texto(texto)  # Chama a função para analisar o texto e armazena os resultados.

    # Exibe os resultados na interface
    resultado_texto = (
        f"Número de palavras: {resultado['num_palavras']}\n"  # Adiciona o número total de palavras ao resultado.
        f"Número de frases: {resultado['num_frases']}\n"      # Adiciona o número total de frases ao resultado.
        f"Palavra mais frequente: '{resultado['palavra_frequente'][0]}' "
        f"(ocorrências: {resultado['palavra_frequente'][1]})\n"  # Adiciona a palavra mais frequente e sua contagem ao resultado.
        f"Frequência das palavras:\n"
    )
    
    for palavra, contagem in resultado['frequencia_palavras'].items():  
        resultado_texto += f"'{palavra}': {contagem}\n"  # Adiciona a frequência de cada palavra ao resultado.

    resultado_texto += (
        f"\nTotal de letras: {resultado['letras']}\n"   # Adiciona o total de letras ao resultado.
        f"Total de números: {resultado['numeros']}\n"   # Adiciona o total de números ao resultado.
        f"Total de pontuação: {resultado['pontuacao']}"   # Adiciona o total de caracteres de pontuação ao resultado.
    )
    
    messagebox.showinfo("Resultados da Análise", resultado_texto)  # Exibe os resultados da análise em uma caixa de mensagem.

# Criando a janela principal
root = tk.Tk()  
root.title("Analisador de Texto")  # Define o título da janela principal.

# Frame para entrada de texto
frame_entrada = tk.Frame(root)  
frame_entrada.pack(pady=10)  

tk.Label(frame_entrada, text="Insira seu texto ou carregue um arquivo:").pack()  
# Cria um rótulo pedindo ao usuário para inserir seu texto ou carregar um arquivo.

entry_texto = tk.Text(frame_entrada, width=50, height=10)  
entry_texto.pack(pady=5)  
# Cria uma área de texto onde o usuário pode digitar ou colar seu texto.

# Botão para carregar arquivo
btn_carregar = tk.Button(root, text="Carregar Arquivo", command=carregar_arquivo)  
btn_carregar.pack(pady=5)  
# Cria um botão que permite ao usuário carregar um arquivo .txt.

# Botão para analisar o texto
btn_analisar = tk.Button(root, text="Analisar Texto", command=analisar)  
btn_analisar.pack(pady=10)  
# Cria um botão que inicia a análise do texto quando clicado.

# Inicia a aplicação
root.mainloop()  
# Inicia o loop principal da interface gráfica, permitindo que a janela permaneça aberta e responda às interações do usuário.