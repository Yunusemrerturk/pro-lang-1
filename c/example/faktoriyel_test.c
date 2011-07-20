#include <stdio.h>

void Fakt_Test(int x, int f_x){
        int tmp1 = x;
        int tmp2 = f_x;

        if (x == 0 && f_x == 1)
                printf("\n0 ! == 1 ifadesi gecerlidir.\n");
        else if (x<0 && f_x==-2)
                printf("\n%d ! == %d ifadesi gecerlidir.\n", tmp1, tmp2);
        else if (x<12 && f_x==-1)
                printf("\n%d ! == %d ifadesi gecerlidir.\n", tmp1, tmp2);
        else {
                while (x != 1)
                        f_x = f_x / x--;
                if (f_x == 1)
                        printf("\n%d ! == %d ifadesi gecerlidir.\n", tmp1, tmp2);
                else
                        printf("\n%d ! == %d ifadesi gecerli degildir.\n", tmp1, tmp2);
        }
}

int Faktoriyel(int x){
        int f = 1;
        if (x<0)
                return -2;
        else if (x==0)	       
                return 1;
        else if (x>=13)
                return -1;

        while (x != 1)
                f = f * x--;
        return f;
}

int main(void){
        int sayi = 13;
        Fakt_Test(-5, Faktoriyel(-5));
        Fakt_Test(0, Faktoriyel(0));
        Fakt_Test(5, Faktoriyel(5));
        Fakt_Test(5, Faktoriyel(6));
        Fakt_Test(15, Faktoriyel(15));
        return 0;
}

