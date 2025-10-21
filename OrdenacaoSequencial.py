import numpy as np
import time

def merge_sort_sequencial(arr):
 
    if len(arr) <= 1:
        return arr
    
    meio = len(arr) // 2
    esquerda = merge_sort_sequencial(arr[:meio])
    direita = merge_sort_sequencial(arr[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):

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

def main():
 
    vetor = np.load('A.npy')

    print(f"Primeiros 10 elementos (desordenados): {vetor[:10]}\n")
    
    print("--- ORDENAÇÃO SEQUENCIAL ---")
    inicio = time.time()
    vetor_ordenado = merge_sort_sequencial(vetor)
    tempo_decorrido = time.time() - inicio

    print(f"✓ Ordenação concluída!")

    print(f"Tempo de execução: {tempo_decorrido:.6f} segundos")

    np.save('vetor_ordenado_sequencial.npy', vetor_ordenado)
    print("\n✓ Vetor ordenado salvo em 'vetor_ordenado_sequencial.npy'")
    
    return vetor_ordenado, tempo_decorrido

if __name__ == "__main__":
    main()
