import numpy as np
import multiprocessing as mp
import time

def multiplica_linha(args):
    """
    Multiplica uma única linha de A pela matriz B.
    """
    linha, B = args
    return np.dot(linha, B)

def multiplicacao_matrizes_paralela(A, B, num_processos=4):
    """
    Multiplica as matrizes A e B em paralelo usando multiprocessing.
    Retorna a matriz resultante C.
    """
    # Preparar lista de tarefas (cada linha de A será uma tarefa)
    tarefas = [(A[i, :], B) for i in range(A.shape[0])]

    # Pool de processos
    with mp.Pool(processes=num_processos) as pool:
        linhas_resultantes = pool.map(multiplica_linha, tarefas)

    # Reconstituir a matriz resultante
    C = np.vstack(linhas_resultantes)
    return C

def main():
    mp.freeze_support()

    print("Gerando matrizes A (200x400) e B (400x100)...")
    np.random.seed(42)
    A = np.random.randint(1, 100, size=(200, 400))
    B = np.random.randint(1, 100, size=(400, 100))

    num_processos = 8
    print(f"Usando {num_processos} processos paralelos\n")

    inicio = time.time()
    C = multiplicacao_matrizes_paralela(A, B, num_processos)
    tempo = time.time() - inicio

    print(f"✓ Multiplicação paralela concluída em {tempo:.6f} segundos.")
    print(f"Matriz resultante C tem formato: {C.shape}")
    print("Primeiras 3 linhas da matriz resultante:\n", C[:3, :5])  # mostra parte da matriz
    np.save("C_paralela.npy", C)

    return tempo

if __name__ == "__main__":
    main()
