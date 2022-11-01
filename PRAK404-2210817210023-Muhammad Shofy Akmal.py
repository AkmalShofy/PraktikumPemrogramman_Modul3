w=1
while w==1 :
    print("Pilih program\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Exit")
    print("Masukkan Pilihan : ", end=''); a = int(input())
    if a<1 or a>5 : 
        print("Input anda salah, silahkan coba lagi\n")
    elif a==5 : 
        print("Terimakasih, telah menggunakan kalkulator Akmal"); break
    else : 
        print("Masukkan Nilai Pertama : ", end=''); b=float(input())
        print("Masukkan Nilai Kedua   : ", end=''); c=float(input())
        if a==1 : print("Hasil Penjumlahan antara %.2f dengan %.2f adalah %.2f\n" % (b,c,b+c))
        elif a==2 : print("Hasil Pengurangan antara %.2f dengan %.2f adalah %.2f\n" % (b,c,b-c))
        elif a==3 : print("Hasil Perkalian antara %.2f dengan %.2f adalah %.2f\n" % (b,c,b*c))
        else : print("Hasil Pembagian antara %.2f dengan %.2f adalah %.2f\n" % (b,c,b/c))