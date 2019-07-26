class Luas():
    def __init__(self):
        self.alas = input("alas : ")
        self.tinggi = input("tinggi : ")
    def segipanjang(self):
        a = int(self.alas)
        t = int(self.tinggi)
        print("luas segipanjang =>")
        print(a*t)

class Volume():
    def __init__(self):
        self.p = input("panjang : ")
        self.l = input("lebar   : ")
        self.t = input("tinggi  : ")
    def balok(self):
        pa=int(self.p)
        le=int(self.l)
        ti=int(self.t)
        print("volume balok =>")
        print(pa*le*ti)

lu = Luas()
lu.segipanjang()
vol = Volume()
vol.balok()
