using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

    public interface IFlightStorable
    {
        void Add(Flight flight);
        Flight Read(int id);
        List<Flight> ReadAll();
        void Update(Flight flight);
        void Delete(int id);
    }
