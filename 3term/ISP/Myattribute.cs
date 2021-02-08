using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solver
{
    [AttributeUsage(AttributeTargets.Class)]
    public class Myattribute:Attribute
    {
        public string PluginName { get; private set; }
        public string Build{get; set;}
        public Myattribute(string name)
        {
            PluginName=name;
        }
    }
}
