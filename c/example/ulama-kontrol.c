#include <stdio.h>
#include <string.h>

int SesliMi(char ch){
	char *sesli = "aeiouAEIOU";
	if ( strchr(sesli, (int)ch)!=NULL )
		return 1;
	return 0;
}

int SessizMi(char ch){
      	char *sessiz = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
	if ( strchr(sessiz, (int)ch)!=NULL )
		return 1;
	return 0;
}

int BoslukMu(char ch){
	if (ch==' ')
		return 1;
	return 0;
}

int UlamaVarMi(char * ch1){
        if ( SessizMi(ch1[0]) && BoslukMu(ch1[1]) && SesliMi(ch1[2]))
		return 1;
	return 0;
}

int UlamaSay(char * mtn){
    int i=0;
    int k=0;
    while( mtn[i+2] != '\0'){
        if(UlamaVarMi(&mtn[i])) k++;
        i++;
    }
    return k;
}

int main(void){
        char metin[] = "Kugu, ordekgiller ailesine ait, iri ve beyaz su kusu turlerinin ortak adidir.";
	printf("ulama sayısı: %d\n", UlamaSay(metin));
        return 0;
}


