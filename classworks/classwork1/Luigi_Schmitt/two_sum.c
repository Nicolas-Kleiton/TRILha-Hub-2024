// Two sum in C

#include <stdio.h>

void two_sum(int* nums, int numsSize, int target) {
    int found = 0; // Flag para verificar se encontramos algum par

    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                if (!found) {
                    printf("True\n");
                    found = 1; // Definimos que encontramos pelo menos um par e imprimimos True por isso
                }
                printf("[%d, %d]\n", nums[i], nums[j]);
            }
        }
    }

    if (!found) { // Caso não haja nenhuma soma igual o target aqui vai ficar 0! = 1 e irá rodar o False
        printf("False\n");
    }
}

int main() {
    int nums[] = {1, 2, 3, 4}; // Define um array de inteiros
    int target = 5;
    int numsSize = sizeof(nums) / sizeof(nums[0]); // 16 bytes divido por 4 bytes = 4 elementos na lista (são int)

    two_sum(nums, numsSize, target);

    return 0;
}
