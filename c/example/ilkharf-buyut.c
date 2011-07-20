#include <stdio.h>

int main(void){
        int c, state=1;
        for( ; ; ){
                c=getchar();
                if( c==EOF ) break;
                switch (state){
                        case 1:
                                if( isalpha(c) ) putchar(toupper(c)); 
                                state=2;
                                break;
                        case 2:
                                if( isalpha(c) ) state=1;
                                putchar(c);
                                break;
                        default:
                                printf("Hata var!");
                }
                printf("\n");
                return 0;
        }
}
