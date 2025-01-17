# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    # Windows
    if name == 'nt':
      _ = system('cls')
        
    # Mac ou Linux
    else:
        _ = system('clear')

# Função
def game():
  
  limpa_tela()
  
  print("\nBem-vindo(a) ao jogo da forca!")
  print("Adivinhe a palavra abaixo:\n")
  
  # Lista de palavras para o jogo
  palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
  
  # Escolhe randomicamente uma palavra
  palavra = random.choice(palavras)