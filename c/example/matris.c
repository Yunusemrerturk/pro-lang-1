#include <stdio.h>

int * Matris(int satir, int sutun){
	int * mtr;
	mtr = (int *) calloc(satir*sutun+2, sizeof(int));
	mtr[0] = satir;
	mtr[1] = sutun;
	return mtr;
}

void Ekle(int *Matris, int sat, int sut, int deger){
	sat--; sut--;
	Matris[2+sat*Matris[1] +sut]=deger;
}

void Sifirla(int *Matris, int sat, int sut){
	sat--; sut--;
	Matris[2+sat*Matris[1] +sut]=0;
}

int Eleman(int *Matris, int sat, int sut){
	sat--; sut--;
	return Matris[2+sat*Matris[1] +sut];
}

void Yazdir(int *Matris){
	int sat = Matris[0];
	int sut = Matris[1];
	int i, j;
	printf("\nMatris : \n\n");
	for (i=0; i<sat; i++){
		for (j=0; j<sut; j++)
			printf("%3d", Matris[2+i*sut+j]);
		printf("\n");
	}
}

int main(void){
	int * MyMatrix;
	MyMatrix = Matris(3,5);
	Ekle(MyMatrix, 3, 5, 18);
	Ekle(MyMatrix, 2, 2, -7);
	Ekle(MyMatrix, 3, 3, 13);
	Yazdir(MyMatrix);
	Sifirla(MyMatrix, 2, 2);
	Yazdir(MyMatrix);
	printf("\n3. satir 3. sutundaki eleman : %d\n", Eleman(MyMatrix, 3, 3));
	return 0;
}

