class kendaraan:
  def __init__ (self, name):
    self.name = name
    self.penumpang = []
  def tambah_penumpang(self, nama_penumpang):
    self. penumpang.append(nama_penumpang)

class mobil(kendaraan):
  pintu_terbuka = False
  def buka_pintu(self):
    self.pintu_terbuka = True
    def tutup_pintu(self):
      self.pintu_terbuka = False
      def welcome(self):
        print("selamat datang silahkan duduk")

mobil = mobi;("mobil nissan")
print(f"namakendaraan:{mobil.nama}")
mobil. tambah_penumpang("Ilham")
mobil. tambah_penumpang("Abel")

print(f"penumpang: {mobil.tambah_penumpang}")
mobil.buka_pintu()
print(f"namakendaraan:{mobil.pintu_terbuka}")
mobil. tutup_pintu()
print(f"namakendaraan:{mobil.pintu_terbuka}")
mobil.welcome()