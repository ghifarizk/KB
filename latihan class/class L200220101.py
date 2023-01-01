class Persegi_Panjang(object):
    """data dan proses tentang bangun persegi panjang"""
    def __init__(self, panjang, lebar):
        self.p = panjang
        self.l = lebar
        
    def luas(self):
        l = self.p * self.l
        return l
    
bangun = Persegi_Panjang(8,5)
print (bangun.luas())