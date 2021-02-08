using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;

namespace ISP_5
{
    class Program
    {
        static void Main(string[] args)
        {
            var cfg = ConfigurationManager.OpenExeConfiguration("ISP-5.exe");
            var section=(CustomConfig) cfg.Sections["custom"];
            section.Pathinfo.Path = "blabla";
            cfg.Save();
        }
    }
}
