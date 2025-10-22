import subprocess
import time

print("🔄 Comparando desempenho entre execução sequencial e paralela...\n")


inicio_seq = time.time()
subprocess.run(["python", "multiplicacao_matrizes_sequencial.py"], check=True)
tempo_seq = time.time() - inicio_seq

inicio_par = time.time()
subprocess.run(["python", "multiplicacao_matrizes_paralela.py"], check=True)
tempo_par = time.time() - inicio_par

speedup = tempo_seq / tempo_par if tempo_par > 0 else float('inf')

print("\n📊 RESULTADOS:")
print(f"Tempo sequencial: {tempo_seq:.6f} s")
print(f"Tempo paralelo:   {tempo_par:.6f} s")
print(f"Speedup obtido:   {speedup:.2f}x mais rápido com paralelismo 🚀")

