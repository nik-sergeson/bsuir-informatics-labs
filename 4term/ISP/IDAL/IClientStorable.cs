using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public interface IClientStorable
{
    void Add(Client client);
    Client Read(int id);
    void Update(Client client);
    void Delete(int id);
    List<Client> ReadAll();
}