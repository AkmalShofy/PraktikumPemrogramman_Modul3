#include <stdio.h>
int main() {
int a,b,c,d,e,g;
printf("Masukkan Jumlah Detik : ");
scanf("%d", &e);
a = e / 86400;
b = e % 86400;
c = b / 3600;
g = b % 3600;
d = g / 60;
e = g % 60;
if (a>0) {printf("%d hari %.2d:%.2d:%.2d",a,c,d,e);}
else {printf("%.2d:%.2d:%.2d",c,d,e);}
}