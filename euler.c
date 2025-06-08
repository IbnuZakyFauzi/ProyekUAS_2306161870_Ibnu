#include <stdio.h>

#define g 9.81       //percepatan gravitasi (m/s^2)
#define dt 0.1       //langkah waktu (s)
#define xo 100.0     //posisi awal (m)
#define vo 0.0       //kecepatan awal (m/s)

int main() {
    double t = 0.0;       //waktu
    double x = xo;        //ketinggian
    double v = vo;        //kecepatan
    int i = 0;

    printf("Langkah\tWaktu(s)\tPosisi(m)\tKecepatan(m/s)\n");

    // Iterasi menggunakan Euler
    while (x > 0) {
        printf("%d\t%.2f\t\t%.3f\t\t%.3f\n", i, t, x, v);

        // Update ketinggian dan kecepatan
        x = x - v * dt;
        v = v + g * dt;
        t = t + dt;
        i++;
    }

    //iterasi saat benda menyentuh tanah
    printf("%d\t%.2f\t\t%.3f\t\t%.3f\n", i, t, x, v);

    return 0;
}
