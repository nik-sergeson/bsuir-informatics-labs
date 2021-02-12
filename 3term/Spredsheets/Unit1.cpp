//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
#include "Table.h"
#include "DataHelper.h"
#include "Cell.h"
#include "EquSolver.h"
#include <string>
#include "FileHelper.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
Table *table;
DataHelper *helper;
char operations[]={'+','-','*','/','^','(',')'};
std::set<char> EquSolver::_operations(operations,operations+7);

//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
        : TForm(Owner)
{
}
//---------------------------------------------------------------------------

void __fastcall TForm1::FormCreate(TObject *Sender)
{
Table* stable=new Table(1,4);
Edit1->Text="";
Edit2->Text="";
Edit3->Text="";
Edit3->Visible=false;
StringGrid1->Cells[1][1]=2;
StringGrid1->Cells[1][2]=2;
StringGrid1->Cells[1][3]=2;
for(int i=1;i<=StringGrid1->ColCount;i++)
    StringGrid1->Cells[i][0]=stable->ColName(i-1);
for(int i=1;i<=StringGrid1->RowCount;i++)
    StringGrid1->Cells[0][i]=i-1;
table=stable;
table->Update(1,1,"2");
table->Update(1,2,"2");
table->Update(1,3,"2");
table->SetCurrCell(-1,-1);
table->FTypMod(false);
table->CellChanged(false);
N12->Visible=false;
helper=new DataHelper();
ScrollBar1->PageSize=(int)((double)StringGrid1->VisibleColCount/(double)StringGrid1->ColCount*100)+9;
ScrollBar2->PageSize=(int)((double)StringGrid1->VisibleRowCount/(double)StringGrid1->RowCount*100)+9;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::ScrollBar2Change(TObject *Sender)
{
if(ScrollBar2->Position+ScrollBar2->PageSize==ScrollBar2->Max){
   StringGrid1->RowCount=StringGrid1->RowCount+30;
   ScrollBar2->PageSize=(int)((double)StringGrid1->VisibleRowCount/(double)StringGrid1->RowCount*100);
   for(int i=StringGrid1->RowCount-30;i<=StringGrid1->RowCount;i++)
      StringGrid1->Cells[0][i]=i-1;
}
StringGrid1->TopRow=ScrollBar2->Position*((double)(StringGrid1->RowCount-StringGrid1->VisibleRowCount)/(double)(ScrollBar2->Max-ScrollBar2->PageSize))+1;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::StringGrid1SelectCell(TObject *Sender, int ACol,
      int ARow, bool &CanSelect)
{
if(!table->IfCellChanged()){
   if(table->TypFor()){
      char *temp=new char[strlen(StringGrid1->Cells[table->GetFormCol()][table->GetFormRow()].c_str())];
      strcpy(temp,StringGrid1->Cells[table->GetFormCol()][table->GetFormRow()].c_str());
      strcat(temp,Table::CellAddr(ARow-1,ACol-1));
      StringGrid1->Cells[table->GetFormCol()][table->GetFormRow()]=temp;
      table->CellChanged(true);
   }
   else if((table->GetCurRow()>=0)&&!(table->CopyIsAvailable())){
      table->EditCell(StringGrid1->Cells[table->GetCurCol()][table->GetCurRow()].c_str(),StringGrid1,table->GetCurRow(),table->GetCurCol());
      table->SetCurrCell(-1,-1);
   }
}
Edit1->Text=Table::CellAddr(ARow-1,ACol-1);
Cell *temp=table->GetCell(ARow,ACol);
   if(temp!=NULL)
      Edit2->Text=temp->GetData();
}
//---------------------------------------------------------------------------

void __fastcall TForm1::StringGrid1MouseWheelDown(TObject *Sender,
      TShiftState Shift, TPoint &MousePos, bool &Handled)
{
if(StringGrid1->VisibleRowCount+StringGrid1->TopRow==StringGrid1->RowCount){
   StringGrid1->RowCount=StringGrid1->RowCount+30;
   ScrollBar2->PageSize=(int)((double)StringGrid1->VisibleRowCount/(double)StringGrid1->RowCount*100);
   for(int i=StringGrid1->RowCount-30;i<=StringGrid1->RowCount;i++)
      StringGrid1->Cells[0][i]=i-1;
}
ScrollBar2->Position=(StringGrid1->TopRow-1)/((double)(StringGrid1->RowCount-StringGrid1->VisibleRowCount)/(double)(ScrollBar2->Max-ScrollBar2->PageSize));
StringGrid1->Perform(WM_VSCROLL,1,0);
Handled=true;
}
//---------------------------------------------------------------------------

void __fastcall TForm1::StringGrid1MouseWheelUp(TObject *Sender,
      TShiftState Shift, TPoint &MousePos, bool &Handled)
{
StringGrid1->Perform(WM_VSCROLL,0,0);
ScrollBar2->Position=(StringGrid1->TopRow-1)/((double)(StringGrid1->RowCount-StringGrid1->VisibleRowCount)/(double)(ScrollBar2->Max-ScrollBar2->PageSize));
Handled=true;
}
//---------------------------------------------------------------------------

void __fastcall TForm1::ScrollBar1Change(TObject *Sender)
{
if(ScrollBar1->Position+ScrollBar1->PageSize==ScrollBar1->Max){
   StringGrid1->ColCount=StringGrid1->ColCount+30;
   ScrollBar1->PageSize=(int)((double)StringGrid1->VisibleColCount/(double)StringGrid1->ColCount*100);
   for(int i=StringGrid1->ColCount-30;i<=StringGrid1->ColCount;i++)
      StringGrid1->Cells[i][0]=table->ColName(i-1);
}
StringGrid1->LeftCol=ScrollBar1->Position*((double)(StringGrid1->ColCount-StringGrid1->VisibleColCount)/(double)(ScrollBar1->Max-ScrollBar1->PageSize))+1;
}
//---------------------------------------------------------------------------


void __fastcall TForm1::StringGrid1SetEditText(TObject *Sender, int ACol,
      int ARow, const AnsiString Value)
{
if((table->TypFor())&&(table->IfCellChanged())){
   StringGrid1->Col=table->GetFormCol();
   StringGrid1->Row=table->GetFormRow();
   StringGrid1->EditorMode=true;
   StringGrid1->SetFocus();
   keybd_event(VK_RIGHT,0,0,0);
   table->CellChanged(false);
}
}
//---------------------------------------------------------------------------


void __fastcall TForm1::StringGrid1KeyPress(TObject *Sender, char &Key)
{
if(strlen(StringGrid1->Cells[StringGrid1->Col][StringGrid1->Row].c_str())==0 ){
   if(Key==61){
      table->FTypMod(true);
      table->SetFormCol(StringGrid1->Col);
      table->SetFormRow(StringGrid1->Row);
   }
   else{
      table->FTypMod(false);
   }
}
if((Key==13)&&(!table->TypFor())){
    table->EditCell(StringGrid1->Cells[table->GetCurCol()][table->GetCurRow()].c_str(),StringGrid1,table->GetCurRow(),table->GetCurCol());
    Cell *temp=table->GetCell(table->GetCurRow(),table->GetCurCol());
   if(temp!=NULL)
      Edit2->Text=temp->GetData();
    table->SetCurrCell(-1,-1);
}
if((Key==13)&&(table->TypFor())){
char * str=StringGrid1->Cells[table->GetFormCol()][table->GetFormRow()].c_str();
if(table->EditCell(StringGrid1->Cells[table->GetFormCol()][table->GetFormRow()].c_str(),StringGrid1,table->GetFormRow(),table->GetFormCol())){
  // Cell *tempcell=table->GetCell(table->GetFormRow(),table->GetFormCol());
   //StringGrid1->Cells[table->GetFormCol()][table->GetFormRow()]=EquSolver::Solve(EquSolver::OBP(tempcell->GetData()),table);
}
   table->SetCurrCell(-1,-1);
   table->FTypMod(false);
   Cell *temp=table->GetCell(table->GetFormRow(),table->GetFormCol());
   if(temp!=NULL)
      Edit2->Text=temp->GetData();
}
}
//---------------------------------------------------------------------------


void __fastcall TForm1::StringGrid1GetEditText(TObject *Sender, int ACol,
      int ARow, AnsiString &Value)
{
if(!table->TypFor()){
   table->SetCurrCell(ARow,ACol);
}
}
//---------------------------------------------------------------------------



void __fastcall TForm1::N1Click(TObject *Sender)
{
SetCurrentDirectory("D:\\PrTable\\Tables");
OpenDialog1->InitialDir=GetCurrentDir();
OpenDialog1->FileName="MyTable1";
OpenDialog1->Execute();
table=FileHelper::ReadTable(OpenDialog1->FileName.c_str(),StringGrid1);
}
//---------------------------------------------------------------------------

void __fastcall TForm1::N2Click(TObject *Sender)
{
SetCurrentDirectory("D:\\PrTable\\Tables");
SaveDialog1->InitialDir=GetCurrentDir();
SaveDialog1->FileName="MyTable1";
SaveDialog1->DefaultExt=".dat";
SaveDialog1->Execute();
FileHelper::WriteTable(SaveDialog1->FileName.c_str(),table);
}
//---------------------------------------------------------------------------



void __fastcall TForm1::Edit2KeyPress(TObject *Sender, char &Key)
{
if(Key==13){
   table->EditCell(Edit2->Text.c_str(),StringGrid1,StringGrid1->Row,StringGrid1->Col);
}
}
//---------------------------------------------------------------------------

void __fastcall TForm1::N4Click(TObject *Sender)
{
table->RestoreBackUp();
char *str=table->GetData(table->GetCurRow(),table->GetCurCol());
StringGrid1->Cells[table->GetCurCol()][table->GetCurRow()]=str;
}
//---------------------------------------------------------------------------


void __fastcall TForm1::StringGrid1MouseDown(TObject *Sender,
      TMouseButton Button, TShiftState Shift, int X, int Y)
{
if(Button==mbRight){
    if(StringGrid1->Options.Contains(goEditing)){
       StringGrid1->Options=StringGrid1->Options>>goEditing;
       N5->Visible=true;
    }
    else{
       N5->Visible=false;
       N12->Visible=false;
       StringGrid1->Options=StringGrid1->Options<<goEditing;
    }
}
}
//---------------------------------------------------------------------------



void __fastcall TForm1::N5Click(TObject *Sender)
{
table->SetCurrCell(StringGrid1->Row,StringGrid1->Col);
table->CopySelection(StringGrid1->Selection.Right-StringGrid1->Selection.Left+1,StringGrid1->Selection.Bottom-StringGrid1->Selection.Top+1);
N12->Visible=true;
}
//---------------------------------------------------------------------------

void __fastcall TForm1::N7Click(TObject *Sender)
{
int maxlength=0;
for(int i=1;i<=table->GetRowCount();i++){
   if(maxlength<strlen(table->GetData(i,StringGrid1->Col)))
      maxlength=strlen(table->GetData(i,StringGrid1->Col));
}
StringGrid1->ColWidths[StringGrid1->Col]=(int)(maxlength*6.4)+1;
}
//---------------------------------------------------------------------------



void __fastcall TForm1::N9Click(TObject *Sender)
{
Edit3->Text="Введите ключевое слово для поиска";
Edit3->Visible=true;
}
//---------------------------------------------------------------------------

void __fastcall TForm1::N10Click(TObject *Sender)
{
helper->RangeSort(StringGrid1->Selection.Left,StringGrid1->Selection.Top,StringGrid1->Selection.Right,StringGrid1->Selection.Bottom,table);
for(int i=StringGrid1->Selection.Left;i<=StringGrid1->Selection.Right;i++)
    for(int j=StringGrid1->Selection.Top;j<=StringGrid1->Selection.Bottom;j++)
       StringGrid1->Cells[i][j]=table->GetData(j,i);
}
//---------------------------------------------------------------------------

void __fastcall TForm1::N11Click(TObject *Sender)
{
delete helper;
delete table;
Form1->Visible=false;
}
//---------------------------------------------------------------------------



void __fastcall TForm1::Edit3KeyPress(TObject *Sender, char &Key)
{
if(Key==13){
   if(!helper->CacheSearch(Edit3->Text.c_str())){
      if((StringGrid1->Selection.Left==StringGrid1->Selection.Right)&&(StringGrid1->Selection.Top==StringGrid1->Selection.Bottom))
         helper->RangeSearch(1,1,table->GetColCount(),table->GetRowCount(),table,Edit3->Text.c_str());
      else
         helper->RangeSearch(StringGrid1->Selection.Left,StringGrid1->Selection.Top,StringGrid1->Selection.Right,StringGrid1->Selection.Bottom,table,Edit3->Text.c_str());
   }
    StringGrid1->Col=helper->NextCol();
    StringGrid1->Row=helper->NextRow();
}
if(Key==27)
   Edit3->Visible=false;
}
//---------------------------------------------------------------------------


void __fastcall TForm1::StringGrid1DblClick(TObject *Sender)
{
char *tempstr=new char[strlen(table->GetData(StringGrid1->Row,StringGrid1->Col))];
strcpy(tempstr,table->GetData(StringGrid1->Row,StringGrid1->Col));
tempstr[strlen(table->GetData(StringGrid1->Row,StringGrid1->Col))]='\0';
StringGrid1->Cells[StringGrid1->Col][StringGrid1->Row]=tempstr;
StringGrid1->EditorMode=true;
table->CellChanged(true);
StringGrid1->SetFocus();
keybd_event(VK_RIGHT,0,0,0);
if(table->GetData(StringGrid1->Row,StringGrid1->Col)[0]=='='){
   table->FTypMod(true);
   table->SetFormCol(StringGrid1->Col);
   table->SetFormRow(StringGrid1->Row);
}
}
//---------------------------------------------------------------------------


void __fastcall TForm1::N12Click(TObject *Sender)
{
int width=table->GetSelectionWidth(),length=table->GetSelectionLength();
int rows=StringGrid1->Row,cols=StringGrid1->Col;
table->InsertSelection(StringGrid1,rows,cols);
for(int i=rows;i<=rows+width;i++){
  for(int j=cols;j<=cols+length;j++){
      if(table->GetData(i,j)[0]=='=')
        StringGrid1->Cells[j][i]=EquSolver::Solve(EquSolver::OBP(table->GetData(i,j)),table);
     else
         StringGrid1->Cells[j][i]=table->GetData(i,j);
    }
}
}
//---------------------------------------------------------------------------

