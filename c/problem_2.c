#include <stdio.h>
#include <stdbool.h>


int main() {
    int aux;
    int previous = 1;
    int actual = 2;
    long sum = actual;
    bool stopCondition = true;

    // for (int i = 2; i < 4E6; i++) {
    //     aux = previous;
    //     previous = actual;
    //     actual = previous + aux;
    //     if (actual % 2 == 0) {
    //         sum += actual;
    //     }
    // }

    while (stopCondition == true) {
        aux = previous;
        previous = actual;
        actual = previous + aux;
        if (actual % 2 == 0) {
            sum += actual;
        }
        if (actual > 4E6) {
            stopCondition = false;
        }
    }
    printf("sum: %li", sum);
    return 0;
}