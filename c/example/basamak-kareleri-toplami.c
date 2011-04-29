#include <stdio.h>

int bkt(sayi){
        int son=0;
        while (sayi!=0){
                son += sayi%10;
                sayi = sayi/10;
        }
        return son;
}

main(void){
        printf("%d\n",bkt(13));
}

