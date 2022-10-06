#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LENGTH 100
#define SIZE 8

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("wis-untar: tar-file\n");
        exit(1);
    }
    FILE *A;
    FILE *B;
    A = fopen(argv[1], "r");
    if (A == NULL) {
        printf("wis-untar: cannot open file\n");
        exit(1);
    }
    char *buf;
    buf = (char *)malloc(LENGTH);
    long n;
    int t;
    t = fread(buf, 1, LENGTH, A);
    while (t == LENGTH) {
        B = fopen(buf, "w");
        fread(&n, SIZE, 1, A);
        buf = (char *)realloc(buf, n);
        fread(buf, 1, n, A);
        fwrite(buf, 1, n, B);
        fclose(B);
        buf = (char *)malloc(LENGTH);
        t = fread(buf, 1, LENGTH, A); 
    }
    fclose(A);


    return 0;
}