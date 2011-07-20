#include <stdio.h>

bs(sayi){
        int bas=0;
        if (sayi==0)
                return 1;
        while (sayi!=0){
                sayi = sayi/10;
                bas++;
        }
        return bas;
}

main(void){
        printf("%d\n",bs(341));
}


