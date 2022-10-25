e = int (input ("Masukkan Jumlah Detik : "))
a = int (e / 86400)
b = int (e % 86400)
c = int (b / 3600)
f = int (b % 3600)
d = int (f / 60)
e = int (f % 60)
if (a>0) :
    print("%d hari %.2d:%.2d:%.2d" %(a,c,d,e))
else     :
    print("%.2d:%.2d:%.2d"% (c,d,e))