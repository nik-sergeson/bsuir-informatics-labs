#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>

const int NMAX=10;

int LenCtr(int Ctr);
int ** Posit(void);
void PrinM(int **Arr);
void Vipe(int **Arr);

int main(){
	int **Arr;

	Arr=Posit();
	PrinM(Arr);
	Vipe(Arr);
	return 0;
}

int **Posit(void){
	static int i, j,**Arr,DimSh=4,NShip=1,n,CtrI,CtrJ,Summ=0;
	bool Set=false;

	Arr = (int **)malloc(NMAX * sizeof(int *));
	for (i = 0; i < NMAX; i++)
        Arr[i] = (int *)malloc(NMAX * sizeof(int));
	 for (i = 0; i < NMAX; i++)
        for (j = 0; j < NMAX; j++)
           Arr[i][j] = 0;
	 srand(time(NULL));
	 while (DimSh){
		  for (n=1;n<=NShip;n++){
			  Set=false;
			  while (!Set){
			  i=rand()%10;
			  j=rand()%10;
			  Summ=0;
			  for (CtrJ=j-LenCtr(j);CtrJ<=j+LenCtr((NMAX-1)-j);CtrJ++)
				for (CtrI=i-LenCtr(i);CtrI<=i+LenCtr((NMAX-1)-i);CtrI++)
					Summ=Summ+Arr[CtrJ][CtrI];
				if (Summ==0){
				  if (j>DimSh-2){
					  if (j==DimSh-1){
						  for (CtrJ=0;CtrJ<j;CtrJ++)
							for(CtrI=i-LenCtr(i);CtrI<=i+LenCtr((NMAX-1)-i);CtrI++)
								Summ=Summ+Arr[CtrJ][CtrI];
								if (Summ==0){
									for (CtrJ=0;CtrJ<=j;CtrJ++)
										Arr[CtrJ][i]=DimSh;
										Set=true;
								}
								else Summ=0;
					  }
					  else if (!Set){
						  for (CtrJ=j-(DimSh);CtrJ<j;CtrJ++)
							for(CtrI=i-LenCtr(i);CtrI<=i+LenCtr((NMAX-1)-i);CtrI++)
								Summ=Summ+Arr[CtrJ][CtrI];
								if (Summ==0){
									for (CtrJ=j-(DimSh-1);CtrJ<=j;CtrJ++)
										Arr[CtrJ][i]=DimSh;
										Set=true;
								}
								else Summ=0;
					  }
				  }
				  if (((NMAX-1)-i>=DimSh-1)&&(!Set)){
					  if ((NMAX-1)-i==DimSh-1){
						  for (CtrJ=j-LenCtr(j);CtrJ<=j+LenCtr((NMAX-1)-j);CtrJ++)
							for(CtrI=i+1;CtrI<=(NMAX-1);CtrI++)
								Summ=Summ+Arr[CtrJ][CtrI];
								if (Summ==0){
									for (CtrI=i;CtrI<=(NMAX-1);CtrI++)
										Arr[j][CtrI]=DimSh;
										Set=true;
								}
								else Summ=0;
					  }
					  else if (!Set){
						  for (CtrJ=j-LenCtr(j);CtrJ<=j+LenCtr((NMAX-1)-j);CtrJ++)
							for(CtrI=i+1;CtrI<=i+DimSh;CtrI++)
								Summ=Summ+Arr[CtrJ][CtrI];
								if (Summ==0){
									for (CtrI=i;CtrI<=i+DimSh-1;CtrI++)
										Arr[j][CtrI]=DimSh;
										Set=true;
								}
								else Summ=0;
					  }
				  }	
				  if (((NMAX-1)-j>=DimSh-1)&&(!Set)){
					  if ((NMAX-1)-j==DimSh-1){
						  for (CtrJ=j+1;CtrJ<=(NMAX-1);CtrJ++)
							for(CtrI=i-LenCtr(i);CtrI<=i+LenCtr((NMAX-1)-i);CtrI++)
								Summ=Summ+Arr[CtrJ][CtrI];
								if (Summ==0){
									for (CtrJ=j;CtrJ<=(NMAX-1);CtrJ++)
										Arr[CtrJ][i]=DimSh;
										Set=true;
								}
								else Summ=0;
					  }
					  else if (!Set){
						  for (CtrJ=j+1;CtrJ<=j+DimSh;CtrJ++)
							for(CtrI=i-LenCtr(i);CtrI<=i+LenCtr((NMAX-1)-i);CtrI++)
								Summ=Summ+Arr[CtrJ][CtrI];
								if (Summ==0){
									for (CtrJ=j;CtrJ<=j+(DimSh-1);CtrJ++)
										Arr[CtrJ][i]=DimSh;
										Set=true;
								}
								else Summ=0;
					  }
				  }	
				  if ((i>=DimSh-1)&&(!Set)){
					  if (i==DimSh-1){
						  for (CtrJ=j+LenCtr(j);CtrJ<=CtrJ-LenCtr((NMAX-1)-j);CtrJ++)
							for(CtrI=0;CtrI<=i-1;CtrI++)
								Summ=Summ+Arr[CtrJ][CtrI];
								if (Summ==0){
									for (CtrI=0;CtrI<=i;CtrI++)
										Arr[j][CtrI]=DimSh;
										Set=true;
								}
								else Summ=0;
					  }
					  else if (!Set){
						  for (CtrJ=j+LenCtr(j);CtrJ<=CtrJ-LenCtr((NMAX-1)-j);CtrJ++)
							for(CtrI=i-DimSh;CtrI<=i-1;CtrI++)
								Summ=Summ+Arr[CtrJ][CtrI];
								if (Summ==0){
									for (CtrI=i-(DimSh-1);CtrI<=i;CtrI++)
										Arr[j][CtrI]=DimSh;
										Set=true;
								}
								else Summ=0;
					  }
				  }	
			  }
			  }
			}
			NShip++;
			DimSh--;
		}
		return Arr;
}

void PrinM(int **Arr){
	int i,j;

	for (i = 0; i < NMAX; i++){
			for (j = 0; j < NMAX; j++)
				printf("%d ",Arr[i][j]);
			printf("\n");
		}
		getch();
}

int LenCtr(int Ctr){
	
	if (Ctr>0) 
		return 1;
	else return 0;
}

void Vipe(int **Arr){
	int i;

	for (i = 0; i < NMAX; i++)
        free(Arr[i]);
	free(Arr);
}