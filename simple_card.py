class Siswa():
    def __init__(self):
        self.nama = input("nama : ")
        self.nim = input("nim : ")
    def make_card(self):
        print("-------------ID CARD-----------")
        print("nama siswa : "+ format(self.nama))
        print("nim siswa  : "+ format(self.nim))
        print("-------------------------------")
    def panggilsiswa(self):
        self.siswa()

data_diri = Siswa()
data_diri.make_card()

