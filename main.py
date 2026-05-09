# Criacao do projeto 2 - Orientado pelo professor Orlando Saraiva  - E.de Dados.
# Parte 1 - Criacao das classes



class Musica:
    # Criacao de uma faixa musical (caixinha magica - piada interna)

    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def exibir(self):
        print(f"  [{self.id}] {self.titulo} — {self.artista}")
        print(f"       Gênero: {self.genero} | BPM: {self.bpm}")


class NodoLista:
    #carrega uma musica e tem um ponteiro para o próximo nó. (FIFO)

    def __init__(self, musica):
        self.musica = musica
        self.proximo = None  



if __name__ == "__main__":

    # Criando Musicas
    m1 = Musica(1, "Weightless", "Marconi Union", "Ambient", 60)
    m2 = Musica(2, "Lofi Study", "ChilledCow", "Lo-fi", 85)
    m3 = Musica(3, "Eye of the Tiger", "Survivor", "Rock", 109)

    # Nos para cada musica
    nodo1 = NodoLista(m1)
    nodo2 = NodoLista(m2)
    nodo3 = NodoLista(m3)

    
    nodo1.proximo = nodo2
    nodo2.proximo = nodo3
    
    print("=== Músicas encadeadas ===\n")

    atual = nodo1  # começa no primeiro elo
    while atual is not None:
        atual.musica.exibir()
        atual = atual.proximo  # avança para o próximo elo

    print("\nFim da corrente!")