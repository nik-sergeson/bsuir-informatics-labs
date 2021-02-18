using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Data.Entity.Infrastructure;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;

namespace EntityFramework
{
    public class EntityDAC<T> where T : Entity
    {
        public EntityDAC()
        {
            Database.SetInitializer<EntityContext<T>>(null);
            using (var context = new EntityContext<T>())
            {
                if (!context.Database.Exists())
                {
                    ((IObjectContextAdapter)context).ObjectContext.CreateDatabase();
                }
            }
        }

        public long Create(T obj)
        {
            using (var context = new EntityContext<T>())
            {
                context.Entities.Add(obj);
                context.SaveChanges();
                return context.Entities.ToList().Last().ID;
            }
        }

        public void Update(T obj)
        {
            using (var context = new EntityContext<T>())
            {
                context.Entry(obj).State = EntityState.Modified;
                context.SaveChanges();
            }
        }

        public T Read(int id)
        {
            using (var context = new EntityContext<T>())
            {
                return context.Entities.Find(id);
            }
        }

        public void Delete(int id)
        {
            using (var context = new EntityContext<T>())
            {
                context.Entities.Remove(context.Entities.Find(id));
                context.SaveChanges();
            }
        }

        public IEnumerable<T> ReadAll()
        {
            using (var context = new EntityContext<T>())
            {
                return context.Entities.ToList();
            }
        }
    }

    public class EntityContext<T> : DbContext where T : Entity
    {
        public EntityContext()
            : base("EFConnection")
        {
        }

        public DbSet<T> Entities { get; set; }
    }
}