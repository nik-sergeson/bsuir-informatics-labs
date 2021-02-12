#pragma hdrstop
#include "FileHelper.h"
#include "Cell.h"
#include <stdio.h>
#include <stdlib.h>
#include <Grids.hpp>
using namespace std;

bool FileHelper::WriteTable(char *path,Table *table){
FILE *fp;
if((fp=fopen(path,"wb+"))==NULL){
   return false;
}
int cols=table->GetColCount(),rows=table->GetRowCount();
fwrite(&rows,sizeof(int),1,fp);
fwrite(&cols,sizeof(int),1,fp);
for(int i=1;i<=table->GetColCount();i++){
    for(int j=1;j<=table->GetRowCount();j++){
        char *temp=table->GetCell(j,i)->GetData();
        int size=strlen(temp);
        fwrite(&size,sizeof(int),1,fp);
        for(int k=1;k<=size;k++){
           fwrite(&temp[k-1],sizeof(char),1,fp);
        }
        int linksize=table->GetCell(j,i)->CountLinks();
        fwrite(&linksize,sizeof(int),1,fp);
        for(int n=0;n<linksize;n++){
           int *templink=table->GetCell(j,i)->LinkPosition(n);
           ++templink[0];
           ++templink[1];
           fwrite(&templink[0],sizeof(int),1,fp);
           fwrite(&templink[1],sizeof(int),1,fp);
        }
    }
}
fclose(fp);
return true;
}

Table* FileHelper::ReadTable(char *path,TStringGrid *gr){
FILE *fp;
int k;
if((fp=fopen(path,"rb+"))==NULL){
   return NULL;
}
int cols,rows;
for(int i=2;i<=gr->ColCount;i++){
   gr->Cols[i]->Clear();
}
for(int i=1;i<=gr->ColCount;i++)
    gr->Cells[i][0]=Table::ColName(i-1);
fread(&rows,sizeof(int),1,fp);
fread(&cols,sizeof(int),1,fp);
Table *tempt=new Table(cols,rows);
for(int i=1;i<=cols;i++){
    for(int j=1;j<=rows;j++){
        int size;
        fread(&size,sizeof(int),1,fp);
        char *tempd=(char *)malloc(size*sizeof(char));
        for(k=1;k<=size;k++){
           fread(&tempd[k-1],sizeof(char),1,fp);
        }
        if(size!=0){
           tempd[k-1]='\0';
        }
        tempt->Update(i,j,tempd);
        if(size!=0){
           gr->Cells[i][j]=tempd;
        }
        int linksize;
        fread(&linksize,sizeof(int),1,fp);
        for(int n=0;n<linksize;n++){
           int linkrow,linkcol;
           Cell *tempc=tempt->GetCell(j,i);
           fread(&linkrow,sizeof(int),1,fp);
           fwrite(&linkcol,sizeof(int),1,fp);
           tempc->SetLink(linkrow,linkcol);
        }
    }
}
return tempt;
}
