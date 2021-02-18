#include <stdio.h>
#include <conio.h>
#include <malloc.h>
#include <Windows.h>
#include <time.h>

typedef struct item{
	int Val;
	struct item *next;
} Item;

typedef struct tree{
	int Val;
	struct tree *left;
	struct tree *right;
} Tree;

typedef struct stack{
	int Val;
	struct stack *next;
} Stack;

Item * AddEl(Item *Head,int Val);
void InitSp(Item **Head);
int SpToTree(Item *Head,Tree **Node);
void AddToTree(int Data,Tree **Node);
void Length(int i, int *Max, Tree *Node,Stack *Tmp,Item **MaxSp);
Stack * AddStack(Stack * Head, int Data);
Stack * DelStack(Stack *Head,int Size);
void WievSt(Stack *Head);
void WievCircle(Item *Head);
void StToSp(Stack **Tmp,Item **Max);
void AddToEnd(Item **Head,int Data);
void Delsp(Item **Head);
void AddToBeg(Item **Head,int Data);
void WievSp(Item *Head);
void Out(Tree *root, unsigned k);

int main(void){
	Item *Head=NULL,*p=NULL,*MaxHe=NULL;
	int Val,i,Len=0,NumEl;
	Tree *root=NULL;
	Stack *Temp=NULL;
	
	srand(time(NULL));
	InitSp(&Head);
	printf("List:\n");
	WievCircle(Head);
	printf("\n");
	NumEl=SpToTree(Head,&root);
	Length(0,&Len,root,Temp,&MaxHe);
	Out(root,0);
	printf("Longest branch:\n");
	WievSp(MaxHe);
	getch();
	return 0;
}

Item * AddEl(Item *Head,int Val){
	Item *Elem=NULL,*P;
	
	Elem=(Item *)malloc(sizeof(Item));
	Elem->Val=Val;
	if (Head==NULL){
		Head=Elem;
		Head->next=Head;
	}
	else{
		P=Head;
		while(P->next!=Head)
			P=P->next;
		Elem->next=Head;
		P->next=Elem;
	}
	return Head;
}

int SpToTree(Item *Head,Tree **Node){
	Item *p=Head;
	int i=0;

	do{
		++i;
		AddToTree(p->Val,Node);
		p=p->next;		
	}
	while(p!=Head);
	return i;
}

void WievCircle(Item *Head){
	Item *p=Head;

	do{
		printf("%d ",p->Val);
		p=p->next;
	}
	while(p!=Head);
}

void InitSp(Item **Head){
	int Nelem=0,i,Val;

	Nelem=rand()%18+3;
	for(i=1;i<=Nelem;i++){
		Val=rand()%20;
		*Head=AddEl(*Head,Val);
	}
}

void AddToTree(int Data,Tree **Node){

	if (*Node==NULL){
		(*Node)=(Tree *)malloc(sizeof(Tree));
		(*Node)->left=NULL;
		(*Node)->right=NULL;
		(*Node)->Val=Data;
	}
	else if(Data<(*Node)->Val)
		AddToTree(Data,&((*Node)->left));
	else
		AddToTree(Data,&((*Node)->right));
}

void Length(int i, int *Max, Tree *Node,Stack *Tmp,Item **MaxSp){

	Tmp=AddStack(Tmp,Node->Val);
	if (Node->left)
		Length(i+1,Max, Node->left,Tmp,MaxSp);
 	if (*Max<i){
		*Max=i;
		StToSp(&Tmp,MaxSp);
	}
	if  (Node->right)
		Length(i+1,Max, Node->right,Tmp,MaxSp);
}

Stack *AddStack(Stack * Head, int Data){
	Stack *Elem=NULL;

	Elem=(Stack *)malloc(sizeof(Stack));
	Elem->Val=Data;
	if(Head==NULL){
		Elem->next=NULL;
		Head=Elem;
	}
	else{
		Elem->next=Head;
		Head=Elem;
	}
	return Head;
}
Stack * DelStack(Stack *Head,int Size){
	Stack *Elem=NULL;
	int i;

	for (i=1;i<=Size;i++){
		Elem=Head;
		Head=Head->next;
		free(Elem);
	}
	return Head;
}

void WievSt(Stack *Head){
	Stack *Elem=Head;

	while(Elem){
		printf("%d\n",Elem->Val);
		Elem=Elem->next;
	}
}

void AddToEnd(Item **Head,int Data){
	Item *Elem=NULL,*p=*Head;

	Elem=(Item*)malloc(sizeof(Item));
	Elem->Val=Data;
	Elem->next=NULL;
	if ((*Head)==NULL){
		*Head=Elem;
	}
	else{
		while (p->next!=NULL)
			p=p->next;
		p->next=Elem;
	}
}

void Delsp(Item **Head){
	Item *Elem=NULL;

	Elem=*Head;
	if(*Head!=NULL)
		*Head=(*Head)->next;
	free(Elem);
}

void AddToBeg(Item **Head,int Data){
	Item *Elem=NULL;

	Elem=(Item*)malloc(sizeof(Item));
	Elem->Val=Data;
	if (*Head==NULL){
		Elem->next=NULL;
		*Head=Elem;
	}
	else{
		Elem->next=*Head;
		*Head=Elem;
	}
}

void StToSp(Stack **Tmp,Item **Max){
	Stack *ElTmp=*Tmp;
	Item *ElMax=*Max;

	if (*Max==NULL){
		while (ElTmp!=NULL){
			AddToBeg(&(*Max),ElTmp->Val);
			ElTmp=ElTmp->next;
		}
	}
	else{
		while (*Max!=NULL)
			Delsp(&(*Max));
		StToSp(Tmp,Max);
	}
}

void WievSp(Item *Head){
	Item *Elem=Head;

	while(Elem){
		printf("%d  ",Elem->Val);
		Elem=Elem->next;
	}
}

void Out(Tree *root, unsigned n)
{
   long i;
   if (root)
   {
      Out(root->right, n+5);
      for (i = 0; i < n; i++) 
         printf(" ");
      printf("%d\n", root->Val);
      Out(root->left, n+5);
   }
}