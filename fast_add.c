#include <stdio.h>

#define MAX_SIZE 1000  // Adjust this size as needed

// Array to store data in the C module
int data_array[MAX_SIZE];

// Function to load data into the array
void load_data(int *array, int size) {
    if (size > MAX_SIZE) {
        size = MAX_SIZE;
    }
    for (int i = 0; i < size; i++) {
        data_array[i] = array[i];
    }
}

// Function to sum the array using assembly for optimization
int sum_array(int size) {
    int sum = 0;
    // Inline assembly to optimize summing the array
    for (int i = 0; i < size; i++) {
        __asm__ (
            "movl %1, %%eax;"  // Move array element into register
            "addl %%eax, %0;"  // Add register to sum
            : "=r" (sum)       // output
            : "r" (data_array[i]), "0" (sum)  // inputs
            : "%eax"           // clobbered register
        );
    }
    return sum;
}
