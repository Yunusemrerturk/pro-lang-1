#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void){
        char c,y;
        c=getchar();
        while(c!=EOF){
        yeni:
                if( c==' ' ){
                        putchar(c);
                        c=getchar();
                        if( isalpha(c) ) printf("%c", toupper(c));
                }
                else if( isalpha(c) ){
                        y=getchar();
                        if( y==' ' ) 
                        {
                                printf("%c ",toupper(c));
                                c=y;
                                goto yeni;
                        }
                        else printf("%c%c",c,y);
                }
                c=getchar();
        }
        printf("\n");
        return 0;
}


