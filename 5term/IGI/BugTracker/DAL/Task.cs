using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;


namespace Entities
{
    public class Task
    {
        public int Id { get; set; }
        public TaskStatus Status { get; set; }
        public string Description { get; set; }
        public User Reporter{ get; set; }
        public DateTime OpenDate { get; set; }
        public DateTime Deadline { get; set; }
        public int Priority { get; set; }
        public Project Project { get; set; }
        public IEnumerable<Comment> Comments { get; set; }

        public Task() { }

        public Task(int id, User usr, string descr, DateTime opendate, DateTime deadline, int priority,Project proj,IEnumerable<Comment> coms)
        {
            this.Id = id;
            this.Reporter = Reporter;
            this.Project = proj;
            this.Comments = coms;
            this.Description = descr;
            this.OpenDate = opendate;
            this.Deadline = deadline;
            this.Priority = priority;
        }
    }
}
