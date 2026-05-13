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