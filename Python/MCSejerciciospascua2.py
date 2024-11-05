class Cancion:
    def __init__(self, titulo="", autor=""):
        self.titulo = titulo
        self.autor = autor

    def dame_titulo(self):
        return self.titulo

    def dame_autor(self):
        return self.autor

    def pon_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def pon_autor(self, nuevo_autor):
        self.autor = nuevo_autor

cancion1 = Cancion("Dame tu cosita", "El Chombo")
print("Título:", cancion1.dame_titulo())
print("Autor:", cancion1.dame_autor())

cancion1.pon_titulo("Rizzler")
cancion1.pon_autor("Jelli House")
print("Título actualizado:", cancion1.dame_titulo())
print("Autor actualizado:", cancion1.dame_autor())