from estruturas import *

biblioteca = Biblioteca()

fila_relaxar = Fila()
fila_focar = Fila()
fila_animar = Fila()
fila_treinar = Fila()
historico = Fila()

biblioteca.inserir("Weightless", "Marconi Union", "Ambient", 60)
biblioteca.inserir("Lofi Study", "ChilledCow", "Lo-fi", 85)
biblioteca.inserir("Eye of the Tiger", "Survivor", "Rock", 109)
biblioteca.inserir("Lose Yourself", "Eminem", "Rap", 171)
biblioteca.inserir("Bohemian Rhapsody", "Queen", "Rock", 72)
#buscar por ID
print("\n=== Buscando por ID 2 ===")

resultado = biblioteca.buscar(2)

if resultado:
    resultado.exibir()
else:
    print("Música não encontrada.")

print("\n=== Biblioteca ===")
biblioteca.listar()

montar_filas_por_humor(
    biblioteca,
    fila_relaxar,
    fila_focar,
    fila_animar,
    fila_treinar
)

print("\n=== Fila Relaxar ===")
fila_relaxar.listar()

print("\n=== Reproduzindo próxima ===")
reproduzir_proxima(fila_relaxar, historico)

print("\n=== Histórico ===")
historico.listar()

exibir_estatisticas(
    biblioteca,
    fila_relaxar,
    fila_focar,
    fila_animar,
    fila_treinar,
    historico
)