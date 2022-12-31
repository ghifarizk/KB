class segitiga(object):
    def __init__(self, alas, tinggi):
       self.a = alas
       self.t = tinggi

    def luas(self): #ini adalah method
        """ Mengembalikan luas jajargenjang ini """
        L = self.a * self.t / 2
        return L

bangun = segitiga(4, 26)
print (bangun.luas())