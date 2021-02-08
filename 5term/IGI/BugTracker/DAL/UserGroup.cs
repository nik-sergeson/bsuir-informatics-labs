using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entities
{
    public class UserGroup
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public HashSet<string> permissions { get; set; }

        public UserGroup() { }

        public UserGroup(int id, string name, HashSet<string> perm)
        {
            this.Id = id;
            this.Name = name;
            this.permissions = perm;
        }
    }
}
