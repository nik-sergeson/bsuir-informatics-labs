//---------------------------------------------------------------------------

#ifndef TableH
#define TableH
#include "Cell.h"
#include <Grids.hpp>
#include <deque>
class Table
{
std::deque<char *> _infobackup;
std::deque<int> _inforow;
std::deque<int> _infocol;
int _cols;
int _rows;
int _adddim;
bool _typformula;
int _formcol;
int _formrow;
int _curcellrow;
int _selectioncols;
int _selectionrows;
bool _cellchanged;
int _curcellcol;
int _selectiontop;
int _selectionleft;
Cell **_cellarr;
Cell **_tempselection;
public:
Table();
Table(int Collc, int Rowc);
void Update(int Collc,int Rows, char *Str);
void Resize(int Collc,int Rowc);
static int * GetIndex(char *str);
Cell* GetCell(int Row,int Col);
bool TypFor();
void FTypMod(bool isformula);
int GetFormCol();
int GetFormRow();
char* GetData(int Row,int Col);
void SetFormCol(int Col);
void SetFormRow(int Row);
void SetCurrCell(int Row,int Col);
int GetCurRow();
int GetCurCol();
int GetRowCount();
int GetColCount();
bool IfCellChanged();
void CellChanged(bool Chg);
static char* ColName(int Col);
static char* CellAddr(int Row,int Col);
static bool LinkAnalyzer(int Row,int Col,char* Postform,Table *table);
static void LinkDestroyer(int Row,int Col,char* Postform,Table *table);
bool EditCell(char* Source, TStringGrid* GR,int Row,int Col);
void RestoreBackUp();
void CopySelection(int Width,int Height);
void InsertSelection(TStringGrid* GR,int Row,int Col);
bool CopyIsAvailable();
int GetSelectionLength();
int GetSelectionWidth();
Cell *GetVec(int Col);
void LinkObserver(TStringGrid* GR,int Row,int Col);
~Table();
};
//---------------------------------------------------------------------------
#endif
