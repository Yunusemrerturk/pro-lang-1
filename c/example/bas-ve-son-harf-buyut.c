#include <stdio.h>
#include <string.h>

int main(void){
        char dizgi[] = "merhaba dunya";
        int k=1, i, toplam = strlen(dizgi);
        printf("dizginin ilk hali: %s\n", dizgi);
        for (i=0; i<toplam; i++){
                if (k==1){
                        dizgi[i] = dizgi[i]-32;
                        k=0;
                }
                if (dizgi[i]==' '){
                        dizgi[i-1] = dizgi[i-1]-32;
                        k=1;
                }
                if(i+1==toplam){
                        dizgi[i] = dizgi[i]-32;
                }
        }
        printf("dizginin son hali: %s\n", dizgi);
        return 0;
}
