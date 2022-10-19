#include <stdio.h>
int main () {
float a,b,c;
printf ("Masukkan Angka Pertama : "); scanf ("%f", &a);
printf ("Masukkan Angka Kedua   : "); scanf ("%f", &b);
printf ("Masukkan Angka Ketiga  : "); scanf ("%f", &c);
if      (a<b & b<c) {printf ("%.0f %.0f %.0f", a,b,c);}
else if (b<a & a<c) {printf ("%.0f %.0f %.0f", b,a,c);}
else if (c<a & a<b) {printf ("%.0f %.0f %.0f", c,a,b);}
else if (b<c & c<a) {printf ("%.0f %.0f %.0f", b,c,a);}
else if (c<b & b<a) {printf ("%.0f %.0f %.0f", c,b,a);}
else  {printf ("%.0f %.0f %.0f", a,c,b);}
}