//---------------------------------------------------------------------------

#ifndef FileHelperH
#define FileHelperH
#include "Table.h"
#include <Grids.hpp>

class FileHelper{
public:
static bool WriteTable(char *path,Table *table);
static Table* ReadTable(char *path,TStringGrid *gr);
};
//---------------------------------------------------------------------------
#endif
