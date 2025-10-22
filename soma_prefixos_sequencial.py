import numpy as np
import time

def soma_prefixos_sequencial(A):
   
    B = np.zeros_like(A)
    soma = 0
    for i in range(len(A)):
        soma += A[i]
        B[i] = soma
    return B

def main():
    print("Carregando ou gerando vetor A...")
    try:
        A = np.load("A.npy")
    except FileNotFoundError:
        A = np.random.randint(1, 100, size=50000)
        np.save("A.npy", A)
    print(f"Vetor A com {len(A)} elementos carregado.")

    inicio = time.time()
    B = soma_prefixos_sequencial(A)
    tempo = time.time() - inicio

    print(f"✓ Soma de prefixos (sequencial) concluída em {tempo:.6f} segundos.")
    np.save("B_sequencial.npy", B)
    return tempo

if __name__ == "__main__":
    main()
