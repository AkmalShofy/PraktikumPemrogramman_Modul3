#include <stdio.h>
int main () {
float a;
printf ("Masukkan Bilangan Cacah : "); scanf ("%f", &a);
if (a==0) {printf ("Nol");}
else if (0<a<10) {printf ("Satuan");}
else if (10<a<20) {printf ("Belasan");}
else if (a>=100) {printf ("Anda Menginput Melebihi Limit Bilangan");}
else {printf ("Puluhan");}
}