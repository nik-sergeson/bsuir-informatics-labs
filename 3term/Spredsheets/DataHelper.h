//---------------------------------------------------------------------------

#ifndef DataHelperH
#define DataHelperH
#include <vector>
#include <queue>
#include "Cell.h"
#include "Table.h"

class DataHelper{
std::queue<int> _rowresults;
std::queue<int> _colresults;
Cell *_cellvec;
char *_lastsearch;
public:
DataHelper();
static std::vector<int> PrefixFunc(char *str);
static bool FindSubString(char *basestr,char *substr);
void SortArr(int high,int low);
void RangeSearch(int Left,int Top,int Right,int Bottom,Table *table,char *Source);
int NextCol();
int NextRow();
bool CacheSearch(char *string);
void RangeSort(int Left,int Top,int Right,int Bottom,Table *table);
~DataHelper();
};
//---------------------------------------------------------------------------
#endif
