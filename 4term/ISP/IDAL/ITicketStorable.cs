using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public interface ITicketStorable
{
    void Add(Ticket ticket);
    Ticket Read(int id);
    List<Ticket> ReadAllForPlane(int planeid);
    List<Ticket> ReadAllForClient(int ownerid);
    void Update(Ticket ticket);
    void Delete(int id);
    List<Ticket> ReadAll();
}
