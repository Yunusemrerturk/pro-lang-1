// yılın kaçıncı gününde olduğumuzu söyleyen program.
// Girdi   bugün (21.10.2010) girildiğinde
// Çıktı
//     * "bugün yılın 294. günüdür" diyecek
//     * haftayı da ver

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
        char tarih[11] = "21.11.2010 ";
        char yil[10] = "";
        char ay[10] = "";
        char gunler[10] = "";
        int aylar[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
        int i, gun=0;
        for(i = 6; i<strlen(tarih); i++)
                yil[i-6] = tarih[i];

        for(i = 3; i<6; i++)
                ay[i-3] = tarih[i];

        for(i = 0; i<2; i++)
                gunler[i] = tarih[i];

        gun += atoi(gunler);

        for (i=0; i<atoi(ay)-1; i++)
               gun += aylar[i];

        if (atoi(yil)%4==0)
                gun++;

        printf("Bugün yılın %d. gündündeyiz\nHaftalardan %d. haftadayız\n", gun, gun/7+1);
        return 0;
}

