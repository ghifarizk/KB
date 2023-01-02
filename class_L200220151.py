class tiket:
    def __init__(self,nama,harga,tribun,sektor):
        self.nama = nama
        self.harga = harga
        self.tribun = tribun
        self.sektor = sektor
    def nama(self):
        return self.nama


    def harga(self):
        return self.harga

    def tribun(self):
        return self.tribun

    def sektor(self):
        return self.sektor

d = tiket("Rohmad","Rp100.000","2","Barat")

print("Berikut Pesanan Anda:")
print('Nama     :',d.nama)
print('Harga    :',d.harga)
print('Tribun   :',d.tribun)
print('Sektor   :',d.sektor)
