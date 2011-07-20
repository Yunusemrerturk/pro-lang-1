#include <stdio.h>

faktoriyel(sayi){
        if (sayi==0)
                return 1;
        int ilk=1;
        while (sayi!=0){
                ilk *= sayi;
                sayi--;
        }
        return ilk;
}

main(void){
        printf("%d\n",faktoriyel(4));
}

