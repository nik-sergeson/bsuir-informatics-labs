using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;


namespace Entities
{
    public class User
    {
        public int ID { get; set; }
        public virtual UserGroup UserGroup { get; set; }
        public string Login { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }

        public User() { }

        public User(int id, string login, string name, string email)
        {
            this.ID = id;
            this.Login = login;
            this.Name = name;
            this.Email = email;
        }
    }
}
