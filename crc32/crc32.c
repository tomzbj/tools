#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

unsigned long polynormial = 0xedb88320;

static unsigned long crc32(unsigned long crc, unsigned char* msg, int size) 
{
    for(int i = 0; i < size; i++) {
        crc ^= msg[i];
        for(int j = 0; j < 8; j++) {
            bool lsb = crc % 2;
            crc >>= 1;
            if(lsb)
                crc ^= polynormial;
        } 
    }
    return crc;
} 

int main(int argc, char* argv[])
{
    if(argc != 2)
        exit(1);

    FILE* fp = fopen(argv[1], "rb"); 
    if(fp == NULL)
        exit(1);

    unsigned char buf[256];
    int n;
    unsigned long crc = 0xffffffff;
    while((n = fread(buf, 1, 256, fp)) > 0) {
        crc = crc32(crc, buf, n); 
    } 
    printf("0x%08lx\n", ~crc); 
    fclose(fp);

    return 0;
}
