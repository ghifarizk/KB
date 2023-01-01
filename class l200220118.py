class Balok(object):
    """data dan proses tentang bangun balok"""
    def __init__(self, panjang, lebar, tinggi):
        self.p = panjang
        self.l = lebar
        self.t = tinggi
        
    def volume(self):
        v = self.p * self.l * self.t
        return v
    
bangun = Balok(6,4,3)
print (bangun.volume())
    