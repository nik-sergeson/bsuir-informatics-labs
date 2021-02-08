using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solver
{
    public interface ISolver
    {
        int Priority(char oper);
        string ShuntingYard(string expression);
        double CountEquality(string opb);
    }
}
