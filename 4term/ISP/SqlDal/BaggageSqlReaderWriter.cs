using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using IDAL;

namespace SqlDal
{
    public class BaggageSqlReaderWriter:IStorable<Baggage>
    {
        public void Add(Baggage bag)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "INSERT INTO baggage(ownerid, weight) VALUES ('" + bag.ID + "', '" + bag.Weight + "')";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public Baggage Read(int ownerid)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM baggage WHERE ownerid = '" + ownerid + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            reader.Read();
            Baggage bags=new Baggage(ownerid, reader.GetFieldValue<int>(reader.GetOrdinal("Weight")));
            connection.Close();
            return bags;
        }

        public void Update(Baggage bag)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "UPDATE TOP(1) baggage SET weight = '" + bag.Weight+ "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void Delete(int ID)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "DELETE FROM baggage WHERE ID = '" + ID + "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public List<Baggage> ReadAll()
        {
            List<Baggage> bags = new List<Baggage>();
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM baggage";
            connection.Open();
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                bags.Add(new Baggage(reader.GetFieldValue<int>(reader.GetOrdinal("ownerid")), reader.GetFieldValue<int>(reader.GetOrdinal("Weight"))));
            }
            connection.Close();
            return bags;
        }
    }
}
