
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


class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Biblioteca:
    
    #Lista encadeada simples que guarda todas as músicas.

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
            print("  A biblioteca está vazia.")
            return

        atual = self.cabeca
        while atual is not None:
            atual.musica.exibir()
            atual = atual.proximo

  
    def buscar(self, valor):
        atual = self.cabeca
        while atual is not None:
            musica = atual.musica
            # compara por id se valor for número, ou por título se for texto
            if musica.id == valor or musica.titulo.lower() == str(valor).lower():
                return musica   # achou — devolve o objeto Musica
            atual = atual.proximo
        return None  # não encontrou


# TESTE


if __name__ == "__main__":
    biblioteca = Biblioteca()

    print("=== Adicionando músicas ===\n")
    biblioteca.inserir("Weightless",      "Marconi Union", "Ambient", 60)
    biblioteca.inserir("Lofi Study",      "ChilledCow",    "Lo-fi",   85)
    biblioteca.inserir("Eye of the Tiger","Survivor",      "Rock",    109)
    biblioteca.inserir("Lose Yourself",   "Eminem",        "Rap",     171)

    print("=== Biblioteca completa ===\n")
    biblioteca.listar()

    print("\n=== Buscando por id 2 ===\n")
    resultado = biblioteca.buscar(2)
    if resultado:
        resultado.exibir()
    else:
        print("  Música não encontrada.")

    print("\n=== Buscando por título 'Lose Yourself' ===\n")
    resultado = biblioteca.buscar("Lose Yourself")
    if resultado:
        resultado.exibir()
    else:
        print("  Música não encontrada.")

    print("\n=== Buscando id que não existe (99) ===\n")
    resultado = biblioteca.buscar(99)
    if resultado:
        resultado.exibir()
    else:
        print("  Música não encontrada.")