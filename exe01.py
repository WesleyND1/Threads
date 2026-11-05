import multiprocessing
import time

def tarefa(id):

  # Sleep de 0.5 segundos
    time.sleep(0.5)
  # Inicializa o id
    print("Thread #", id)

    print("Thread #", id, "terminou")


def main():
  # 1. Inicializa o vetor com [0] * 5 (posições)
  parametros = [0] * 5

  # 2. Preenche o vetor com os valores do id
  for i in range(5):
    parametros[i] = i  # Preenche com 0, 1, 2, 3, 4 (total de 5)

  # 3. Uso do 'with' com .map
  with multiprocessing.Pool(processes=5) as threads:
    # O .map distribui os itens do vetor um a um para a função 'tarefa'
    threads.map(tarefa, parametros)


if __name__ == "__main__":
  main()