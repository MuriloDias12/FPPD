import subprocess
import time

print("🔄 Comparando desempenho entre execução sequencial e paralela...\n")

# Executar versão sequencial
inicio_seq = time.time()
subprocess.run(["python", "buscaSequencial.py"], check=True)
tempo_seq = time.time() - inicio_seq

# Executar versão paralela
inicio_par = time.time()
subprocess.run(["python", "BuscaParalela.py"], check=True)
tempo_par = time.time() - inicio_par

# Calcular speedup
speedup = tempo_seq / tempo_par if tempo_par > 0 else float('inf')

print("\n📊 RESULTADOS:")
print(f"Tempo sequencial: {tempo_seq:.6f} s")
print(f"Tempo paralelo:   {tempo_par:.6f} s")
print(f"Speedup obtido:   {speedup:.2f}x mais rápido com paralelismo 🚀")

