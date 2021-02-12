using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solver
{
    [AttributeUsage(AttributeTargets.Class)]
    public class MyAttribute:Attribute
    {
        public string PluginName { get; private set; }
        public string Build{get; set;}
        public MyAttribute(string name)
        {
            PluginName=name;
        }
    }
}
