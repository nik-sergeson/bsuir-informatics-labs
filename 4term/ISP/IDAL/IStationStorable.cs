using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

    public interface IStationStorable
    {
        void Add(Station station);
        Station Read(int id);
        List<Station> ReadAll();
        void Update(Station station);
        void Delete(int id);
    }
