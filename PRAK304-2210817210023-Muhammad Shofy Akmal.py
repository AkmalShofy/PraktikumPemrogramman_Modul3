a = float(input("Masukkan Bilangan Cacah : "))
if a == 0:
    print ("Nol")
elif 0<a<10 :
    print ("Satuan")
elif 10<a<20 :
    print ("Belasan")
elif  a>=100 :
    print ("Anda Menginput Melebihi Limit Bilangan") 
else :
    print ("Puluhan")