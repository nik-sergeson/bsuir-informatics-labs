using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Entities;
using System.Data.Entity.Infrastructure;
using System.Data.Entity;
using System.Security;

namespace BLL
{
    public static class ProjectLogic
    {
        public static void Create(Project project, int doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                if (db.Projects.ToList().Count != 0)
                    project.ID = db.Projects.Max(x => x.ID) + 1;
                else
                    project.ID = 1;
                project.User = db.Users.First(x => x.ID == doer);
                db.Projects.Add(project);
                db.SaveChanges();
            }
        }


        public static void Update(Project project, int doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                var oldVersion = db.Projects.First(x=>x.ID==project.ID);
                oldVersion.User = db.Users.First(x => x.ID == project.User.ID);
                oldVersion.Description = project.Description;
                oldVersion.Name = project.Name;
                db.Projects.Attach(oldVersion);
                ((IObjectContextAdapter)db).ObjectContext.ObjectStateManager.ChangeObjectState(oldVersion, EntityState.Modified);
                db.SaveChanges();
            }
        }


        public static void Delete(Project project, User doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                db.Projects.Remove(db.Projects.First(x=>x.ID==project.ID));
                db.SaveChanges();
            }
        }

        public static void Delete(int projectId, User doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                db.Projects.Remove(db.Projects.First(x => x.ID == projectId));
                db.SaveChanges();
            }
        }

        public static Project Read(int projectId, User doer)
        {
            Project proj;
            using (BugTrackerDb db = new BugTrackerDb())
            {
                proj = (from u in db.Projects.Include("User") where u.ID == projectId select u).FirstOrDefault();
            }
            return proj;
        }

        public static List<Project> ReadAll(User doer)
        {
            List<Project> pl=new List<Project>();
            using (BugTrackerDb db = new BugTrackerDb())
            {
                pl=(from u in db.Projects.Include("User") select u).ToList();
            }
            return pl;
        }
        
    }
}
