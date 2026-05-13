from musicas import Musica


class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Biblioteca:
    def __init__(self):
        self.cabeca = None
        self._contador = 0

    def inserir(self, titulo, artista, genero, bpm):
        if not isinstance(bpm, (int, float)) or bpm <= 0:
            print("BPM inválido.")
            return

        self._contador += 1
        nova_musica = Musica(self._contador, titulo, artista, genero, bpm)
        novo_nodo = NodoLista(nova_musica)

        if self.cabeca is None:
            self.cabeca = novo_nodo
            return

        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo_nodo

    def listar(self):
        if self.cabeca is None:
            print("A biblioteca está vazia.")
            return

        atual = self.cabeca
        while atual:
            atual.musica.exibir()
            atual = atual.proximo

    def buscar(self, valor):
        atual = self.cabeca

        while atual:
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

        while atual.proximo:
            if atual.proximo.musica.id == id_musica:
                atual.proximo = atual.proximo.proximo
                print("Música removida com sucesso.")
                return True
            atual = atual.proximo

        print("Música não encontrada.")
        return False


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
        novo = NodoFila(musica)

        if self.inicio is None:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    def dequeue(self):
        if self.inicio is None:
            print("Fila vazia.")
            return None

        musica = self.inicio.musica
        self.inicio = self.inicio.proximo
        self.tamanho -= 1

        if self.inicio is None:
            self.fim = None

        return musica

    def listar(self):
        if self.inicio is None:
            print("Fila vazia.")
            return

        atual = self.inicio
        while atual:
            atual.musica.exibir()
            atual = atual.proximo


def montar_filas_por_humor(biblioteca, relaxar, focar, animar, treinar):
    relaxar.__init__()
    focar.__init__()
    animar.__init__()
    treinar.__init__()

    atual = biblioteca.cabeca

    while atual:
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


def reproduzir_proxima(fila, historico):
    musica = fila.dequeue()

    if musica:
        print("\nReproduzindo agora:")
        musica.exibir()
        historico.enqueue(musica)


def exibir_estatisticas(
    biblioteca,
    fila_relaxar,
    fila_focar,
    fila_animar,
    fila_treinar,
    historico
):
    print("\n=== Estatísticas ===")
    print(f"Total na biblioteca: {biblioteca._contador}")
    print(f"Fila Relaxar: {fila_relaxar.tamanho}")
    print(f"Fila Focar: {fila_focar.tamanho}")
    print(f"Fila Animar: {fila_animar.tamanho}")
    print(f"Fila Treinar: {fila_treinar.tamanho}")
    print(f"Total reproduzidas: {historico.tamanho}")