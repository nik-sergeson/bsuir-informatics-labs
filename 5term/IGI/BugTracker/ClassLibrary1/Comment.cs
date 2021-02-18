using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Data.Entity;
using System.Globalization;
using System.Web.Security;

namespace Entities
{
    public class Comment
    {
        public int ID { get; set; }
        [Required]
        [Display(Name = "Your comment")]
        public string Text { get; set; }
        public virtual User User { get; set; }
        public DateTime CreationTime { get; set; }
        public virtual Task Task { get; set; }

        public Comment() { }

        public Comment(int id,string text,User UserID,DateTime creationtime,Task taskid){
            this.ID=id;
            this.Text=text;
            this.CreationTime=creationtime;
            this.User = UserID;
            this.Task = taskid;
        }
    }
}
