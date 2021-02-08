#include <malloc.h>
#include <stdio.h>
#include <conio.h>
#include <Windows.h>
#include <string.h>
#include <stdlib.h>

const int SLength=17;

void Menu(void);
double * AddElem(double Val,double* Mas,int *Smas);
double CurrVal(int Index,double* Mas);
double * EditMas(int ElemIndex,double Val,double* Mas);
double * MasMenu(double* Mas,int *Smas);
void Calculations(double *VoiceTime,double *MoveSp,double *MoveTime,int SVoiceTime,double VVelos);
int Count(double Val);

void main(void){
	
	Menu();
}

void Menu(void){
	int Choice=0,SVoiceTime=0,SMoveSp=0,SMoveTime=0;
	double *VoiceTime=NULL,*MoveSp=NULL,*MoveTime=NULL,VVelos;
	char str1[SLength];
	
	while (Choice!=5){
		system("cls");
		printf("1)Vrem'a golosovani'a pered i'm ychastkom\n2)Skorost na i'm ychastke\n3)Vrem'a dvizheni'a na i'm ychastke\n4)Calculate\n5)Exit\n");
		Choice=getch();
		switch (Choice){
			case '1':
				VoiceTime=MasMenu(VoiceTime,&SVoiceTime);
				break;
			case '2':
				MoveSp=MasMenu(MoveSp,&SMoveSp);			
				break;
			case '3':
				MoveTime=MasMenu(MoveTime,&SMoveTime);		
				break;
			case '4':
				system("cls");
				printf("Enter speed of bycecle\n");
				scanf("%s",&str1);
				if (((VVelos=atof(str1))==0)||(Count(VVelos)<strlen(str1)))
					printf("Wrong value");
				else
					Calculations(VoiceTime,MoveSp,MoveTime,SVoiceTime,VVelos);
				getch();
				break;
			case '5':
				Choice=5;
				free(VoiceTime);
				free(MoveSp);
				free(MoveTime);
				break;
		}
	}
}

double * MasMenu(double* Mas,int *Smas){
	int Choice=0,ElemIndex;
	double Val;
	char str1[SLength],str2[SLength];
		
	while (Choice!=4){
		system("cls");
		printf("1)Add Element\n2)Edit element\n3)Value(index)\n4)Back\n");
		Choice=getch();
		switch (Choice){
			case '1':
				system("cls");
				printf("Enter value\n");
				scanf("%s",str1);
				if (((Val=atof(str1))==0)||(Count(Val)<strlen(str1)))
					printf("Wrong value");
				else{
					Mas=AddElem(Val,Mas,Smas);
					printf("Element entered,press any button to continue\n");
				}
				getch();
				break;
			case '2':
				system("cls");
				printf("Enter value and index \n");
				scanf("%s",str1);
				Val=atof(str1);
				scanf("%s",str2);
				ElemIndex=atoi(str2);
				if ((Val==0) || (ElemIndex==0) ||(Count(ElemIndex)<strlen(str2))||(Count(Val)<strlen(str1))|| (ElemIndex>*Smas)){
					printf("Wrong value");
				}
				else{
				Mas=EditMas(ElemIndex,Val,Mas);
				printf("Element edited,press any button to continue\n");
				}
				getch();
				break;
			case '3':
				system("cls");
				printf("Enter index\n");
				scanf("%s",str2);
				if (((ElemIndex=atoi(str2))==0)||(Count(ElemIndex)<strlen(str2))||(ElemIndex>*Smas))
					printf("Wrong value");
				else{
				printf("Value=%.2lf\n",CurrVal(ElemIndex,Mas));
				printf("Press any button to continue\n");
				}
				getch();
				break;
			case '4':
				Choice=4;
			break;
		}
	}
	return Mas;
}

double * EditMas(int ElemIndex,double Val,double* Mas){
	
	Mas[ElemIndex-1]=Val;
	return Mas;
}

double * AddElem(double Val,double* Mas,int *Smas){
	double* CMas=NULL;
	int i;

	if (*Smas==0){
		Mas = (double *) malloc( sizeof(double));
		*Smas=1;
		Mas[0]=Val;
		return Mas;
	}
	else{
		++*Smas;
		CMas=(double *) malloc((*Smas)*sizeof(double));
		for(i=0;i<*Smas-1;++i){
			CMas[i]=Mas[i];
		}
		free(Mas);
		CMas[*Smas-1]=Val;
		return CMas;	
	}	
}

double CurrVal(int Index,double* Mas){
	
	return Mas[Index-1];
}

void Calculations(double *VoiceTime,double *MoveSp,double *MoveTime,int SVoiceTime,double VVelos){
	int i=0;
	double SVelos=0,SStop=0,ds=0,Nds=0,Tmeet=0,CTime=0,SMeet=0;
	bool VLead=true;

	for(i;i<=SVoiceTime-1;++i){
		ds=(SStop-SVelos);
		Nds=ds-(VoiceTime[i]/60)*VVelos;
		if ((ds*Nds)<0){
			Tmeet=ds/VVelos;
			SMeet=SStop;
			Tmeet=CTime+Tmeet;
			printf("Time=%3.1lf\n",Tmeet);
			printf("Length=%3.1lf\n",SMeet);
		}
		ds=Nds;
		SVelos=SVelos+(VoiceTime[i]/60)*VVelos;
		CTime=CTime+VoiceTime[i]/60;
		Nds=(SStop+MoveSp[i]*MoveTime[i]-(SVelos+VVelos*MoveTime[i]));
		if ((ds*Nds)<0){
			Tmeet=ds/(VVelos-MoveSp[i]);
			SMeet=SVelos+Tmeet*VVelos;
			Tmeet=CTime+Tmeet;
			printf("Time=%3.1lf\n",Tmeet);
			printf("Length=%3.1lf\n",SMeet);
		}
		SVelos=SVelos+VVelos*MoveTime[i];
		SStop=SStop+MoveTime[i]*MoveSp[i];
		CTime=CTime+MoveTime[i];
	}
	if (Tmeet==0)
		printf("Won't meet\n");
}

int Count(double Val){
	int i=0;

	if ((Val-(int)Val)!=0)
		++i;
	while ((int)Val!=0)
		Val/=10;
	while ((Val-(int)Val)!=0){
		Val*=10;
		++i;
	}
	return i;
}