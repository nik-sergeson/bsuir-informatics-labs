using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Entities;
using System.Data.Entity;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            //Database.SetInitializer<BugTrackerDb>(null);
            UserGroup gr1 = new UserGroup(1, "Administrator");
            UserGroup gr2 = new UserGroup(2, "Moderator");
            UserGroup gr3 = new UserGroup(3, "User");
            TaskStatus t1 = new TaskStatus() { ID = 1, Name = "Opened" };
            TaskStatus ts = new TaskStatus() { ID = 2, Name = "Resolved" };
            BugTrackerDb db = new BugTrackerDb();
            db.Groups.Add(gr1);
            db.Groups.Add(gr2);
            db.Groups.Add(gr3);
            db.TaskStasuses.Add(t1);
            db.TaskStasuses.Add(ts);
            db.SaveChanges();
            Console.Read();
        }
    }
}
