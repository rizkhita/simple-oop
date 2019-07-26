class Kelas () :
    def __init__ (self) :
        self.variabel = "variabel"
    def metode (self) :
        print(self.variabel)
    def panggil (self) :
        self.metode()

wadah = Kelas()
wadah.method()
wadah.panggil()
