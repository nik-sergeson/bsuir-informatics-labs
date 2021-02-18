#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include <Windows.h>
#include <string.h>
#include <ctime>
#include <dos.h>
#include <string.h>

typedef struct item{
	char Name[10];
	long ID;
	long Cost;
	int Available;
	char About[80];
	int license;
	char Country[10];	
}item;

typedef struct Person{
	char Name[20];
	long MobPhone,HomePhone;
	char Passport[16];
}Person;

typedef struct ItemSp{
	char FName[20];
	item *info;
	struct ItemSp *next, *prev;
}ItemSp;

void Add(ItemSp **Head,ItemSp **Tail,item **Elem,const char *path);
void Del(ItemSp **Head, ItemSp **Tail);
void AdvView(ItemSp *Head,ItemSp **BinHe, ItemSp **BinTa);
void PrintIt(item *Elem);
void Ads(void);
void BaseFromFile(ItemSp **Head,ItemSp **Tail,const char *path);
void BaseToFile(ItemSp **Head,ItemSp **Tail,FILE *fp,const char *path);
void AddNew(ItemSp **Head,ItemSp **Tail, item **Elem,int Count);
void AddToHist(char Passport,ItemSp *Head);
void Cost(int *cSum, int GoodCost);
void AddBuyer(Person *person);
bool FileExcist(const char *path);
void EnterElem(item **Elem);
void AdvancedMenu(void);
void WorkWithSpis(ItemSp **Head,ItemSp **Tail, const char *path);
void WorkWithBin(ItemSp **Head,ItemSp **Tail);
void AdmView(ItemSp *SpHe,const char path);

int main(void){
	int choice=0,i;
	char sCh[2];
	item *Head=NULL,*Tail=NULL;
	FILE *fp;

	srand(time(NULL));
	//Ads();
	for (i=1;i<=5;i++);
		//Add(&Head,&Tail,i);
	//AdvView(Head);
	while (choice!=4){
		system("cls");
		printf("1)Computers\n2)Accessories\n3)Repair parts\n4)Acoustic\n5)Monitors\n6)Memory\n7)Advansed");
		scanf("%s",sCh);
		switch(atoi(sCh)){
		case 1:
			printf("");
			break;
		case 2:
			printf("");
			break;
		case 3:
			printf("");
			break;
		case 4:
			printf("");
			break;
		case 5:
			printf("");
			break;
		case 6:
			printf("");
			break;
	}
}
}

void Add(ItemSp **Head,ItemSp **Tail,item **Elem,const char *path){
	ItemSp *InsElem;

	InsElem=(ItemSp *)malloc(sizeof(ItemSp));
	InsElem->info=*Elem;
	memcpy(InsElem->FName,path, sizeof(InsElem->FName));
	InsElem->next=NULL;
	if (*Head==NULL){
		InsElem->prev=NULL;
		*Head=InsElem;
		*Tail=InsElem;
	}
	else{
		(*Tail)->next=InsElem;
		InsElem->prev=*Tail;
		*Tail=InsElem;
	}
}

void Del(ItemSp **Head, ItemSp **Tail){
	ItemSp *DelElem;

	DelElem=*Tail;
	*Tail=(*Tail)->prev;
	(*Tail)->next=NULL;
	free(DelElem);
}

void AdvView(ItemSp *SpHe,ItemSp **BinHe, ItemSp **BinTa){
	ItemSp *Temp;
	item *BuyProd;
	int i;
	char Count[10];

	Temp=SpHe;
	PrintIt((Temp->info));
	while((i=getch())!=27){
		switch(i){
		case 224:
			i=getch();
			switch(i){
				case 75:
					system("cls");
					if (Temp->prev!=NULL)
						Temp=Temp->prev;
					PrintIt((Temp->info));
					break;
				case 77:
					system("cls");
					if (Temp->next!=NULL)
						Temp=Temp->next;
					PrintIt((Temp->info));
					break;
			}
		case 13:
			printf("Enter quantity of product\n");
			scanf("%s",&Count);
			if((atoi(Count))>Temp->info->Available)
				printf("There aren't so much product in store");
			else{
				BuyProd=(item *)malloc(sizeof(item));
				memcpy(BuyProd, Temp->info, sizeof(item));
				AddNew(BinHe,BinTa,&BuyProd,atoi(Count));
				Temp->info->Available-=atoi(Count);
			}
		}
	}
}

