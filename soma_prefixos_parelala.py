import numpy as np
import time
import multiprocessing as mp

def soma_prefixo_parcial(subarray):

    parcial = np.zeros_like(subarray)
    soma = 0
    for i in range(len(subarray)):
        soma += subarray[i]
        parcial[i] = soma
    return parcial, soma

def soma_prefixos_paralela(A, num_processos=4):
  
    tamanho = len(A)
    passo = tamanho // num_processos
    fatias = [A[i*passo:(i+1)*passo] for i in range(num_processos - 1)]
    fatias.append(A[(num_processos - 1)*passo:])

    with mp.Pool(processes=num_processos) as pool:
        resultados = pool.map(soma_prefixo_parcial, fatias)

    
    prefixos, somas = zip(*resultados)
    somas_acumuladas = np.cumsum([0] + list(somas[:-1]))

    
    B = np.zeros_like(A)
    pos = 0
    for i in range(num_processos):
        B[pos:pos+len(prefixos[i])] = prefixos[i] + somas_acumuladas[i]
        pos += len(prefixos[i])

    return B

def main():
    mp.freeze_support()
    print("Carregando vetor A...")
    A = np.load("A.npy")
    print(f"Vetor A com {len(A)} elementos carregado.")

    num_processos = 3
    inicio = time.time()
    B = soma_prefixos_paralela(A, num_processos)
    tempo = time.time() - inicio

    print(f"✓ Soma de prefixos (paralela) concluída em {tempo:.6f} segundos usando {num_processos} processos.")
    np.save("B_paralela.npy", B)
    return tempo

if __name__ == "__main__":
    main()
