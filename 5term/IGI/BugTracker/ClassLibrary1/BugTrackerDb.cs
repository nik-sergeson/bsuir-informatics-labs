using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entities
{
    public class BugTrackerDb: DbContext
    {
        public DbSet<Comment> Comments { get; set; }
        public DbSet<Project> Projects { get; set; }
        public DbSet<Task> Tasks { get; set; }
        public DbSet<TaskStatus> TaskStasuses { get; set; }
        public DbSet<UserGroup> Groups { get; set; }
        public DbSet<User> Users { get; set; }
    }
}
