using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Entities;

namespace DALInterfaces
{
    public interface ITaskDataAccess
    {
        void Create(Task task);
        Task Read(int id);
        void Update(Task task);
        void Delete(Task task);
        void Delete(int id);
        IEnumerable<Task> ReadAll(int projectId);
    }
}
