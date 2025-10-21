import numpy as np
import time
import multiprocessing as mp
from multiprocessing import Pool

def merge_sort_sequencial(arr):
    """
    Merge sort sequencial (usado nos chunks).
    """
    if len(arr) <= 1:
        return arr
    
    meio = len(arr) // 2
    esquerda = merge_sort_sequencial(arr[:meio])
    direita = merge_sort_sequencial(arr[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    """
    Mescla dois vetores ordenados.
    """
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return np.array(resultado)

def ordenar_chunk(chunk):
    """
    Ordena um chunk do vetor (executado em paralelo).
    """
    return merge_sort_sequencial(chunk)

def merge_chunks(chunks):
    """
    Mescla todos os chunks ordenados em um único vetor ordenado.
    """
    while len(chunks) > 1:
        novos_chunks = []
        for i in range(0, len(chunks), 2):
            if i + 1 < len(chunks):
                mesclado = merge(chunks[i], chunks[i + 1])
                novos_chunks.append(mesclado)
            else:
                novos_chunks.append(chunks[i])
        chunks = novos_chunks
    return chunks[0]

def ordenacao_paralela(vetor, num_processos=4):
    """
    Ordenação paralela usando merge sort distribuído.
    """
    vetor_copia = vetor.copy()
    tamanho_chunk = len(vetor_copia) // num_processos
    chunks = []

    for i in range(num_processos):
        inicio = i * tamanho_chunk
        fim = (i + 1) * tamanho_chunk if i != num_processos - 1 else len(vetor_copia)
        chunks.append(vetor_copia[inicio:fim])
    
    with Pool(processes=num_processos) as pool:
        chunks_ordenados = pool.map(ordenar_chunk, chunks)
    
    return merge_chunks(chunks_ordenados)

def main():
    mp.freeze_support()

    print("Carregando arquivo .npy...")
    vetor = np.load('A.npy')
    print(f"Vetor carregado com {len(vetor)} elementos")
    print(f"Primeiros 10 elementos (desordenados): {vetor[:10]}\n")
    
    num_processos = 8
    print(f"Usando {num_processos} processos paralelos")
    
    print("--- ORDENAÇÃO PARALELA ---")
    inicio = time.time()
    vetor_ordenado = ordenacao_paralela(vetor, num_processos)
    tempo_decorrido = time.time() - inicio
    
    print(f"✓ Ordenação concluída!")
    print(f"Primeiros 10 elementos (ordenados): {vetor_ordenado[:10]}")
    print(f"Últimos 10 elementos (ordenados): {vetor_ordenado[-10:]}")
    print(f"Tempo de execução: {tempo_decorrido:.6f} segundos")
    print(f"Processos utilizados: {num_processos}")
    
    np.save('vetor_ordenado_paralelo.npy', vetor_ordenado)
    print("\n✓ Vetor ordenado salvo em 'vetor_ordenado_paralelo.npy'")
    
    return vetor_ordenado, tempo_decorrido

if __name__ == "__main__":
    main()
