#include <stdio.h>
#include <conio.h>
#include <math.h>
const MinInHour=60,HalfOfDay=12,DegInHour=30,DegInMinute=6, HorMinDeg=0.5;

int main(void){
	int hr=0,min=0;
	float deg=0;
	printf("enter minutes\n");
	scanf("%d",&min);
	while (min>=MinInHour*HalfOfDay)
		min=min-MinInHour*HalfOfDay;
	hr=min/MinInHour;
	min=min-hr*MinInHour;
	deg=abs(hr*DegInHour+min*HorMinDeg-min*DegInMinute);
	printf("%3.1lf degrees\n",deg);
	printf("%d hour %d minute\n",hr,min);
	getch();
	return 0;