import numpy as np
import time

def multiplicacao_matrizes_sequencial(A, B):
    # Verifica se as dimensões são compatíveis
    assert A.shape[1] == B.shape[0], "As matrizes não podem ser multiplicadas!"

    linhas_A, colunas_A = A.shape
    linhas_B, colunas_B = B.shape

    # Cria matriz resultado C com zeros
    C = np.zeros((linhas_A, colunas_B))

    # Multiplicação sequencial
    for i in range(linhas_A):
        for j in range(colunas_B):
            soma = 0
            for k in range(colunas_A):
                soma += A[i, k] * B[k, j]
            C[i, j] = soma
    return C


def main():
    print("Gerando matrizes A (200x400) e B (400x100)...")

    # Gera as matrizes aleatórias
    A = np.random.randint(1, 100, size=(200, 400))
    B = np.random.randint(1, 100, size=(400, 100))

    print("Iniciando multiplicação sequencial...")
    inicio = time.time()
    C = multiplicacao_matrizes_sequencial(A, B)
    tempo = time.time() - inicio

    print(f"✓ Multiplicação concluída em {tempo:.4f} segundos.")
    print(f"Dimensão da matriz resultante: {C.shape}")

    # Salva a matriz resultado
    np.save("C_sequencial.npy", C)
    return tempo


if __name__ == "__main__":
    main()
