using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.Entity;
using System.Data;
using System.Data.Entity.Infrastructure;
using Entities;
using System.Security;

namespace BLL
{
    public static class CommentLogic
    {
        public static void Create(Comment comment, int doer,int task)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                if (db.Comments.ToList().Count != 0)
                    comment.ID = db.Comments.Max(x => x.ID) + 1;
                else
                    comment.ID = 1;
                comment.User = db.Users.First(x => x.ID == doer);
                comment.Task = db.Tasks.First(x => x.ID == task);
                comment.CreationTime = DateTime.Now;
                db.Comments.Add(comment);
                db.SaveChanges();
            }
        }

        public static void Delete(Comment comment, User doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                db.Comments.Remove(db.Comments.First(x=>x.ID==comment.ID));
                db.SaveChanges();
            }
        }

        public static void Delete(int commentId,User doer)
        {
            Comment comment;
            using (BugTrackerDb db = new BugTrackerDb())
            {
                if (db.Comments.ToList().Count > 0)
                    comment = db.Comments.First(x => x.ID == commentId);
                else
                    return;
            }
            Delete(comment, doer);
        }

        public static Comment Read(int commentId, User doer)
        {
            Comment com;
            using (BugTrackerDb db = new BugTrackerDb())
            {
                com = (from u in db.Comments.Include("Task").Include("User") where u.ID == commentId select u).FirstOrDefault();
            }            
            return com;
        }

        public static List<Comment> ReadAll(Entities.Task task, User doer)
        {
            return ReadAll(task.ID, doer);
        }

        public static List<Comment> ReadAll(int taskId, User doer)
        {
            List<Comment> coms=new List<Comment>();
            using (BugTrackerDb db = new BugTrackerDb())
            {
                coms = (from u in db.Comments.Include("User").Include("Task") where u.Task.ID == taskId select u).ToList();
            }
            return coms;
        }

        public static void Update(Comment project, int doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                var oldVersion = db.Comments.First(x => x.ID == project.ID);
                oldVersion.User = db.Users.First(x => x.ID == project.User.ID);
               // oldVersion.CreationTime = project.CreationTime;
                oldVersion.Text = project.Text;
                oldVersion.Task = db.Tasks.First(x => x.ID == project.Task.ID);
                db.Comments.Attach(oldVersion);
                ((IObjectContextAdapter)db).ObjectContext.ObjectStateManager.ChangeObjectState(oldVersion, EntityState.Modified);
                db.SaveChanges();
            }
        }
    }
}
