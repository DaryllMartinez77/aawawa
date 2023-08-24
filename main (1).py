def greeting(nama):
  print("halo", nama)
  
greeting("Rizky")

#fungsi mengembalikan nilai
def penjumlahan(a,b):
  hasil = a +b
  return hasil

hasil_penjumlahan = penjumlahan (7,9)
print("Hasil penjumlahan adalah", hasil_penjumlahan)
print(f"Hasil penjumlahan adalah {hasil_penjumlahan}")

#fungsi variable argumen
def jumlahkan (*args):
    total = 0
    for angka in args:
        total += angka
    return total

hasil = jumlahkan(12,30,40,50,5,3,7,0,700,1000)
print(f"hasil penjumlahan: {hasil}")

