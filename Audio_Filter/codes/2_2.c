#include <stdio.h>
#include <math.h>

int main() {
    int N = 20, i;
    double x_values[6] = {1.0, 2.0, 3.0, 4.0, 2.0, 1.0}, y_values[20];
    FILE *fp = fopen("y_n_output.txt", "w");

    y_values[0] = x_values[0];
    y_values[1] = -0.5 * y_values[0] + x_values[1];
    fprintf(fp, "%lf\n%lf\n", y_values[0], y_values[1]);

    for (i = 2; i <= N - 1; i++) {
        if (i < 6)
            y_values[i] = -0.5 * y_values[i - 1] + x_values[i] + x_values[i - 2];
        else if (i > 5 && i < 8)
            y_values[i] = -0.5 * y_values[i - 1] + x_values[i - 2];
        else
            y_values[i] = -0.5 * y_values[i - 1];
        fprintf(fp, "%lf\n", y_values[i]);
    }

    fclose(fp);
    return 0;
}

