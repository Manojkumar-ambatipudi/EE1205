
#include <stdio.h>
float ap_values(float x0, float d, int n){
	return x0 + n*d;
}

int main()
{
    FILE *fp = fopen("data.dat", "w");
    float sum = 0;
    for (int i= 0; i<13; i++){
        sum +=ap_values(0.5, 0.5, i);
        fprintf(fp,"%d\t%.2f\t%.2f\n", i, ap_values(0.5, 0.5, i), sum);
    }
    fclose(fp);
}

