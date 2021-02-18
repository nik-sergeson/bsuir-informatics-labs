#include <stdio.h>
#include <malloc.h>
#include <Windows.h>

#define LONG_STR 128
#define LETT 64
#define BIGLETT 90
#define BIGLIT 32

char** Input(int *Textlen);
void Output(char* str);
void Wipe(char **Text,int Textsize);

int main(void){
	char **Arr;
	int Textsize=0,i;

	Arr=Input(&Textsize);
	printf("Right words:\n");
	for(i=0;i<Textsize;i++)
		Output(Arr[i]);
	Wipe(Arr,Textsize);
	system("pause");	
	return 0;
}

char** Input(int *Textlen){
	long i = 0, sLen = 0;
	int TextSize=0;
	char ch,* str,**Text=NULL;

	printf("Enter string :\n");
	while(1){
		Text=(char **)realloc(Text,(++TextSize)*sizeof(char *));
		i = 0;
		sLen = 0;
		Text[TextSize-1] = (char *)malloc(LONG_STR*sizeof(char));
		while((ch = getchar()) != '\n')
		{
			Text[TextSize-1][sLen + i] = ch;
			if(i < LONG_STR)
				i++;
			else
			{
				Text[TextSize-1] = (char *)realloc(Text[TextSize-1],(LONG_STR + (sLen += LONG_STR))*sizeof(char));
				i = 0;
			}
		}
		if(i < LONG_STR)
			sLen += i;
		if (sLen==0){
			free(Text[TextSize-1]);
			*Textlen=TextSize-1;
			break;
		}
		else
			Text[TextSize-1][sLen] = '\0';
	}
    return Text;
}

void Output(char* str){
	int Nelem=0,BWord=0,ch1=0,ch2=0;
	bool Bl=true;
	   	
	while (str[Nelem]!='\0'){
		while ((str[Nelem]!=' ')&&(str[Nelem]!='\0')){
		if ((int)str[Nelem]<LETT){
			break;
		}
		ch1=(int)str[Nelem-1];
		if (ch1>BIGLETT)
			ch1-=BIGLIT;
		ch2=(int)str[Nelem];
		if (ch2>BIGLETT)
			ch2-=BIGLIT;
		if (ch2<ch1)
			Bl=false;
		++Nelem;
		}
		if ((Bl)&&((int)str[Nelem-1]>LETT)&&(Nelem-BWord>1)){
			for (BWord;BWord<Nelem;BWord++)
				printf("%c",str[BWord]);
			printf("\n");
		}
		Bl=true;
		++Nelem;
		BWord=Nelem;
		}
}

void Wipe(char **Text,int Textsize){
	int i;

	for(i=0;i<Textsize;i++)
		free(Text[i]);
	free(Text);
}