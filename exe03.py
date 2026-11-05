import multiprocessing
import random
import time


# Função que controla cada sapo (cada processo/thread)
def sapo_corredor(id_sapo, distancia_maxima, salto_maximo):
  distancia_percorrida = 0
  salto_atual = 0

  print(
      f"--- Sapo #{id_sapo} largou! Precisa percorrer {distancia_maxima} cm"
      " ---"
  )

  # O loop continua até o sapo atingir ou ultrapassar a distância máxima
  while distancia_percorrida < distancia_maxima:
    # Sorteia um salto de 1 até o tamanho máximo (ex: 1 a 5 cm)
    salto_atual = random.randint(1, salto_maximo)

    # Acumula na distância total percorrida
    distancia_percorrida += salto_atual

    # Se passar da distância máxima, limita para ficar exato na linha de chegada
    if distancia_percorrida > distancia_maxima:
      distancia_percorrida = distancia_maxima

    # Mostra no console a narração do salto e quanto percorreu
    print(
        f"Sapo #{id_sapo} deu um pulo de {salto_atual} cm | Total percorrido:"
        f" {distancia_percorrida}/{distancia_maxima} cm"
    )

    # Pequeno atraso para dar efeito de narração em tempo real
    time.sleep(0.3)

  # Assim que percorrer a distância máxima, apresenta que o sapo chegou
  print(f"🏁 FIM DA LINHA! O Sapo #{id_sapo} CHEGOU! ")


def main():
  # Configurações da corrida
  total_sapos = 5
  distancia_maxima = 30  # Distância total que os sapos devem percorrer (em cm)
  salto_maximo = 5  # Tamanho máximo de cada pulo (de 1 a 5 cm)

  # Inicializando o vetor de parâmetros com [0] * 5
  parametros = [0] * total_sapos

  # Preenchendo o vetor com os parâmetros de cada sapo (id, distância máxima, salto máximo)
  for i in range(total_sapos):
    id_sapo = i + 1
    parametros[i] = (id_sapo, distancia_maxima, salto_maximo)

  print("=== INÍCIO DA CORRIDA DE SAPOS! ===")
  print(
      f"Distância total: {distancia_maxima} cm | Salto máximo por vez:"
      f" {salto_maximo} cm\n"
  )

  # Executa a corrida usando o Pool com starmap para múltiplos argumentos
  with multiprocessing.Pool(processes=total_sapos) as pool:
    pool.starmap(sapo_corredor, parametros)

  print("\n=== TODOS OS SAPOS CRUZARAM A CHEGADA! FIM DE JOGO ===")


if __name__ == "__main__":
  main()