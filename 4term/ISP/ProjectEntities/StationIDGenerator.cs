using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BLL
{
    public class StationIDGenerator
    {
        private int _id = int.MaxValue;

        public static StationIDGenerator IDGenerator { get; private set; }

        private StationIDGenerator() { }

        static StationIDGenerator()
        {
            IDGenerator = new StationIDGenerator();
        }

        public int GetID()
        {
            _id--;
            return _id;
        }
    }
}
