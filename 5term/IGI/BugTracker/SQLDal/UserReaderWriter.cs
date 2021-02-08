using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
using System.Data.SqlClient;
using Entities;
using DALInterfaces;


namespace SQLDal
{
    public class UserReaderWriter : IUserDataAccess
    {
        private string connectionString;

        public UserReaderWriter(string connection)
        {
            this.connectionString = connection;
        }

        public void Create(User usr, string passw)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "INSERT INTO Users(id, groupid, login, name, email,password) VALUES ('" + usr.Id + "', '" + usr.Group.Id + "', '" + usr.Login + "', '" + usr.Name + "', '" + usr.Email + "', convert(binary(128),'" + passw + "'))";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public User Read(int id)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                User usr;
                command.CommandText = "SELECT * FROM Users WHERE id = '" + id + "'";
                connection.Open();
                var reader = command.ExecuteReader();
                if (reader.Read())
                    usr = new User(id, reader.GetFieldValue<string>(reader.GetOrdinal("login")), reader.GetFieldValue<string>(reader.GetOrdinal("name")), reader.GetFieldValue<string>(reader.GetOrdinal("email")),GetGroup(id));
                else
                    usr = null;
                connection.Close();
                return usr;
            }
        }

        public User Read(string login)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                User usr;
                command.CommandText = "SELECT * FROM Users WHERE login = '" + login + "'";
                connection.Open();
                var reader = command.ExecuteReader();
                if (reader.Read())
                    usr = new User(reader.GetFieldValue<int>(reader.GetOrdinal("id")), login, reader.GetFieldValue<string>(reader.GetOrdinal("name")), reader.GetFieldValue<string>(reader.GetOrdinal("email")),GetGroup(reader.GetFieldValue<int>(reader.GetOrdinal("id"))));
                else
                    usr = null;
                connection.Close();
                return usr;
            }
        }

        public void Update(User usr)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "UPDATE Users SET name = '" + usr.Name + "', login = '" + usr.Login + "', email = '" + usr.Email + "'  WHERE id = '" + usr.Id + "'";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public void Delete(int ID)
        {
            List<Project> projs=new List<Project>(SqlFactory.GetFactory().GetProjectDataAccess().ReadAuthorProject(ID));
            foreach (var proj in projs)
                    SqlFactory.GetFactory().GetProjectDataAccess().Delete(proj);
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "DELETE FROM Users WHERE id = '" + ID + "'";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public void Delete(User usr)
        {
            Delete(usr.Id);
        }

        public IEnumerable<User> ReadAll()
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                List<User> usr = new List<User>();
                command.CommandText = "SELECT * FROM Users";
                connection.Open();
                var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    usr.Add(new User(reader.GetFieldValue<int>(reader.GetOrdinal("id")), reader.GetFieldValue<string>(reader.GetOrdinal("login")), reader.GetFieldValue<string>(reader.GetOrdinal("name")), reader.GetFieldValue<string>(reader.GetOrdinal("email")),GetGroup(reader.GetFieldValue<int>(reader.GetOrdinal("id")))));
                }
                connection.Close();
                return usr;
            }

        }

        public HashSet<string> GetPermissions(User user)
        {
            return GetGroupPermissions(user.Group.Id);
        }

        public HashSet<string> GetPermissions(int userId)
        {
            using (var connection = new SqlConnection(connectionString))
            {
                var cmd = connection.CreateCommand();
                cmd.CommandText = "SELECT * FROM users WHERE id = '"+userId+"'";
                connection.Open();
                var reader = cmd.ExecuteReader();
                return GetGroupPermissions(reader.GetFieldValue<int>(reader.GetOrdinal("groupid")));
            }
        }

        private UserGroup GetGroup(int userid)
        {
            using (var connection = new SqlConnection(connectionString))
            {
                var cmd = connection.CreateCommand();
                cmd.CommandText = "SELECT * FROM users WHERE id = '" + userid + "'";
                connection.Open();
                var reader = cmd.ExecuteReader();
                return new UserGroup(reader.GetFieldValue<int>(reader.GetOrdinal("groupid")), reader.GetFieldValue<string>(reader.GetOrdinal("name")),GetGroupPermissions(reader.GetFieldValue<int>(reader.GetOrdinal("groupid"))));
            }
        }

        private HashSet<string> GetGroupPermissions(int groupId)
        {
            HashSet<string> permissions = new HashSet<string>();
            using (var connection = new SqlConnection(connectionString))
            {

                var cmd = connection.CreateCommand();
                cmd.CommandText = "SELECT * FROM UserGroup WHERE id = '" + groupId + "'";
                connection.Open();
                var reader = cmd.ExecuteReader();
                if (reader.GetFieldValue<int>(reader.GetOrdinal("allow_create")) == 1)
                    permissions.Add("allow_create");
                if (reader.GetFieldValue<int>(reader.GetOrdinal("allow_moderate")) == 1)
                    permissions.Add("allow_moderate");
            }
            return permissions;
        }

        public bool CheckLoginInformation(string login, byte[] passwordHash)
        {
            byte[] hash;
            using (var connection = new SqlConnection(connectionString))
            {
                 var cmd = connection.CreateCommand();
                 cmd.CommandText = "SELECT password FROM users WHERE login ='" +login + "'";
                connection.Open();
                using (var reader = cmd.ExecuteReader())
                {
                    if (reader.Read())
                    {
                        hash = (byte[])reader.GetValue(0);
                    }
                    else
                    {
                        return false;
                    }
                }
            }
            if (hash.Length != passwordHash.Length) return false;
            for (int i = 0; i < hash.Length; ++i)
            {
                if (hash[i] != passwordHash[i]) return false;
            }
            return true;
        }
    }
}
