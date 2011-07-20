#include <stdio.h>
#include <string.h>

/*Herhangi bir dizgi içerisinde ardarda ceng var mıdır? yok mudur? ayırt edebilen programı yazınız.
Girdi : cengkleng --> Çıktı : Evet
Girdi : cenkgleng --> Çıktı : Hayır
Durum makinasıyla yapın denilmis ama bu otomataya uyar mı? hic sanmam.*/

char main(void){
        char dizgi[20],c[10];
        printf("Dizgiyi girin : ");
        scanf("%s", dizgi);
        printf("Aranacak dizgiyi girin : ");
        scanf("%s", c);

        int i, j, ok=0;
        for(i=0;i<strlen(dizgi);i++){
                j=0;
                while(dizgi[i]==c[j]){
                        if(j<strlen(c)){
                                i++;
                                j++;
                        }
                        else{
                                ok=1;
                                break;
                        }
                }
        }
        if(ok==1) printf("Evet\n");
        else printf("Hayir\n");
}
