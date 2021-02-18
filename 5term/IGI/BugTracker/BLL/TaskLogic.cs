using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Entities;
using System.Security;
using Entities;
using System.Data.Entity.Infrastructure;
using System.Data.Entity;
using System.Security;

namespace BLL
{
    public static class TaskLogic
    {
        public static void Create(Task task, int doer,int project)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                if (db.Tasks.ToList().Count != 0)
                    task.ID = db.Tasks.Max(x => x.ID) + 1;
                else
                    task.ID = 1;
                task.OpenDate = DateTime.Now;
                task.Deadline = task.OpenDate + TimeSpan.FromDays(30);
                task.TaskStatus = db.TaskStasuses.First(x => x.Name == "Opened");
                task.User = db.Users.First(x => x.ID == doer);
                task.Project = db.Projects.First(x => x.ID == project);
                db.Tasks.Add(task);
                db.SaveChanges();
            }
        }

        public static void Update(Task task, User doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                var oldVersion = db.Tasks.First(x => x.ID == task.ID);
                /* if (oldVersion == null)
                 {
                     string message = "No task id=" + task.Id.ToString() + " to update. Doer id=" +
                         doer.Id.ToString();
                     throw new SecurityException(message);
                 }

                 if (oldVersion.Reporter != task.Reporter)
                 {
                     string message = "Error while updating task id=" + task.Id.ToString() + ". Cannot" +
                         " change opener. Doer id=" + doer.Id.ToString();
                     throw new SecurityException(message);
                 }

                 if (doer.Group.Id == 1)
                 {*/
                //oldVersion.Deadline = task.Deadline;
                oldVersion.Description = task.Description;
                //oldVersion.OpenDate = task.OpenDate;
                oldVersion.Priority = task.Priority;
                oldVersion.Project = db.Projects.First(x => x.ID == task.Project.ID);
                oldVersion.User = db.Users.First(x=>x.ID==task.User.ID);
                oldVersion.TaskStatus = db.TaskStasuses.First(x=>x.ID==task.TaskStatus.ID);
                db.Tasks.Attach(oldVersion);
                ((IObjectContextAdapter)db).ObjectContext.ObjectStateManager.ChangeObjectState(oldVersion, EntityState.Modified);
                db.SaveChanges();
            }

        }

        public static void Delete(Task task,User doer)
        {
            Delete(task.ID, doer);
        }

        public static void Delete(int taskId, User doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                db.Tasks.Remove(db.Tasks.First(x => x.ID == taskId));
                db.SaveChanges();
            }
        }

        public static Task Read(int taskId, User doer)
        {
            Task l;
            using (BugTrackerDb db = new BugTrackerDb())
            {
                l = (from u in db.Tasks.Include("User").Include("Project").Include("TaskStatus") where u.ID == taskId select u).FirstOrDefault();
            }
            return l;
        }

        public static IEnumerable<Task> ReadAll(Project project, User doer)
        {
            return ReadAll(project.ID, doer);
        }

        public static List<Task> ReadAll()
        {
            List<Task> l = new List<Task>();
            using (BugTrackerDb db = new BugTrackerDb())
            {
                l = (from u in db.Tasks.Include("User").Include("Project").Include("TaskStatus") select u).ToList();
            }
            return l;
        }

        public static List<Task> ReadAll(int projectId,User doer)
        {
            List<Task> l=new List<Task>();
            using (BugTrackerDb db = new BugTrackerDb())
            {
                l = (from u in db.Tasks.Include("User").Include("Project").Include("TaskStatus") where u.Project.ID == projectId select u).ToList();
            }
            return l;
        }
    }
}
