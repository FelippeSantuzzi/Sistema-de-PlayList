# Sistema de Playlist Inteligente

Sistema desenvolvido em Python para gerenciamento de músicas utilizando **estruturas de dados encadeadas**, sem uso de `list`, `deque` ou qualquer estrutura pronta do Python para armazenar os dados principais.

O projeto simula uma biblioteca musical capaz de organizar músicas, montar filas de reprodução e manter histórico das músicas reproduzidas.

---

## Funcionalidades

### Biblioteca Musical

Gerencia todas as músicas cadastradas através de uma **lista encadeada simples**.

Operações disponíveis:

- Adicionar músicas
- Buscar músicas por **ID** ou **título**
- Remover músicas da biblioteca
- Listar todas as músicas cadastradas

---

### Filas de Reprodução (FIFO)

As músicas são organizadas automaticamente em filas de reprodução de acordo com o BPM (*batidas por minuto*).

| Categoria | Faixa de BPM |
|-----------|--------------|
| Relaxar   | até 80       |
| Focar     | 81 a 120     |
| Animar    | 121 a 160    |
| Treinar   | acima de 160 |

As filas seguem a lógica **FIFO (First In, First Out)**, onde a primeira música inserida é a primeira a ser reproduzida.

---

### Reprodução de Músicas

Ao reproduzir uma música, o sistema:

1. Remove a música do início da fila (`dequeue`)
2. Exibe a música atualmente em reprodução
3. Registra automaticamente a música no histórico

---

### Histórico de Reprodução

Todas as músicas reproduzidas são armazenadas em uma **fila separada**, preservando a ordem original de execução.

---

### Estatísticas do Sistema

O sistema apresenta:

- Total de músicas cadastradas na biblioteca
- Quantidade de músicas em cada fila de humor
- Total de músicas já reproduzidas

---

## Estrutura do Projeto

```text
sistema_playlist/
├── main.py
├── estruturas.py
├── musicas.py
└── README.md
```

### `musicas.py`

Contém a classe `Musica`, responsável por representar cada música cadastrada.

---

### `estruturas.py`

Contém:

#### Lista encadeada

- `NodoLista`
- `Biblioteca`

#### Fila FIFO

- `NodoFila`
- `Fila`

#### Funções auxiliares

- `montar_filas_por_humor()`
- `reproduzir_proxima()`
- `exibir_estatisticas()`

---

### `main.py`

Arquivo responsável pela execução e demonstração do funcionamento completo do sistema.

---

## Requisitos atendidos

- Implementação manual com **nós encadeados**
- Sem uso de `list`, `deque` ou estruturas prontas
- Histórico implementado como instância separada da classe `Fila`
- Geração automática de IDs
- IDs não reutilizados após remoção
- Reconstrução completa das filas
- Tratamento de entradas inválidas:
  - BPM não numérico
  - BPM menor ou igual a zero
  - ID inexistente
  - Fila vazia ao tentar reproduzir

---

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

---

## Conceitos aplicados

- Programação Orientada a Objetos (POO)
- Lista Encadeada
- Fila FIFO
- Manipulação de nós
- Modularização de código

---

Projeto desenvolvido para prática de estruturas de dados em Python.