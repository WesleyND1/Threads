import multiprocessing
import random
import time


# Função que cada "thread" (processo) vai executar
def calcula_soma(id_linha, valores):
  soma = 0

  # Cada iteração do laço para a soma seguido por sleep de 0.2 segundos
  for valor in valores:
    soma += valor
    time.sleep(0.2)

  # Ao final, imprime a identificação da linha e o resultado da soma
  print("ID da linha:", id_linha, "| Resultado da soma:", soma)


def main():
  # Vetor de parâmetros inicializado com [0] * 3 (para 3 chamadas)
  parametros = [0] * 3

  for i in range(3):
    # 1. Inicializa uma variável id inteira
    id_val = i + 1

    # 2. Inicializa 5 variáveis inteiras para valores, cada uma de 1 a 100
    val1 = random.randint(1, 100)
    val2 = random.randint(1, 100)
    val3 = random.randint(1, 100)
    val4 = random.randint(1, 100)
    val5 = random.randint(1, 100)

    # Vetor com os 5 valores recebidos
    vetor_valores = [val1, val2, val3, val4, val5]

    # 3. Cria o vetor de parâmetros (id como primeiro, vetor de valores como segundo)
    parametros[i] = (id_val, vetor_valores)

  # 4. Faz as 3 chamadas usando o Pool e starmap (já que são múltiplos argumentos)
  with multiprocessing.Pool(processes=3) as pool:
    pool.starmap(calcula_soma, parametros)


if __name__ == "__main__":
  main()