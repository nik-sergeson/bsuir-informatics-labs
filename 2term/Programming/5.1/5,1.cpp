#include <malloc.h>
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>
#include <string.h>
#include <Windows.h>

const int SLength=17;

typedef struct item{
	struct item *next;
	int IncTime;
}Item;

Item ** Add(Item **HeIl,int Time);
Item ** Delete(Item **HeIl);
int LengthSp(Item *Head);
int MinTime(Item ***Serv,int *ServTime,int n,int* Summ,int **ElemInd,int *Count);
void Calculat(int Time,Item ***Serv,int *ServTime,int n);
void Initial(int n,int Time,int *ServTime);
void PrintSp(Item *Head);
void WievAll(Item ***Serv,int *ServTime,int n);
int Count(double Val);
bool IsServ(int *ar, int Count,int Val);

int main(void){
	int n=0,Time,i,*ServTime=NULL;;
	char str1[SLength],str2[SLength];

	while(1){
		system("cls");
		printf("Enter number of services\n");
		scanf("%s",str1);
		n=atoi(str1);
		printf("Enter time\n");
		scanf("%s",str2);
		Time=atoi(str2);
		if ((n==0) || (Time==0) ||(Count(n)!=strlen(str1))||(Count(Time)!=strlen(str2))){
			printf("Wrong value");
			getch();
			continue;
		}
		else{
			ServTime=(int *)malloc(n*sizeof(int));
			for(i=0;i<n;i++){
				while(1){
				printf("Enter time of %d service\n",i+1);
				scanf("%s",str1);
				ServTime[i]=atoi(str1);
				if((ServTime[i]==0)||(Count(ServTime[i])!=strlen(str1))){
					printf("Wrong value");
					getch();
					continue;
				}
				else 
					break;
				}
			}
			Initial(n,Time,ServTime);
			break;
		}
	}
	getch();
	return 0;
}

void Initial(int n,int Time,int *ServTime){
	Item ***Serv=NULL;
	int Nelem,j,i;
	
	srand(time(NULL));	
	Serv=(Item ***)malloc(n*sizeof(Item **));
	for(i=0;i<n;i++){
		Serv[i]=(Item **)malloc(2*sizeof(Item*));
		Serv[i][0]=NULL;
		Serv[i][1]=NULL;
	}
	for(i=0;i<n;i++){
		Nelem=rand()%10+1;
		for(j=0;j<Nelem;j++)
			Serv[i]=Add(Serv[i],0);
	}
	WievAll(Serv,ServTime,n);	
	Calculat(Time,Serv,ServTime,n);
}

Item ** Add(Item **HeIl, int Time){
	Item *Head=NULL,*Tail=NULL,*Car;

	Head=HeIl[0];
	Tail=HeIl[1];
	Car=(Item *)malloc(sizeof(Item));
	Car->next=NULL;
	Car->IncTime=Time;
	if (Head==NULL){
		Head=Car;
		Tail=Car;
	}
	else{
		Tail->next=Car;
		Tail=Car;
	}
	HeIl[0]=Head;
	HeIl[1]=Tail;
	return(HeIl);
}

Item ** Delete(Item **HeIl){
	Item *Head=NULL,*Tail=NULL,*Car;

	Head=HeIl[0];
	Tail=HeIl[1];
	Car=Head;
	if (Head!=NULL){
	Head=Head->next;
	if (Head==NULL)
		Tail=NULL;
	free(Car);
	}
	HeIl[0]=Head;
	HeIl[1]=Tail;
	return(HeIl);
}

int LengthSp(Item *Head){
	int i=0;
	Item *p=Head;

	while (p!=NULL){
		p=p->next;
		++i;
	}
	return i;
}

int MinTime(Item ***Serv,int *ServTime,int n,int* Summ,int **ElemInd,int *Count){
	int MinInd=-1,i=0,MinT=0,Tmp;
	bool Excist=false;

	for(i=0;i<n;i++){
		Excist=IsServ(*ElemInd,*Count,i);
		if(Excist==false){
			MinT=ServTime[i]*(1+LengthSp(Serv[i][0]));
			break;
		}
	}
	for(i=0;i<n;i++){
		Tmp=ServTime[i]*(1+LengthSp(Serv[i][0]));
		Excist=IsServ(*ElemInd,*Count,i);
		if ((Tmp<=MinT)&&(Excist==false)){
			MinT=Tmp;
			MinInd=i;
			}
	}
	*Summ=MinT;
	return MinInd;
}

void Calculat(int Time,Item ***Serv,int *ServTime,int n){
	int i,SumTm=0,MInd=0,Csum=0,SummEnterM=rand()%10+1,EntInd,*LastLeft=NULL;
	Item **Route=NULL;
	int *ElemInd=NULL,Count=-1;

	Route=(Item **)malloc(2*sizeof(Item *));
	ElemInd=(int*)malloc(n*sizeof(int));
	Route[0]=NULL;
	Route[1]=NULL;
	LastLeft=(int *)malloc(n*sizeof(int));
	for (i=0;i<n;i++)
		LastLeft[i]=0;
	while (1){
		MInd=MinTime(Serv,ServTime,n,&Csum,&ElemInd,&Count);
		if(MInd==-1)
			break;
		++Count;
		ElemInd[Count]=MInd;
		if ((SumTm+Csum)>Time)			
			break;
		else{
			Serv[MInd]=Add(Serv[MInd],SumTm);
			SumTm+=Csum;
			while(SummEnterM<=SumTm){
				EntInd=rand()%n;
				if(SummEnterM)
					Serv[EntInd]=Add(Serv[EntInd],SummEnterM);
				SummEnterM+=rand()%10+1;
			}			
			for (i=0;i<n;i++)
				while(1){
					if (Serv[i][0]==NULL)
						break;
					if ((Serv[i][0]->IncTime-LastLeft[i])>0)
						if ((Serv[i][0]->IncTime+ServTime[i])<=SumTm){
							LastLeft[i]=Serv[i][0]->IncTime+ServTime[i];
							Serv[i]=Delete(Serv[i]);
						}
						else 
							break;
					else
						if (LastLeft[i]+ServTime[i]<=SumTm){
							LastLeft[i]+=ServTime[i];
							Serv[i]=Delete(Serv[i]);
						}
						else
							break;
			}
			printf("Choice:%d\n",MInd+1);
			printf("Time:%d\n",SumTm);
			WievAll(Serv,ServTime,n);
			Route=Add(Route,MInd+1);
			}
	}
	printf("Route:\nBegin->");
	PrintSp(Route[0]);
	printf("->Exit");
}

void PrintSp(Item *Head){
	Item *p=NULL;
	int i=0;

	p=Head;
		while (p!=NULL){
			printf("(%d)%d ",++i,p->IncTime);
			p=p->next;
		}
	}

int Count(double Val){
	int i=0;

	if ((Val-(int)Val)!=0)
		++i;
	else 
		while((int)Val%10==0){
			Val=(int)(Val/10);
			++i;
		}
	while ((int)Val!=0)
		Val/=10;
	while ((Val-(int)Val)!=0){
		Val*=10;
		++i;
	}
	return i;
}

void WievAll(Item ***Serv,int *ServTime,int n){
	int i;

	printf("Queue:\n");
	for(i=0;i<n;i++){
		PrintSp(Serv[i][0]);
		printf("---%d min\n",ServTime[i]);
	}
}

bool IsServ(int *ar, int Count,int Val){
	int i=0;
	bool Isin=false;

	for(i=0;i<=Count+1;i++){
		if(ar[i]==Val){
			Isin=true;
		}
	}
	return Isin;
}