#imports:
#Permite detectar e responder a eventos do teclado.
import keyboard
#Permite manipular o tempo, como atrasos e pausas.
import time
#Permite manipular o sistema, como encerrar o programa. usei pra encerrar o programa.
import sys
#Permite contar quantas vezes cada palavra aparece no texto. usei pra contar palavras mais frequentes.
from collections import Counter
#Expressões regulares, usadas para encontrar padrões em texto. usei pra evitar que o código contasse pontuação como palavras/junto com palavras.
import re
#Permite abrir uma caixa de diálogo para selecionar arquivos. usei pra selecionar o arquivo de texto.
import easygui
#apresentação do projeto:
print("Sejam bem vindos ao projeto final da disciplina Língua e Programação 2025.1! O projeto consiste em uma ferramenta concordanciadora feita para analisar textos em .txt. O projeto foi desenvolvido por: Eduardo de Melo Cavalcante e Guilherme Ferreira de Oliveira.")

#comando pra iniciar o programa e Loop principal:
print("Para iniciar o programa, pressione <Enter>.")
while True:
    input()
    print("""
Ferramentas disponíveis:

| 1 - File Review |  
    → Exibe o conteúdo do arquivo.

| 2 - Word |  
    → Conta as palavras mais frequentes.

| 3 - Cluster |  
    → (Ainda não implementada)

| 4 - N-Gram |  
    → Exibe as associações mais comuns do texto.

| 5 - Kwic |  
    → (Ainda não implementada)
""")

#introdução das ferramentas:
    escolha_de_ferramentas = input("Escolha uma ferramenta digitando o nome ou número dela: ").strip().lower()
    if escolha_de_ferramentas not in ["file review", "word", "cluster", "n-gram", "kwic","1","2","3","4","5"]:
        print("Ferramenta inválida. Tente novamente pressionando <Enter>.")
        continue
#codigo pra puxar texto de arquivo, nessa posição o codigo vai funcionar em todas as ferramentas:
    print("Escolha os arquivos de texto que deseja analisar.")
    time.sleep(1)
    print("Uma janela de seleção de arquivo foi aberta.\nEm certos programas como VS CODE a janela de seleção é aberta atrás desta janela.")
    caminho_arquivo = easygui.fileopenbox(msg="Selecione o arquivo de texto (.txt)", filetypes=["*.txt"], multiple=True)
    if not caminho_arquivo:
        print("Nenhum arquivo selecionado. tente novamente pressionando <Enter>.")
        continue
    textos = []
    for caminho in caminho_arquivo:
        with open(caminho, encoding="utf-8") as f:
            textos.append(f.read())
    texto_completo = "\n".join(textos)

#codigo pro File Review:
    if escolha_de_ferramentas == "file review" or escolha_de_ferramentas == "1":
            print("Você escolheu a ferramenta File Review.")
            time.sleep(2)
            print("-" * 80)
            File_review = texto_completo
            print(File_review)
            print("-" * 80)

#codigo pro Word:
    elif escolha_de_ferramentas == "word" or escolha_de_ferramentas == "2":
        print("Você escolheu a ferramenta Word.")
        time.sleep(2)
        print("-" * 150)
        texto_Word = texto_completo.lower()
        words = re.findall(r'\b\w+\b', texto_Word)
        counts = Counter(words)
        mais_frequentes = counts.most_common()
        print(mais_frequentes)
        print("-" * 150)

#codigo pro Cluster:
    elif escolha_de_ferramentas == "cluster" or escolha_de_ferramentas == "3":
        print("Você escolheu a ferramenta Cluster.")
        time.sleep(2)
        print("-" * 150)


#codigo pro N-Gram:
    elif escolha_de_ferramentas == "n-gram" or escolha_de_ferramentas == "4":
        print("Você escolheu a ferramenta N-Gram.")
        time.sleep(2)
        print("-" * 150)
        texto_ngram = texto_completo.lower()
        words_ngram = re.findall(r'\b\w+\b', texto_ngram)
        nextword = iter(words_ngram)
        next(nextword)
        freq = Counter(zip(words_ngram, nextword))
        print(freq)
        print("-" * 150)

#codigo pro Kwic:
    elif escolha_de_ferramentas == "kwic" or escolha_de_ferramentas == "5":
        print("Você escolheu a ferramenta Kwic.")


# Loop para voltar ao menu principal ou encerrar o programa
    print("Digite <barra de espaço> para continuar ou <esc> para encerrar o programa: ")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'space':
                print("Voltando ao menu principal... Pressione <Enter> para continuar.")
                break
        elif event.name == 'esc':
            print("Programa está encerrando...")
            time.sleep(4)
            sys.exit()

