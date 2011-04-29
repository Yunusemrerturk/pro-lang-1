#include <stdio.h>

int main(void){
        char kelime[]="kelek";
        int i, son, k=strlen(kelime);
        for (i=0; i<k/2; i++){
                if (kelime[i]==kelime[k-1-i])
                        son=1;
                else{
                        son=0;
                        break;
                }
        }
        if (son==1)
                printf("palindromdur");
        else
                printf("palindrom değildir");
}

