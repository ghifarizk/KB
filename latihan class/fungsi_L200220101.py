print("TOKO OTOKO")
def total(harga,jumlah):
    """fungsi untuk menghitung Total bayar"""
    return harga*jumlah
#input data
harga= int(input("masukan harga barang: "))
jumlah= int(input("masukan jumlah barang yang dibeli: "))
Total=total(harga,jumlah)
print("Total Harga pembelian=",Total)
Bayar=int(input("Jumlah Nominal Uang =" ))
Kembalian= (Bayar-Total)
print("Uang Kembalian = ", "Rp.",Kembalian)