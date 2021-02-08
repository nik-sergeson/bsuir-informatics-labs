using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using FileSavers;

namespace FactoryFileSavers
{
    public class TextSaver : SaveManager
    {
        private class TextStorage : TextReaderWriter, IDocStorage
        {
        }

        public override IDocStorage Create()
        {
            return new TextStorage();
        }
    }
}