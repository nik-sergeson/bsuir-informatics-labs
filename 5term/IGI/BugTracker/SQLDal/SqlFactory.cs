using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DALInterfaces;

namespace SQLDal
{
    public class SqlFactory:DataAccessFactory
    {
        private string connectionString;

        public SqlFactory(string config) : base(config)
        {
            connectionString = config;
        }

        public override ITaskDataAccess GetTaskDataAccess()
        {
            return new TaskReaderWriter(connectionString);
        }

        public override IUserDataAccess GetUserDataAccess()
        {
            return new UserReaderWriter(connectionString);
        }

        public override IProjectDataAccess GetProjectDataAccess()
        {
            return new ProjectReaderWriter(connectionString);
        }

        public override ICommentDataAccess GetCommentDataAccess()
        {
            return new CommentReaderWriter(connectionString);
        }
    }
}
