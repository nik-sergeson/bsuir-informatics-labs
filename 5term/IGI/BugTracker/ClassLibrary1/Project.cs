using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.ComponentModel.DataAnnotations;

namespace Entities
{
    public class Project
    {
        public int ID { get; set; }
        [Required]
        [Display(Name = "Project name")]
        public string Name { get; set; }
        [Required]
        [Display(Name = "Description")]
        public string Description { get; set; }
        public virtual User User { get; set; }

        public Project() { }

        public Project(int id,string name,string descr,User creator){
            this.ID=id;
            this.Name=name;
            this.Description=descr;
            this.User=creator;
        }
    }
}
