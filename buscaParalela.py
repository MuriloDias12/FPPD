import numpy as np
import time
import multiprocessing as mp
from multiprocessing import Pool

def buscar_chunk(args):

    chunk, numero, offset = args
    for i in range(len(chunk)):
        if chunk[i] == numero:
            return offset + i
    return None

def busca_paralela(vetor, numero, num_processos=4):

    tamanho_chunk = len(vetor) // num_processos
    chunks = []
    
    for i in range(num_processos):
        inicio = i * tamanho_chunk
        if i == num_processos - 1:
            fim = len(vetor)
        else:
            fim = (i + 1) * tamanho_chunk
        chunks.append((vetor[inicio:fim], numero, inicio))
    
   
    with Pool(processes=num_processos) as pool:
        resultados = pool.map(buscar_chunk, chunks)
    
    
    for resultado in resultados:
        if resultado is not None:
            return resultado
    return None

def main():
    
    mp.freeze_support()
    
    vetor = np.load('A.npy')

    
    

    numero_buscado = 789665541
   
    num_processos = 8
   
    
    inicio = time.time()
    posicao = busca_paralela(vetor, numero_buscado, num_processos)
    tempo_decorrido = time.time() - inicio


    if posicao is not None:
        print(f"Número {numero_buscado} encontrado na posição: {posicao}")
    else:
        print(f"Número {numero_buscado} não encontrado")
    return posicao, tempo_decorrido

if __name__ == "__main__":
    main()
