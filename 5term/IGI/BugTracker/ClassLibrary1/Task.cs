using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;


namespace Entities
{
    public class Task
    {
        public int ID { get; set; }
        public string Description { get; set; }
        public virtual User User{ get; set; }
        public DateTime OpenDate { get; set; }
        public DateTime Deadline { get; set; }
        public int Priority { get; set; }
        public virtual Project Project { get; set; }
        public virtual TaskStatus TaskStatus { get; set; }

        public Task() { }

        public Task(int id, User usr, string descr, DateTime opendate, DateTime deadline, int priority,Project proj,TaskStatus stat)
            
        {
            this.TaskStatus = stat;
            this.ID = id;
            this.User = usr;
            this.Project = proj;
            this.Description = descr;
            this.OpenDate = opendate;
            this.Deadline = deadline;
            this.Priority = priority;
        }
    }
}
