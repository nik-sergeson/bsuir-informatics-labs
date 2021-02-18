using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using IDAL;

namespace SqlDal
{
    public class AeroplaneSqlReaderWriter:IAeroplaneStorable,IStorable<Aeroplane>
    {

        public void Add(Aeroplane aeroplane)
        {
            SqlConnection connection = ConnectionToServer.Connection;

            SqlCommand command = connection.CreateCommand();
            command.CommandText = "INSERT INTO Aeroplane(id, flightid, capacity) VALUES ('" + aeroplane.ID + "', '" + aeroplane.FlightID + "', '" + aeroplane.Capacity + "')";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public Aeroplane Read(int ID)
        {
            SqlConnection connection = ConnectionToServer.Connection;

            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Aeroplane WHERE ID = '" + ID + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            reader.Read();
            Aeroplane plane= new Aeroplane(ID, reader.GetFieldValue<int>(reader.GetOrdinal("flightid")), reader.GetFieldValue<int>(reader.GetOrdinal("capacity")));
            connection.Close();
            return plane;
        }

        public void Update(Aeroplane plane)
        {
            SqlConnection connection = ConnectionToServer.Connection;

            SqlCommand command = connection.CreateCommand();
            command.CommandText = "UPDATE TOP(1) Aeroplane SET flightid = '" + plane.FlightID + "', capacity = '" + plane.Capacity + "'  WHERE ID = '" + plane.ID + "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void Delete(int ID)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "DELETE FROM Aeroplane WHERE ID = '" + ID + "'";
            SqlCommand command2 = connection.CreateCommand();
            command2.CommandText = "DELETE FROM Ticket WHERE aeroplaneid = '" + ID + "'";
            connection.Open();
            command2.ExecuteNonQuery();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public List<Aeroplane> ReadAll(int flightid)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            List<Aeroplane> la = new List<Aeroplane>();
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Aeroplane WHERE flightid = '" + flightid + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                la.Add(new Aeroplane(reader.GetFieldValue<int>(reader.GetOrdinal("id")), flightid, reader.GetFieldValue<int>(reader.GetOrdinal("capacity"))));
            }
            connection.Close();
            return la;
        }

        public List<Aeroplane> ReadAll()
        {
            SqlConnection connection = ConnectionToServer.Connection;
            List<Aeroplane> la = new List<Aeroplane>();
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Aeroplane";
            connection.Open();
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                la.Add(new Aeroplane(reader.GetFieldValue<int>(reader.GetOrdinal("id")), reader.GetFieldValue<int>(reader.GetOrdinal("flightid")), reader.GetFieldValue<int>(reader.GetOrdinal("capacity"))));
            }
            connection.Close();
            return la;
        }
    }
}
