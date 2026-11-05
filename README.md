# Exercícios de Programação Concorrente e Paralela em Python

Repositório dedicado aos exercícios desenvolvidos durante os estudos de **Processos e Threads** utilizando a biblioteca nativa `multiprocessing` em Python.

Como todos os scripts utilizam apenas a **Biblioteca Padrão** do Python (`multiprocessing`, `random`, `time`), você não precisa instalar nenhuma dependência externa!

---

## Lista de Exercícios

| Exercício | Descrição | Conceitos Aplicados |
| :--- | :--- | :--- |
| **[exe01.py](exercicio-01-threads-simples/exe01.py) - Thread Simples** | Impressão básica com identificadores e atraso temporizado. | `multiprocessing`, `time.sleep`, Vetores estáticos `[0] * n` |
| **[exe02.py](exercicio-02-multiprocessing-soma/exe02.py) - Soma com Vetor** | Geração de valores aleatórios e cálculo de somas em paralelo. | `starmap`, `random.randint`, Múltiplos argumentos |
| **[exe03.py](exercicio-03-corrida-de-sapos/exe03.py) - Corrida de Sapos** | Simulação interativa e narrada de uma corrida concorrente. | Loops concorrentes, Condições de parada, `Pool` |

---

### Detalhes dos Exercícios

#### Exercício 03: Corrida de Sapos
Uma simulação interativa via console que narra o progresso de 5 sapos competindo.
* **Como funciona:** Cada processo representa um sapo que realiza saltos aleatórios (de 1 a 5 cm) a cada iteração até atingir a linha de chegada.

