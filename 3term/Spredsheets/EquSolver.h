//---------------------------------------------------------------------------

#ifndef EquSolverH
#define EquSolverH
#include <stack>
#include <set>
#include "Table.h"

class EquSolver{
static std::set<char> _operations;
public:
static int Prior(char Symb);
static char* OBP(char *Equality);
static double Solve(char* Postform, Table *table);
};

//---------------------------------------------------------------------------
#endif
