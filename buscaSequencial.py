import numpy as np
import time

def busca_sequencial(vetor, numero):
    for i in range(len(vetor)):
        if vetor[i] == numero:
            return i
    return None

def main():
  
    vetor = np.load('A.npy')
   
    numero_buscado = 789665541
    
    inicio = time.time()
    posicao = busca_sequencial(vetor, numero_buscado)
    tempo_decorrido = time.time() - inicio
    
    if posicao is not None:
        print(f"Número {numero_buscado} encontrado na posição: {posicao}")
    else:
        print(f"Número {numero_buscado} não encontrado")
    return posicao, tempo_decorrido

if __name__ == "__main__":
    main()