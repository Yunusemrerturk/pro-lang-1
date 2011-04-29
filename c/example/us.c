#include <stdio.h>

int us(a,b){
        int i,k=1;
        while (b!=0){
                k*=a;
                b--;
        }
        return k;
}

int main(){
        printf("%d", us(3,4));
	return 0;
}

