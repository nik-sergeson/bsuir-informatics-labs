using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Entities
{
    public class Comment
    {
        public int Id { get; set; }
        public string Text { get; set; }
        public User Author { get; set; }
        public DateTime CreationTime { get; set; }
        public Task Task { get; set; }

        public Comment() { }

        public Comment(int id,string text,User author,DateTime creationtime,Task task){
            this.Id=id;
            this.Text=text;
            this.CreationTime=creationtime;
            this.Author = author;
            this.Task = task;
        }
    }
}
