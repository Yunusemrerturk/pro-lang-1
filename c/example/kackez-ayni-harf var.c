#include <stdio.h>
#include <string.h>

// aabbbccccdddee dizgisinin içerisinde sadece 3 kez tekrarlananları ekrana basan programı yazınız.
// çıktı: bd

int main(void){
        char dizgi[100]="aabbbccccdddee", bos[100];
        int i, a, kac=0, k=strlen(dizgi);
        
        for (a=0; a<k ; a++){
                char ilk = dizgi[0];
                kac=0;
                k=strlen(dizgi)+1;
                char son[100]="";
                for (i=0; i<k ; i++){
                        if (dizgi[i]==ilk)
                                kac++;
                        else 
                                son[strlen(son)]=dizgi[i];
                }
                if (kac==3)
                        printf("3 karakterli bir grup harf %c\n", ilk);
                strcpy(dizgi,son);
                
        }
        return 0;
}

