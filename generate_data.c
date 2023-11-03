#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to calculate the distance between two points
double calculate_distance(int x1, int y1, int x2, int y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

int main() {
    FILE *file = fopen("viz.csv", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the header to the CSV file
    fprintf(file, "x1,y1,x2,y2,distance\n");

    // We will iterate from 0 to 10000 to generate numbers for both generators
    for (int i = 0; i <= 1000; ++i) {
        for (int j = 0; j <= 1000; ++j) {
            // We exclude pairs where the two numbers are the same
            if (i != j) {
                double distance = calculate_distance(i, i, j, j);
                fprintf(file, "%d,%d,%d,%d,%f\n", i, i, j, j, distance);
            }
        }
    }

    // Close the file
    fclose(file);

    printf("viz.csv file has been created with the dataset.\n");
    return 0;
}

