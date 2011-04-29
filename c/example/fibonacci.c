#include <stdio.h>

fibonacci(sayi){
        int ilk=0, son=1, bas;
        while (ilk<=sayi){
                printf("%d " , ilk);
                bas = ilk;
                ilk = son;
                son = son+bas;
        }
        printf("\n");
}

main(void){
        fibonacci(8);
}

