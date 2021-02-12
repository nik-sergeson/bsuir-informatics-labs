#include "Cell.h"
#include "EquSolver.h"
#include <stdlib>
#include <string>
#include<stack>
#include <Grids.hpp>
#include "DataHelper.h"
#include<math>
#include "Table.h"

Table::Table(){
_cols=0;
_rows=0;
_adddim=20;
_cellchanged=false;
_typformula=false;
_cellarr=NULL;
_selectionrows=0;
_selectioncols=0;
}

Table::Table(int Collc, int Rowc){
_cols=Collc;
_adddim=20;
_cellchanged=false;
_rows=Rowc;
_typformula=false;
_cellarr=new Cell *[Collc];
for(int i=0;i<Collc;i++){
   _cellarr[i]=new Cell[Rowc];
}
_tempselection=NULL;
_selectionrows=0;
_selectioncols=0;
}

void Table::Update(int Collc,int Rows, char *Str)
{
if((_cols>Collc)&&(_rows>Rows)){
   _cellarr[Collc-1][Rows-1].SetString(Str);
}
else{
   Resize(Collc+Table::_adddim,Rows+Table::_adddim);
   _cellarr[Collc-1][Rows-1].SetString(Str);
}
}

void Table::Resize(int Collc, int Rowc){
Cell **temparr=new Cell *[Collc];
for(int i=0;i<Collc;i++){
    temparr[i]=new Cell[Rowc];
}
for(int i=0;i<_cols;i++){
    for(int j=0;j<_rows;j++){
       temparr[i][j].SetString(_cellarr[i][j].GetData());
    }
}
for(int i=0;i<_cols;i++)
   delete[] _cellarr[i];
delete[] _cellarr;
_cellarr=temparr;
_cols=Collc;
_rows=Rowc;
}

int *Table::GetIndex(char *str){
std::stack<char> val;
int j=0,count=0;
int *ind=new int[2];
ind[0]=0;
ind[1]=0;
while(str[j]>57){
   val.push(str[j]);
   j++;
}
for(j;j<strlen(str);j++){
   ind[1]=ind[1]*10+((int)str[j]-48);
}
int valsize=val.size();
while(val.empty()!=true){
 if ((val.size()==1)&&(valsize!=1))
     ind[0]=ind[0]+pow(26,count)*((int)val.top()-64);
 else
     ind[0]=ind[0]+pow(26,count)*((int)val.top()-65);
 ++count;
 val.pop();
}
return ind;
}

Cell* Table::GetCell(int Row,int Col){
if((Row>_rows)||(Col>_cols))
   return NULL;
return &_cellarr[Col-1][Row-1];
}

bool Table::TypFor(){
return _typformula;
}

void Table::FTypMod(bool isformula){
_typformula=isformula;
}

int Table::GetFormCol(){
return _formcol+1;
}

int Table::GetFormRow(){
return _formrow+1;
}

void Table::SetFormCol(int Col){
_formcol=Col-1;
}

void Table::SetFormRow(int Row){
_formrow=Row-1;
}

void Table::SetCurrCell(int Row,int Col){
_curcellrow=Row-1;
_curcellcol=Col-1;
}

int Table::GetCurRow(){
return _curcellrow+1;
}

int Table::GetCurCol(){
return _curcellcol+1;
}

bool Table::IfCellChanged(){
return _cellchanged;
}

void Table::CellChanged(bool Chg){
_cellchanged=Chg;
}

char* Table::ColName(int Col){
char* name=new char[20];
int j=0;
std::stack<int> ost;
if(Col==0){
   name[0]='A';
   name[1]='\0';
   return name;
}
while(Col>0){
   ost.push(Col%26);
   Col=Col/26;
}
if((!ost.empty())&&(ost.size()!=1)){
   name[j]=64+ost.top();
   ost.pop();
   j++;
}
while(ost.size()>0){
   name[j]=65+ost.top();
   ost.pop();
   j++;
}
name[j]='\0';
return name;
}

