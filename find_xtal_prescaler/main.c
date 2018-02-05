#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

float xtals[] = {
    0.032768, 3.579545, 3.6864, 4.9152, 6, 7, 8, 9.833, 10, 
    10.245, 12, 13.56, 13.433, 14.318, 16, 16.384, 16.9344, 
    17.7344, 20, 20.48, 24, 25, 27, 27.12, 28.224, 32, 48, 
    50, 72

/*    0.032768, 0.038, 0.128, 3.579545, 3.6864, 4, 4.9152, 6, 7, 8, 9.833, 10, 
    10.245, 10.7, 12, 12.288, 13.56, 13.433, 14.318, 16, 16.384, 16.9344, 
    17.7344, 18.432, 20, 20.48, 22.1184, 24, 25, 27, 27.12, 28.224, 32, 48, 
    50, 54, 72
    */
}; 

#define N_XTALS sizeof(xtals) / sizeof(xtals[0])
#define N_DIFFS sizeof(xtals) / sizeof(xtals[0]) * 2

float diff[N_DIFFS] = {0};
int ids[N_DIFFS] = {0};

#define swap(a, b) do {typeof(a) _t; _t = (a); (a) = (b); (b) = _t;} while(0);

int main(void)
{
    int i;
    char buf[64];
    float freq;

    for(i = 0; i < N_XTALS; i++) {
        xtals[i] *= 1e6;
    } 
    while(1) {

        printf("Input needed frequency: "); 

        memset(buf, 0, 64);
        fgets(buf, 64, stdin);

        for(char *c = &(buf[strlen(buf) - 1]); *c == '\r' || *c == '\n';) { 
            *c = '\0'; 
            c = &(buf[strlen(buf) - 1]);
        }

        sscanf(buf, "%f", &freq);

        if(toupper(buf[strlen(buf) - 1]) == 'K')
            freq *= 1000.0;
        else if(toupper(buf[strlen(buf) - 1]) == 'M')
            freq *= 1000000.0;

        for(i = 0; i < N_XTALS; i++) {
            unsigned long div = xtals[i] / freq;
            diff[i * 2] = fabs(freq - xtals[i] / div);
            diff[i * 2 + 1] = fabs(freq - xtals[i] / (div + 1));
        } 

        for(i = 0; i < N_DIFFS; i++) 
            ids[i] = i;

        for(i = 0; i < N_DIFFS - 1; i++) {
            for(int j = i + 1; j < N_DIFFS; j++) {
                if(diff[i] > diff[j]) {
                    swap(diff[i], diff[j]);
                    swap(ids[i], ids[j]);
                }
            }
        }

        for(i = 0; i < 5; i++) { 
            int min_id = ids[i];
            int div = xtals[min_id / 2] / freq;
            float freq_d, err;

            if(min_id % 2 == 1)
                div++;
            freq_d = xtals[min_id / 2] / div;
            err = (freq_d - freq)  / freq * 1e6;
            printf("%.3fM / %d = %.1f (%s%.0fppm)\n", 
                    xtals[min_id / 2] / 1e6, div, freq_d, err > 0 ? "+" : "", err); 
        } 
        putchar('\n');
    }
    return 0;
} 
