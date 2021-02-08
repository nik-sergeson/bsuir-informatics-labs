using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Entities
{
    public class Project
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public User Creator { get; set; }
        public IEnumerable<Task> Tasks { get; set; }

        public Project() { }

        public Project(int id,string name,string descr,User creator,IEnumerable<Task> task){
            this.Id=id;
            this.Name=name;
            this.Description=descr;
            this.Creator=creator;
            this.Tasks = task;
        }
    }
}