char* Table::CellAddr(int Row,int Col){
char* addr=new char[20];
std::stack<int> ost;
strcpy(addr,Table::ColName(Col));
int j=strlen(addr);
if(Row==0){
   addr[j]='0';
   addr[j+1]='\0';
   return addr;
}
while(Row>0){
   ost.push(Row%10);
   Row=Row/10;
}
while(!ost.empty()){
   addr[j]=48+ost.top();
   j++;
   ost.pop();
}
addr[j]='\0';
return addr;
}

bool Table::LinkAnalyzer(int Row,int Col,char* Postform,Table *table)
{
char *curoper=new char [11];
int *index;
char ch;
int j;
Cell *tempcell;
for(int i=1;i<strlen(Postform);i++){
   ch=Postform[i];
   if(!(((ch>='0')&&(ch<='9'))||((ch>='A')&&(ch<='Z')))){
      continue;
   }
   j=0;
   while(((ch>='0')&&(ch<='9'))||((ch>='A')&&(ch<='Z'))){
     curoper[j]=ch;
     i++;
     j++;
     ch=Postform[i];
   }
     i--;
     curoper[j]='\0';
     if(!((curoper[0]>='A')&&(curoper[0]<='Z')))
        continue;
     index=Table::GetIndex(curoper);
     tempcell=table->GetCell(index[1]+1,index[0]+1);
     int *link;
     Cell* curcell=table->GetCell(Row,Col);
     for(int k=0;k<curcell->CountLinks();k++){
        link=table->GetCell(Row,Col)->LinkPosition(k);
        if((link[0]==index[1])&&(link[1]==index[0]))
           return false;
     }
     tempcell->SetLink(Row,Col);
}
return true;
}

void Table::LinkDestroyer(int Row,int Col,char* Postform,Table *table)
{
char *curoper=new char [11];
char ch;
int *index,j;
Cell *tempcell;
for(int i=1;i<strlen(Postform);i++){
   ch=Postform[i];
   if(!(((ch>='0')&&(ch<='9'))||((ch>='A')&&(ch<='Z')))){
      continue;
   }
   j=0;
   while(((ch>='0')&&(ch<='9'))||((ch>='A')&&(ch<='Z'))){
     curoper[j]=ch;
     i++;
     j++;
     ch=Postform[i];
   }
     i--;
     curoper[j]='\0';
     index=Table::GetIndex(curoper);
     tempcell=table->GetCell(index[1]+1,index[0]+1);
     tempcell->DeleteLink(Row,Col);
}
}

bool Table::EditCell(char* Source, TStringGrid* GR,int Row,int Col){
char *oldinfo=GetCell(Row,Col)->GetData();
if((Col<=_cols)&&(Row<=_rows)){
  char *data=GetCell(Row,Col)->GetData();
   if(data[0]=='='){
       LinkDestroyer(Row,Col,data,this);
   }
}
_infobackup.push_back(oldinfo);
_infocol.push_back(Col-1);
_inforow.push_back(Row-1);
if(_infobackup.size()>10){
    _infobackup.pop_front();
    _inforow.pop_front();
    _infocol.pop_front();
}
if(DataHelper::FindSubString(Source,Table::CellAddr(Row-1,Col-1))){
    Update(Col,Row,"");
    GR->Cells[Col][Row]="ЗНАЧ";
    return false;
}
Update(Col,Row,Source);
if(Source[0]=='='){
      if(!LinkAnalyzer(Row,Col,Source,this)){
         Update(Col,Row,"");
         GR->Cells[Col][Row]="ЗНАЧ";
         return false;
      }
}
LinkObserver(GR,Row,Col);
return true;
}

void Table::LinkObserver(TStringGrid* GR,int Row,int Col){
int *link;
for(int i=0;i<_cellarr[Col-1][Row-1].CountLinks();i++){
   link=_cellarr[Col-1][Row-1].LinkPosition(i);
   LinkObserver(GR,link[0]+1,link[1]+1);
}
if(_cellarr[Col-1][Row-1].GetData()[0]=='=')
    GR->Cells[Col][Row]=EquSolver::Solve(EquSolver::OBP(_cellarr[Col-1][Row-1].GetData()),this);
}

