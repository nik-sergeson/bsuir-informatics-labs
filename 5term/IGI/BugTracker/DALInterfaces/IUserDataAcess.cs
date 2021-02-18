using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Entities;

namespace DALInterfaces
{
    public interface IUserDataAccess
    {
        void Create(User user, string paswdHash);
        User Read(int id);
        User Read(string login);
        IEnumerable<User> ReadAll();
        void Update(User user);
        void Delete(User user);
        void Delete(int id);
    }
}
