class Data_diri:
    def __init__(self, nama, alamat, tanggal_lahir):
        self.nama = nama
        self.alamat = alamat
        self.tangal_lahir = tanggal_lahir

DT = Data_diri("Riyo Adesvara Handi Santoso", "Madumulyo Pulisen Boyolali", "07 DESEMBER 2002")
print(DT.nama)
print(DT.alamat)
print(DT.tangal_lahir)
