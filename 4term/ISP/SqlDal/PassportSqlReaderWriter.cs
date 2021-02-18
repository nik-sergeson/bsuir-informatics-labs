using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using IDAL;

namespace SqlDal
{
    public class PassportSqlReaderWriter:IStorable<Passport>
    {
        public void Add(Passport pass)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "INSERT INTO Passport(ownerid, address, photo, name, secondname) VALUES ('" + pass.ID + "', '" + pass.Address + "', " + pass.Photo + "', " + pass.Name + "', " + pass.SecondName + "')";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public Passport Read(int id)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Passport WHERE ID = '" + id + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            reader.Read();
            Passport pass = new Passport(id, reader.GetFieldValue<string>(reader.GetOrdinal("address")), reader.GetFieldValue<string>(reader.GetOrdinal("photo")), reader.GetFieldValue<string>(reader.GetOrdinal("name")),reader.GetFieldValue<string>(reader.GetOrdinal("secondname")));
            connection.Close();
            return pass;
        }

        public void Update(Passport pass)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "UPDATE TOP(1) Passport SET address = '" + pass.Address + "', photo = '" + pass.Photo + "', name= '" + pass.Name + "', secondname = '" +pass.SecondName +"'  WHERE ID = '" + pass.ID + "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void Delete(int ID)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "DELETE FROM Passport WHERE ID = '" + ID + "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public List<Passport> ReadAll()
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            List<Passport> pass = new List<Passport>();
            command.CommandText = "SELECT * FROM Passport";
            connection.Open();
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                pass.Add(new Passport(reader.GetFieldValue<int>(reader.GetOrdinal("id")), reader.GetFieldValue<string>(reader.GetOrdinal("address")), reader.GetFieldValue<string>(reader.GetOrdinal("photo")), reader.GetFieldValue<string>(reader.GetOrdinal("name")), reader.GetFieldValue<string>(reader.GetOrdinal("secondname"))));
            }
            connection.Close();
            return pass;
        }
    }
}
