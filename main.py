# Criacao do projeto 2 - Orientado pelo professor Orlando Saraiva  - E.de Dados.
# Parte 1 - Criacao das classes

class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def remover_musica(self, musica):
        self.musicas.remove(musica)

    def exibir_musicas(self):
        for musica in self.musicas:
            print(f"Título: {musica.titulo}, Artista: {musica.artista}, Duração: {musica.duracao}")
