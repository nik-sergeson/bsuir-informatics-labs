using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Security.Cryptography;
using System.Threading.Tasks;
using Entities;
using System.Security;
using Entities;
using System.Data.Entity.Infrastructure;
using System.Data.Entity;
using System.Security;

namespace BLL
{
    public static class UserLogic
    {
        public static List<User> ReadAll()
        {
            List<User> l=new List<User>();
            using (BugTrackerDb db = new BugTrackerDb())
            {
                l = (from u in db.Users.Include("UserGroup") select u).ToList();
            }
            return l;
        }

        public static User Read(string login,User doer)
        {
            User t = new User();
            using (BugTrackerDb db = new BugTrackerDb())
            {
                t = (from u in db.Users.Include("UserGroup") where u.Login == login select u).FirstOrDefault();
            }
            return t;
        }

        public static User Read(int ID)
        {
            User t=new User();
            using (BugTrackerDb db = new BugTrackerDb())
            {
                t = (from u in db.Users.Include("UserGroup") where u.ID == ID select u).FirstOrDefault();
            }
            return t;
        }

        public static void Update(User user, User doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                var oldVersion = Read(user.Login, doer);
                oldVersion.Email = user.Email;
                oldVersion.UserGroup = db.Groups.First(x => x.ID == user.UserGroup.ID);
                oldVersion.Login = user.Login;
                oldVersion.Name = user.Name;
                oldVersion.Password = user.Password;
                db.Users.Attach(oldVersion);
                ((IObjectContextAdapter)db).ObjectContext.ObjectStateManager.ChangeObjectState(oldVersion, EntityState.Modified);
                db.SaveChanges();
            }
        }

        public static void Delete(int  user, User doer)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                db.Users.Remove(db.Users.First(x=>x.ID==user));
            }
        }

        public static void Create(User user, string password)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                int count = db.Users.ToList().Count;
                user.ID = (count + 1);
                user.UserGroup = db.Groups.First(x=>x.ID==3);
                db.Users.Add(user);
                db.SaveChanges();
            }
        }
        
        public static UserGroup ReadGr(int id)
        {
            UserGroup ug = new UserGroup();
            using (BugTrackerDb db = new BugTrackerDb())
            {
                ug = db.Groups.First(x => x.ID == id);
            }
            return ug;
        }

        public static void ChangeGroup(int userid, int groupid)
        {
            using (BugTrackerDb db = new BugTrackerDb())
            {
                db.Users.First(x => x.ID == userid).UserGroup = db.Groups.First(y => y.ID == groupid);
            }
        }
        
    }
}
