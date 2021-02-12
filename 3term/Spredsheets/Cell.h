//---------------------------------------------------------------------------

#ifndef CellH
#define CellH
#include <Grids.hpp>
class Cell
{
char* _data;
int** _links;
int _linksize;
int _linkposition;
public:
Cell();
Cell(const Cell & acell);
void Resize(int Size);
char* GetData();
void SetString(char* Source);
void SetLink(int Row,int Col);
void DeleteLink(int Row,int Col);
int CountLinks();
void DeleteLinks();
int* LinkPosition(int Counter);
Cell operator=(Cell acell);
~Cell();
};
#endif
