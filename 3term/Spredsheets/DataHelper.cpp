#include "DataHelper.h"
#include <vector>
#include <string>
#include "Cell.h"

std::vector<int> DataHelper::PrefixFunc(char *str){
int len=strlen(str);
std::vector<int> pi(len);
for(int i=1;i<len;i++){
   int j=pi[i-1];
   while((j>0)&&(str[j]!=str[i]))
      j=pi[j-1];
   if(str[i]==str[j])
      j++;
   pi[i]=j;
}
return pi;
}

bool DataHelper::FindSubString(char *basestr,char *substr){
char *tempst=new char[strlen(substr)];
strcpy(tempst,substr);
strcat(tempst,"#");
strcat(tempst,basestr);
int len=strlen(tempst)-strlen(basestr);
std::vector<int> prefs=PrefixFunc(tempst);
for(int i=len;i<strlen(tempst);i++){
   if(prefs[i]==len-1)
      return true;
}
return false;
}

void DataHelper::SortArr(int high,int low){
int i=low,j=high,m=(i+j)/2;
do{
   while(strcmp(_cellvec[i].GetData(),_cellvec[m].GetData())<0)
      ++i;
   while(strcmp(_cellvec[j].GetData(),_cellvec[m].GetData())>0)
      j--;
   if(i<=j){
      Cell temp=_cellvec[j];
      _cellvec[j]=_cellvec[i];
      _cellvec[i]=temp;
      i++;
      j--;
   }
}
while(i<j);
if(low<j)
   SortArr(j,low);
if(i<high)
   SortArr(high,i);
}

void DataHelper::RangeSearch(int Left,int Top,int Right,int Bottom,Table *table,char *Source){
while(!_rowresults.empty()){
   _rowresults.pop();
   _colresults.pop();
}
delete[] _lastsearch;
_lastsearch=NULL;
_lastsearch=new char[strlen(Source)];
strcpy(_lastsearch,Source);
for(int i=Left;i<=Right;i++){
   for(int j=Top;j<=Bottom;j++){
      if(FindSubString(table->GetData(j,i),Source)){
         _rowresults.push(j);
         _colresults.push(i);
      }
   }
}
}

int DataHelper::NextRow(){
if(!_rowresults.empty()){
   int res=_rowresults.front();
   _rowresults.pop();
   return res;
}
}

int DataHelper::NextCol(){
if(!_colresults.empty()){
   int res=_colresults.front();
   _colresults.pop();
   return res;
}
}

DataHelper::DataHelper(){
_lastsearch=NULL;
}

bool DataHelper::CacheSearch(char *string){
if((_lastsearch==NULL)||(strcmp(_lastsearch,string)!=0))
   return false;
else
   return true;
}

void DataHelper::RangeSort(int Left,int Top,int Right,int Bottom,Table *table){
for(int i=Left;i<=Right;i++){
   _cellvec=table->GetVec(i);
   SortArr(Bottom-1,Top-1);
}
}

DataHelper::~DataHelper(){
delete[] _lastsearch;
}
