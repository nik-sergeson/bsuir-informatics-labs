using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using FileSavers;

namespace FactoryFileSavers
{
    public class BinarySaver : SaveManager
    {
        private class BinaryStorage : BinaryReaderWriter, IDocStorage
        {
        }

        public override IDocStorage Create()
        {
            return new BinaryStorage();
        }
    }
}