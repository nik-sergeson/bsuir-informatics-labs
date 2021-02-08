using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Entities;

namespace DALInterfaces
{
    public interface ICommentDataAccess
    {
        void Create(Comment comment);
        Comment Read(int id);
        IEnumerable<Comment> ReadAll(int taskId);
        void Update(Comment comment);
        void Delete(Comment comment);
        void Delete(int id);
    }
}
