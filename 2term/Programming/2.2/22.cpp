#include <math.h>
#include <stdio.h>
#include <conio.h>
#include <Windows.h>
#include "omp.h"

const int NLIM=10000;

double Recurs(int I,int N,double X,double Arg);
double Cycle(int I,double X);
int EWithCycle(double X, double E);
int EWithRecurs(int I,double E,double X,double Arg,double Summ);
void Output(void); 
bool Lim(double X,double E);

void main(void)
{	
	Output();
}

double Cycle(int N,double X)
{
	int I=3;
	double Summ=X,Arg=X;

	for (I;I<=N;I=I+2){
		Arg=Arg*(-1)*pow(X,2.0)/((I-1)*I);
		Summ=Summ+Arg;
	}
	return Summ;
}

double Recurs(int I,int N,double X,double Arg)
{
	if (N>1){
		Arg=Arg*(-1)*pow(X,2.0)/(((I-N)-1)*(I-N));
		return Arg+Recurs(I,N=N-2,X,Arg);		
	}
	return X;
}

int EWithCycle(double X, double E)
{
	int I=1;
	double Arg=X,Summ=X;

	while (abs(sin(X)-Summ)>=E){
		I=I+2;
		Arg=Arg*(-1)*pow(X,2.0)/((I-1)*I);
		Summ=Summ+Arg;
	}
	return I;
}

int EWithRecurs(int I,double E,double X,double Arg,double Summ)
{
	if (abs(sin(X)-Summ)>=E){
		Arg=Arg*(-1)*pow(X,2.0)/((I-1)*I);
		return	EWithRecurs(I+2,E,X,Arg,Summ+Arg);		
	
	}
	return I-2;
}

bool Lim(double X,double E){
	int I=3;
	double Arg=X,I1=0,I2=0;

	I2=I*(I-1)/(I-2);
	for (I;I<NLIM;I=I+2){
	I1=I2;
	I2=I2*(I+1)*(I+2)/((I-1)*I);
	if (abs(I2-I1)<E) 
		break;
	}
	if (I<NLIM){ 
		if (abs(X)<I2)
			return true;
		else
		return false;
	}
	else return true;
}

void Output(void)
{
	int N,NIter;
	double X,Answ,E,StartTime, EndTime,Timer;
	char Choice;

	printf("Enter X and N\n");
	scanf("%lf %d",&X,&N);
	StartTime=omp_get_wtime();
	Answ=Cycle(N,X);
	EndTime=omp_get_wtime();
	printf("Calculations whith function sin\n%lf\n",sin(X));
	printf("Calculations whith cycle\n%lf\n",Answ);
	Timer=EndTime-StartTime;
	printf("%lf second passed\n",Timer);
	if ((N-N/2)>0){
		N=N-1;
	}
	StartTime=omp_get_wtime();
	Answ=Recurs(N+3,N,X,X);
	EndTime=omp_get_wtime();
	printf("Calculations whith recursion\n%lf\n",Answ);
	Timer=EndTime-StartTime;
	printf("%lf second passed\n",Timer);
	printf("Press any key to continue\n");
	getch();
	system("cls");
	printf("Enter pogreshnost'\n");
	scanf("%lf",&E);	
	NIter=EWithCycle(X,E);	
	printf("You need %d iterations(cycle)\n",NIter);
	NIter=EWithRecurs(3,E,X,X,X);
	printf("You need %d iterations(recursion)\n",NIter);
	printf("Press any key to continue\n");
	getch();
	system("cls");
	printf("Enter epsilon\n");
	scanf("%lf",&E);
	if (Lim(X,E))
		printf("Converges\n");
	else 
		printf("Doesn't converge\n");
	printf("Want change X?(y/n)\n");
	Choice=getch();
	while (Choice=='y'){
		system("cls");
		printf("Enter X\n");
		scanf("%lf",&X);
		if (Lim(X,E))
			printf("Converges\n");
		else 
			printf("Doesn't converge\n");
		printf("Want change X?(y/n)\n");
		Choice=getch();
	}
}