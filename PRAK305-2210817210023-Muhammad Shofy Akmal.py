e = float(input("Masukkan Jumlah Detik : "))
a = e / 86400
b = e % 86400
c = b / 3600
f = b % 3600
d = f / 60
e = f % 60
print ("%.0f hari %.0f:%.0f:%.0f" % (a,c,d,e))