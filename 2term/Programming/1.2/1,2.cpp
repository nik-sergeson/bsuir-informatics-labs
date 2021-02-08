#include <stdio.h>
#include <conio.h>
#include <math.h>

int main(void){
	double m;
	int i=1, summ=0;
	printf("Enter m\n");
	scanf("%lf",&m);
	for (i;i<4;i++){
		m=(m-floor(m))*10;
		summ=summ+floor(m);
	}
	printf("Result=%d\n",summ);
	getch();
	return 0;
}