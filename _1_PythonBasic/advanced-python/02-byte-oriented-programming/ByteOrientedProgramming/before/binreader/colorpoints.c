/**
 *  colorpoints.c
 *
 *  A C99 program to write a colored vertex
 *  structures to a binary file.
 *
 */

#include <stdio.h>

struct Vector {
    float x;
    float y;
    float z;
};

struct Color {
    unsigned short int red;
    unsigned short int green;
    unsigned short int blue;
};

struct Vertex {
    struct Vector position;
    struct Color color;
};

int main(int argc, char** argv) {
    struct Vertex vertices[] = {
        { .position = { 3323.176, 6562.231, 9351.231 },
          .color = { 3040, 34423, 54321 } },

        { .position = { 7623.982, 2542.231, 9823.121 },
          .color = { 32736, 5342, 2321 } },

        { .position = { 6729.862, 2347.212, 3421.322 },
          .color = { 45263, 36291, 36701 } },

        { .position = { 6352.121, 3432.111, 9763.232 },
          .color = { 56222, 36612, 11214 } } };

    FILE* file = fopen("colors.bin", "wb");

    if (file == NULL) {
        return -1;
    }

    fwrite(vertices, sizeof(struct Vertex), 4, file);
    fclose(file);

    return 0;
}
