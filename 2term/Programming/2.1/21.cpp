#include <stdio.h>
#include <conio.h>
#include <windows.h>
#include <math.h>

const int NCAR=15,VES1CAR=20,MAXLENGTH=4000,MINVES=50,TARIF=2;double INSUR=0.05;

double EVes(void);
double ELength(void);
void Count(double Ves, double Length,bool Adopt);
bool Analize(double Ves, double Length);
void Author(void);
void OrderDecision(bool Adopt);
void SysDialog(void);
void CountOutput(int Cars,double SInsur,double Summ);

int main()
{
	int choice=0;
	double Ves=0,Length=0;
	bool Adopt=false;
	
	while (choice!=6)
	{
		printf("Menu:\n 1)Enter ves\n 2)Enter length\n 3)Analize\n 4)Count\n 5)Author\n 6)Quit\n");
		choice=getch();
		switch (choice)
		{
			case '1':
				Ves=EVes();
				break;
			case '2':
				Length=ELength();
				break;
			case '3':
				Adopt=Analize(Ves,Length);
				break;
			case '4':
				Count(Ves,Length,Adopt);
				break;
			case '5':
				Author();
				break;
			case '6':
				choice=6;
				break;
			default:
				printf("Illegal");
		}
	}
	return 0;
}

double EVes(void)
{
	double Mass; 

	system("cls");
	printf("Enter ves\n");
	scanf("%lf",&Mass);
	printf("Ves entered,press any button to continue\n");
	getch();
	system("cls");
	return Mass;
}

double ELength(void)
{
	double Length;

	system("cls");
	printf("Enter length\n");
	scanf("%lf",&Length);
	printf("Length entered,press any button to continue\n");
	getch();
	system("cls");
	return Length;
}

bool Analize(double Ves,double Length)
{	
	bool bl;

	system("cls");
	if ((Ves<=MINVES) || (Ves>NCAR*VES1CAR) ||(Length>MAXLENGTH)){
		bl=false;
		OrderDecision(bl);
	}
	else{
		bl=true;
		OrderDecision(bl);
	}
	SysDialog();
	return bl;
}

void Count(double Ves,double Length,bool Adopt)
{
	double Summ,SInsur;
	int Cars;

	system("cls");
	if (Adopt){
		Cars=((int)Ves+1)/VES1CAR;
		if (Cars*VES1CAR-Ves<0)
			Cars++;
		SInsur=Length*TARIF*Cars*INSUR;
		Summ=Length*TARIF*Cars+SInsur;
		CountOutput(Cars,SInsur,Summ);
	}
	else 
		OrderDecision(Adopt);
	SysDialog();
}

void Author(void)
{
	system("cls");
	printf("Student, BSUIR\n");
	SysDialog();
}

void OrderDecision(bool Adopt)
{
	if (Adopt) 
		printf("Order adopted\n");
	else
		printf("Order wasn't adopted\n");
}

void SysDialog(void)
{
	printf("Press any button to continue\n");
	getch();
	system("cls");
}

void CountOutput(int Cars,double SInsur,double Summ)
{
	printf("We need %d cars, insurance will cost %.2lf$, summ, you need to pay is %.2lf$\n",Cars,SInsur,Summ); 
}