void PrintIt(item *Elem){

	printf("About %s\n",Elem->About);
	printf("Cost %d",Elem->Cost);
}

void Ads(void){
	int i;

	printf("\t\t\tIt's easy to buy with cShop!\n");
	for(i=0; i<=79;i++)
		putchar((char)205);
	printf("1)Find PC, that suits you\n2)Fast and easy serch\n3)Simple interface\n4)Lots of goods in catalogue\n5)No problems with details for your PC\n6)Full information in bases\n7)Lots of functions\n\n\n");
	printf("\t\t\t\t\t\t\t Author:Student\n");
	for(i=0; i<=79;i++)
		putchar((char)205);
	printf("Wait while loading");
	for(i=0; i<=5;i++){
		Sleep(800);
		putchar('.');
	}
}

void BaseFromFile(ItemSp **Head,ItemSp **Tail,FILE *fp,const char *path){
	int RecNum=0;
	item *Temp=NULL;

	fp=fopen(path,"rb");
	while(!feof(fp)){
		Temp=(item *)malloc(sizeof(item));
		fread(Temp,sizeof(item),1,fp);
		Add(Head,Tail,&Temp);
	}
	fclose(fp);
}

void BaseToFile(ItemSp **Head,ItemSp **Tail,const char *path){
	ItemSp *Temp;
	FILE *fp;

	fp=fopen(path,"wb");
	Temp=*Head;
	while (Temp!=NULL){
		fwrite(Temp->info,sizeof(item),1,fp);
		Temp=Temp->next;
	}
	fclose(fp);
}

void AddNew(ItemSp **Head,ItemSp **Tail, item **Elem,int Count){
	ItemSp *Temp;
	long ID;

	Temp=*Head;
	ID=(long)(*Elem)->ID;
	while((ID!=(Temp->info->ID))&&(Temp!=NULL))
		Temp=Temp->next;
	if (Temp!=NULL){
		Temp->info->Available+=Count;
		free(*Elem);
	}
	else {
		(*Elem)->Available=Count;
		Add(Head,Tail,Elem);
	}
}

void AddToHist(char Passport,ItemSp *Head){
	FILE *fp,*fp1;
	ItemSp *Temp;
	time_t timer;
	struct tm *tblock;

	timer = time(NULL);
	tblock = localtime(&timer);
	fp=fopen("LOGTOVAROV","wb");//проверить на существование
	fp1=fopen("SPISCHEL","wb");//заменить указатель на файл
	Temp=Head;
	while (Temp!=NULL){
		fwrite(tblock,sizeof(tblock),1,fp);
		fwrite(tblock,sizeof(tblock),1,fp1);
		fwrite(Temp->info,sizeof(item),1,fp);
		fwrite(Temp->info,sizeof(item),1,fp1);
		Temp=Temp->next;
	}
	fclose(fp);
	fclose(fp1);
}

void Cost(int *cSum, int GoodCost){

	*cSum+=GoodCost;
}

void AddBuyer(Person *person){
	FILE *fp;
	int Size;

	fp=fopen("BUYERS","r+b");
	fseek(fp,0,SEEK_END);
	fwrite(person,sizeof(Person),1,fp);
	fclose(fp);
}

bool FileExcist(const char *path){
	FILE *fp;

	fp=fopen(path,"r");
	if (!fp)
		return false;
	else{
		fclose(fp);
		return true;
	}
}

