using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IDAL
{
    public interface IStorable<T>
    {
        void Add(T obj);
        T Read(int id);
        List<T> ReadAll();
        void Update(T obj);
        void Delete(int id);
    }
}
