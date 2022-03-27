class Kelas:
    def __init__(self, nama):
        self.__nama = nama
        self._nama = nama
        self.nama = nama
        


if __name__ == "__main__":
    k = Kelas("Kelas")
    print(k._nama)
    print(k.nama)