void EnterElem(item **Elem){
	char str[80],ch;

	*Elem=(item *)malloc(sizeof(item));
	printf("Enter information about product\n");
	scanf("%s",&str);
	if (strlen(str)==0){
		free(*Elem);
		*Elem=NULL;
		return;
	}
	strcpy((*Elem)->About,str);
	while(1){
		printf("Is product available? y/n");
		ch=getch();
		if (ch=='y'){
			(*Elem)->Available=true;
			break;
		}
		if (ch=='n'){
			(*Elem)->Available=false;
			break;
		}
	}
	printf("Enter elem cost\n");
	scanf("%s",&str);
	(*Elem)->Cost=atoi(str);
	printf("Eter country");
	scanf("%s",&str);
	strcpy((*Elem)->Country,str);
	printf("Enter ID of product");
	scanf("%s",&str);
	(*Elem)->ID=atoi(str);
	printf("Enter length of license");
	scanf("%s",&str);
	(*Elem)->license=atoi(str);
	printf("Enter product name");
	scanf("%s",&str);
	strcpy((*Elem)->Name,str);
}

void AdvancedMenu(void){
	char choice[10]="\0";
	
	while((atoi(choice))!=3){
		system("cls");
		printf("1)Add element\n2)Delete elemens\n");
	}
}

void WorkWithSpis(ItemSp **Head,ItemSp **Tail, const char *path){
	ItemSp *SpHe=NULL,*SpTa=NULL;

	BaseFromFile(&SpHe,&SpTa, path);
	AdvView(SpHe,Head,Tail);
	BaseToFile(Head,Tail,path);
}

void WorkWithBin(ItemSp **Head,ItemSp **Tail){
	int Count=0, SummMon=0;
	ItemSp *Elem,*SpHe=NULL,*SpTa=NULL;;
	char ch;
	Person *Man;

	Elem=*Head;
	while(Elem){
		Count+=Elem->info->Available;
		SummMon+=Elem->info->Available*Elem->info->Cost;
		Elem=Elem->next;
	}
	printf("You have %d goods and need to purchase %d dollars, confirm?(y/n)\n",Count,SummMon);
	ch=getch();
	switch(ch){
		case 'y':
			Man=(Person *)malloc(sizeof(Person));
			printf("Enter your name\n");
			scanf("%s",&Man->Name);
			printf("Enter your mobile phone\n");
			scanf("%ld",&Man->MobPhone);
			printf("Enter your home phone\n");
			scanf("%ld",&Man->HomePhone);
			printf("Enter passport ID\n");
			scanf("%s",&Man->Passport);
			AddBuyer(Man);
			free(Man);
			break;
		case 'n':
			Elem=*Head;
			while(Elem){
				BaseFromFile(&SpHe,&SpTa, Elem->FName);
				AddNew(&SpHe,&SpTa,&Elem->info,Elem->info->Available);
				BaseToFile(&SpHe,&SpTa, Elem->FName);
				Elem=Elem->next;
			}
	}
}

void AdmView(ItemSp *SpHe,const char path){
	ItemSp *Temp,*InsElem;
	int i;
	char Count[10];

	Temp=SpHe;
	PrintIt((Temp->info));
	while((i=getch())!=27){
		switch(i){
		case 224:
			i=getch();
			switch(i){
				case 75:
					system("cls");
					if (Temp->prev!=NULL)
						Temp=Temp->prev;
					PrintIt((Temp->info));
					break;
				case 77:
					system("cls");
					if (Temp->next!=NULL)
						Temp=Temp->next;
					PrintIt((Temp->info));
					break;
			}
		case 13:
			EnterElem(&InsElem->info);
			InsElem->prev=Temp;
			if (Temp->next)
				InsElem->next=Temp->next;
			else
				InsElem->next=NULL;
			Temp->next=InsElem;
			if(InsElem->next->prev)
				InsElem->next->prev=InsElem;			
		}
	}
}