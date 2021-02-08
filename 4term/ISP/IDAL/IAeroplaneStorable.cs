using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public interface IAeroplaneStorable
{
    void Add(Aeroplane plane);
    Aeroplane Read(int id);
    List<Aeroplane> ReadAll(int flightid);
    void Update(Aeroplane plane);
    void Delete(int id);
    List<Aeroplane> ReadAll();
}
