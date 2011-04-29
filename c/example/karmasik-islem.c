#include <stdio.h>

// 2 + 3i karmaşık sayısının reel ve imajiner kısımlarını ekrana basan programı yazınız.
// çıktı
//     * Reel kısım: 2
//     * İmajiner kısım: 3

int main(void){
        char dizgi[]="2+3i", reel[10]="", imaj[10]="";
        int i, j, k;
        k=strlen(dizgi);
        for (i=0; i<k; i++){
                if (dizgi[i]=='+' || dizgi[i]=='-'){
                        break;
                }
                reel[i] = dizgi[i];
        }

        i++;
        for (j=i; j<k; j++){
                if (dizgi[j]=='i'){
                        break;
                }
                imaj[j-i] = dizgi[j];
        }
        printf("Reel kısım: %s\n", reel);
        printf("İmajiner kısım: %s\n", imaj);

        return 0;
}


