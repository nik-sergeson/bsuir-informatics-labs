﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entities
{
    public class UserGroup
    {
        public int ID { get; set; }
        public string Name { get; set; }

        public UserGroup() { }

        public UserGroup(int id, string name)
        {
            this.ID = id;
            this.Name = name;
        }
    }
}
