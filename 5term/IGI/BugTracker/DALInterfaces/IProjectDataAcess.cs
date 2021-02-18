using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Entities;

namespace DALInterfaces
{
    public interface IProjectDataAccess
    {
        void Create(Project project);
        Project Read(int id);
        IEnumerable<Project> ReadAll();
        IEnumerable<Project> ReadAuthorProject(int id);
        void Update(Project project);
        void Delete(Project project);
        void Delete(int id);
    }
}
