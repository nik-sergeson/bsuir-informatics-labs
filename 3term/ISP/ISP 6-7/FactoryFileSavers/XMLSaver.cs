using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using System.Xml.Linq;
using System.Threading.Tasks;
using FileSavers;

namespace FactoryFileSavers
{
    public class XMLSaver : SaveManager
    {
        private class XMLStorage : XMLReaderWriter, IDocStorage
        {
        }

        public override IDocStorage Create()
        {
            return new XMLStorage();
        }
    }
}