int Table::GetRowCount(){
   return _rows;
}

int Table::GetColCount(){
   return _cols;
}

void Table::RestoreBackUp(){
if(!_infobackup.empty()){
   Cell *curcell=GetCell(_inforow.back()+1,_infocol.back()+1);
   char *str=_infobackup.back();
   curcell->SetString(_infobackup.back());
   _curcellrow=_inforow.back();
   _curcellcol=_infocol.back();
   _infobackup.pop_back();
   _inforow.pop_back();
   _infocol.pop_back();
}
}

char* Table::GetData(int Row,int Col){
   return _cellarr[Col-1][Row-1].GetData();
}

void Table::CopySelection(int Width,int Height){
for(int i=1;i<=_selectioncols;i++)
    delete[] _tempselection[i-1];
if(_selectioncols!=0)
    delete[] _tempselection;
_selectioncols=Width;
_selectionrows=Height;
_selectiontop=_curcellrow;
_selectionleft=_curcellcol;
_tempselection=new Cell*[_selectioncols];
for(int i=1;i<=_selectioncols;i++)
   _tempselection[i-1]=new Cell[_selectionrows];
for(int i=0;i<_selectioncols;i++){
    for(int j=0;j<_selectionrows;j++){
        _tempselection[i][j].SetString(_cellarr[_curcellcol+i][_curcellrow+j].GetData());
    }
}
}

void Table::InsertSelection(TStringGrid* GR,int Row,int Col){
if((Row+_selectionrows>=_rows)||(Col+_selectioncols>=_cols))
    Resize(Col+_selectioncols+Table::_adddim,Row+_selectionrows+Table::_adddim);
for(int i=0;i<_selectioncols;i++){
    for(int j=0;j<_selectionrows;j++){
        if(_tempselection[i][j].GetData()[0]!='='){
           EditCell(_tempselection[i][j].GetData(),GR,Row+j,Col+i);
        }
        else{
            char* movedform=new char[strlen(_tempselection[i][j].GetData())*2],*celldata=_tempselection[i][j].GetData(),*curoper=new char[11],ch;
            int l=0,k;
            for(int m=0;m<strlen(celldata);m++){
               ch=celldata[m];
               if(!(((ch>='0')&&(ch<='9'))||((ch>='A')&&(ch<='Z')))){
                  movedform[l]=ch;
                  l++;
                  continue;
               }
               k=0;
               while(((ch>='0')&&(ch<='9'))||((ch>='A')&&(ch<='Z'))){
                  curoper[k]=ch;
                  m++;
                  k++;
                  ch=celldata[m];
               }
               m--;
               curoper[k]='\0';
               int* index=Table::GetIndex(curoper);
               if((curoper[0]>='A')&&(curoper[0]<='Z')){
                   char* str=CellAddr(index[1]-_selectiontop+Row-1,index[0]-_selectionleft+Col-1);
                   for(int n=0;n<strlen(str);n++){
                      movedform[l]=str[n];
                      l++;
                    }
               }
               else{
                   for(int n=0;n<strlen(curoper);n++){
                      movedform[l]=curoper[n];
                      l++;
                    }
               }
            }
            movedform[l]='\0';
            EditCell(movedform,GR,Row+j,Col+i);
        }
    }
}
}

bool Table::CopyIsAvailable(){
if(_tempselection==NULL)
   return false;
else
   return true;
}

int Table::GetSelectionLength(){
return _selectioncols;
}

int Table::GetSelectionWidth(){
return _selectionrows;
}

Cell* Table::GetVec(int Col){
return _cellarr[Col-1];
}

Table::~Table(){
for(int i=0;i<_cols;i++){
   delete[] _cellarr[i];
   if(_tempselection!=NULL)
      delete[] _tempselection[i];
}
if(_tempselection!=NULL)
   delete[] _tempselection;
delete[] _cellarr;
}
