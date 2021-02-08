using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;


namespace Entities
{
    public class User
    {
        public int Id { get; set; }
        public UserGroup Group { get; set; }
        public string Login { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }

        public User() { }

        public User(int id, string login, string name, string email,UserGroup group,string passw)
        {
            this.Id = id;
            this.Login = login;
            this.Name = name;
            this.Email = email;
            this.Password = passw;
            Group = new UserGroup() { Id = 3 };
        }
    }
}
