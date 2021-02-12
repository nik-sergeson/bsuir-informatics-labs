#include "EquSolver.h"
#include "Cell.h"
#include <stdlib>
#include <math>
#include <string>

char* Cell::GetData()
{
if(_data==NULL){
   return "\0";
}
else
   return _data;
}

Cell::Cell()
{
_data=NULL;
_links=NULL;
_linksize=0;
_linkposition=0;
}

void Cell::SetString(char* Source)
{
if(_data!=NULL)
   delete[] _data;
if(!((Source==NULL)||(strlen(Source)==0))){
   _data=new char[strlen(Source)];
   strcpy(_data, Source);
   _data[strlen(Source)]='\0';
}
}

void Cell::SetLink(int Row,int Col){
if(_linksize==_linkposition){
   int **temp=new int*[_linksize+20];
   for(int i=0;i<_linksize;i++){
      temp[i]=new int[2];
      temp[i][0]=_links[i][0];
      temp[i][1]=_links[i][1];
      delete[] _links[i];
   }
   if(_links!=NULL)
      delete[] _links;
    for(int j=_linksize;j<_linksize+20;j++){
       temp[j]=new int[2];
    }
    _linksize=_linksize+20;
   _links=temp;
}
_links[_linkposition][0]=Row-1;
_links[_linkposition][1]=Col-1;
_linkposition++;
}

void Cell::DeleteLink(int Row,int Col){
int i=0;
for(i;i<_linkposition;i++){
  if((_links[i][0]==Row-1)&&(_links[i][1]==Col-1)){
     break;
  }
}
for(int j=i;j<_linkposition;j++){
   _links[j][0]=_links[j+1][0];
    _links[j][1]==_links[j+1][1];
}
_linkposition--;
}

void Cell::DeleteLinks(){
int i=0;
for(i;i<_linkposition;i++)
   delete[] _links[i];
delete[] _links;
_linksize=0;
_linkposition=0;
}

int Cell::CountLinks(){
   return _linkposition;
}

int* Cell::LinkPosition(int Counter){
   if(Counter>_linkposition){
      return NULL;
   }
   else{
      return _links[Counter];
   }
}

Cell::~Cell(){
for(int i=0;i<_linksize;i++)
   delete[] _links[i];
if(_linksize!=0)
   delete[] _links;
if(_data!=NULL)
   delete[] _data;
}

Cell::Cell(const Cell & acell){
_data=new char[strlen(acell._data)];
strcpy(_data,acell._data);
_links=new int*[acell._linksize];
for(int i=0;i<acell._linksize;i++){
   _links[i]=new int[2];
   _links[i][0]=acell._links[i][0];
   _links[i][1]=acell._links[i][1];
}
_linksize=acell._linksize;
_linkposition=acell._linkposition;
}

Cell Cell::operator=(Cell acell){
delete[] _data;
_data=new char[strlen(acell._data)];
strcpy(_data,acell._data);
for(int i=0;i<_linksize;i++)
    delete[] _links[i];
delete[] _links;
_links=new int*[acell._linksize];
for(int i=0;i<acell._linksize;i++){
   _links[i]=new int[2];
   _links[i][0]=acell._links[i][0];
   _links[i][1]=acell._links[i][1];
}
_linksize=acell._linksize;
_linkposition=acell._linkposition;
return *this;
}
