a = float(input("Masukkan Angka Pertama : "))
b = float(input("Masukkan Angka Kedua   : "))
c = float(input("Masukkan Angka Ketiga  : "))
if   (a<b<c) :
    print ("%.0f %.0f %.0f" % (a,b,c))
elif (b<a<c) :
    print ("%.0f %.0f %.0f" % (b,a,c))
elif (c<a<b) :
    print ("%.0f %.0f %.0f" % (c,a,b))
elif (b<c<a) :
    print ("%.0f %.0f %.0f" % (b,c,a))
elif (c<b<a) :
    print ("%.0f %.0f %.0f" % (c,b,a))
else             :
    print ("%.0f %.0f %.0f" % (a,c,b))