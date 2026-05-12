class Musica:
    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def exibir(self):
        print(f"  [{self.id}] {self.titulo} — {self.artista}")
        print(f"       Gênero: {self.genero} | BPM: {self.bpm}")



# LISTA ENCADEADA (Biblioteca)


class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Biblioteca:
    def __init__(self):
        self.cabeca = None
        self._contador = 0

    def inserir(self, titulo, artista, genero, bpm):
        self._contador += 1
        nova_musica = Musica(self._contador, titulo, artista, genero, bpm)
        novo_nodo = NodoLista(nova_musica)

        if self.cabeca is None:
            self.cabeca = novo_nodo
            return

        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo_nodo

    def listar(self):
        if self.cabeca is None:
            print("A biblioteca está vazia.")
            return

        atual = self.cabeca
        while atual is not None:
            atual.musica.exibir()
            atual = atual.proximo

    def buscar(self, valor):
        atual = self.cabeca

        while atual is not None:
            musica = atual.musica

            if musica.id == valor or musica.titulo.lower() == str(valor).lower():
                return musica

            atual = atual.proximo

        return None

    def remover(self, id_musica):
        if self.cabeca is None:
            print("Biblioteca vazia.")
            return False

        if self.cabeca.musica.id == id_musica:
            self.cabeca = self.cabeca.proximo
            print("Música removida com sucesso.")
            return True

        atual = self.cabeca

        while atual.proximo is not None:
            if atual.proximo.musica.id == id_musica:
                atual.proximo = atual.proximo.proximo
                print("Música removida com sucesso.")
                return True

            atual = atual.proximo

        print("Música não encontrada.")
        return False



# FIFO


class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enqueue(self, musica):
        novo_nodo = NodoFila(musica)

        if self.inicio is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo

        self.tamanho += 1

    def dequeue(self):
        if self.inicio is None:
            print("Fila vazia.")
            return None

        musica_removida = self.inicio.musica
        self.inicio = self.inicio.proximo
        self.tamanho -= 1

        if self.inicio is None:
            self.fim = None

        return musica_removida

    def listar(self):
        if self.inicio is None:
            print("Fila vazia.")
            return

        atual = self.inicio

        while atual is not None:
            atual.musica.exibir()
            atual = atual.proximo


# FILAS POR HUMOR


def montar_filas_por_humor(biblioteca, relaxar, focar, animar, treinar):
    # limpa filas antigas
    relaxar.__init__()
    focar.__init__()
    animar.__init__()
    treinar.__init__()

    atual = biblioteca.cabeca

    while atual is not None:
        musica = atual.musica
        bpm = musica.bpm

        if bpm <= 80:
            relaxar.enqueue(musica)

        elif bpm <= 120:
            focar.enqueue(musica)

        elif bpm <= 160:
            animar.enqueue(musica)

        else:
            treinar.enqueue(musica)

        atual = atual.proximo

    print("Filas de humor montadas com sucesso.")


# Teste

if __name__ == "__main__":
    biblioteca = Biblioteca()

    fila_relaxar = Fila()
    fila_focar = Fila()
    fila_animar = Fila()
    fila_treinar = Fila()
    historico = Fila()

    print("=== Adicionando músicas ===\n")
    biblioteca.inserir("Weightless", "Marconi Union", "Ambient", 60)
    biblioteca.inserir("Lofi Study", "ChilledCow", "Lo-fi", 85)
    biblioteca.inserir("Eye of the Tiger", "Survivor", "Rock", 109)
    biblioteca.inserir("Lose Yourself", "Eminem", "Rap", 171)

    print("\n=== Biblioteca completa ===\n")
    biblioteca.listar()

    print("\n=== Buscando por id 2 ===\n")
    resultado = biblioteca.buscar(2)
    if resultado:
        resultado.exibir()
    else:
        print("Música não encontrada.")

    print("\n=== Removendo música id 3 ===\n")
    biblioteca.remover(3)

    print("\n=== Biblioteca após remoção ===\n")
    biblioteca.listar()

    print("\n=== Montando filas por humor ===\n")
    montar_filas_por_humor(
        biblioteca,
        fila_relaxar,
        fila_focar,
        fila_animar,
        fila_treinar
    )

    print("\n=== Fila Relaxar ===")
    fila_relaxar.listar()

    print("\n=== Fila Focar ===")
    fila_focar.listar()

    print("\n=== Fila Animar ===")
    fila_animar.listar()

    print("\n=== Fila Treinar ===")
    fila_treinar.listar()