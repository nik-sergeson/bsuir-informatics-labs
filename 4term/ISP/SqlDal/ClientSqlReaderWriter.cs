using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using IDAL;

namespace SqlDal
{
    public class ClientSqlReaderWriter:IClientStorable,IStorable<Client>
    {
        public void Add(Client client)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "INSERT INTO Client(ID, name) VALUES ('" + client.ID + "', '" +client.Name+ "')";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public Client Read(int id)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Client WHERE ID = '" + id + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            reader.Read();
            Client client = new Client(reader.GetFieldValue<string>(reader.GetOrdinal("name")),id);
            connection.Close();
            return client;
        }

        public void Update(Client client)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "UPDATE TOP(1) Client SET name = '" + client.Name+ "'  WHERE ID = '" + client.ID + "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void Delete(int ID)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "DELETE FROM Client WHERE ID = '" + ID + "'";
            SqlCommand command2 = connection.CreateCommand();
            command2.CommandText = "DELETE FROM baggage WHERE ownerid = '" + ID + "'";
            SqlCommand command3 = connection.CreateCommand();
            command3.CommandText = "DELETE FROM Passport WHERE ownerid = '" + ID + "'";
            SqlCommand command4 = connection.CreateCommand();
            command4.CommandText = "DELETE FROM Ticket WHERE ownerid = '" + ID + "'";
            connection.Open();
            command2.ExecuteNonQuery();
            command3.ExecuteNonQuery();
            command4.ExecuteNonQuery();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public List<Client> ReadAll()
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            List<Client> client = new List<Client>();
            command.CommandText = "SELECT * FROM Client";
            connection.Open();
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                client.Add(new Client(reader.GetFieldValue<string>(reader.GetOrdinal("name")),reader.GetFieldValue<int>(reader.GetOrdinal("id"))));
            }
            connection.Close();
            return client;
        }
    }
}
