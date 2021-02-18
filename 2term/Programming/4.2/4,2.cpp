#include <stdio.h>
#include <conio.h>
#include <malloc.h>

int *LengthMas(int *Nstr);
char **GetStr(int Nstr,int *Length);
void Print(char **Arr,int Nstr);
char** RMove(char **Arr,int *Length,int Nstr);
void PutStr(char **Arr,int Nstr);
void Wipe(char **Arr,int Nstr);

int main(void){
	int Nstr=0,*Length=NULL,i=0;
	char **Arr=NULL;

	Length=LengthMas(&Nstr);
	for(i=0;i<Nstr;i++)
		printf("%d\n",Length[i]);
	Arr=GetStr(Nstr,Length);
	printf("Old strings:\n");
	for(i=0;i<Nstr;i++)
		puts(Arr[i]);
	Print(Arr,Nstr);
	Arr=RMove(Arr,Length,Nstr);		
	printf("New strings:\n");
	Print(Arr,Nstr);
	PutStr(Arr,Nstr);
	Wipe(Arr,Nstr);
	getch();	
	return 0;
}

int *LengthMas(int *Nstr){
	FILE *fp;
	char c;
	int StrB=0,StrE=0,*Length=NULL;

	fp=fopen("text.txt","r");
	while((c=fgetc(fp))!=EOF){
		if (c=='\n'){
			*Nstr+=1;
			Length=(int *)realloc(Length,(*Nstr)*sizeof(int));
			Length[(*Nstr)-1]=StrE-StrB;
			StrE+=2;
			StrB=StrE;
			fseek(fp,StrB,SEEK_SET);
		}
		else
			StrE++;
	}
	if ((StrE-StrB)!=0){
		(*Nstr)+=1;
		Length=(int *)realloc(Length,(*Nstr)*sizeof(int));
		Length[(*Nstr)-1]=StrE-StrB;
	}
	fclose(fp);
	return Length;
}

char **GetStr(int Nstr,int *Length){
	FILE *fp;
	int i,CyrC=0;
	char **Arr;

	fp=fopen("text.txt","r");
	Arr=(char **)malloc(Nstr*sizeof(char*));
	for (i=0;i<Nstr;i++){		
		Arr[i]=(char *)malloc((Length[i]+1)*sizeof(char));
		fgets(Arr[i],Length[i]+1,fp);
		CyrC=CyrC+Length[i]+2;
		fseek(fp,CyrC,SEEK_SET);
	}
	fclose(fp);
	return Arr;
}

void Print(char **Arr,int Nstr){
	int i;

	for(i=0;i<Nstr;i++)
		puts(Arr[i]);
}

char** RMove(char **Arr,int *Length,int Nstr){
	int i,Niter,Nch;
	char TemCh;

	for (i=1;i<=Nstr;i++)
		for(Niter=1;Niter<=i;Niter++){
			TemCh=Arr[i-1][Length[i-1]-1];
			for (Nch=Length[i-1]-1;Nch>=1;Nch--)
				Arr[i-1][Nch]=Arr[i-1][Nch-1];
			Arr[i-1][0]=TemCh;
		}
	return Arr;
}

void PutStr(char **Arr,int Nstr){
	FILE *fp;
	int i;

	fp=fopen("text.txt","r+");
	for(i=0;i<Nstr;i++)
		fprintf(fp,"%s\n",Arr[i]);
	fclose(fp);
}

void Wipe(char **Arr,int Nstr){
	int i;

	for(i=0;i<Nstr;i++)
		free(Arr[i]);
	free(Arr);
}