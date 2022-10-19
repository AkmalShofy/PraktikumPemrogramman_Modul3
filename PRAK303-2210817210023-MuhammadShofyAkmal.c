#include <stdio.h>
int main () {
float N;
printf ("Masukkan Bilangan : "); scanf ("%f", &N);
if (N > 0) {printf ("Positif");}
else if (N < 0) {printf ("Negatif");}
else {printf ("Nol");}
}