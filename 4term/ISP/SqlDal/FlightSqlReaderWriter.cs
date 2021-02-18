using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using IDAL;

namespace SqlDal
{
    public class FlightSqlReaderWriter:IFlightStorable,IStorable<Flight>
    {
        public void Add(Flight flight)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "INSERT INTO Flight(ID, cost, departingpointid, arrivalpointid) VALUES ('" + flight.ID + "', '" + flight.Cost + "', " + flight.DepartingPoint + "', '" + flight.ArrivalPoint+ "')";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public Flight Read(int id)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Flight WHERE ID = '" + id + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            reader.Read();
            Flight flight = new Flight(id, reader.GetFieldValue<int>(reader.GetOrdinal("cost")), reader.GetFieldValue<int>(reader.GetOrdinal("departingpointid")), reader.GetFieldValue<int>(reader.GetOrdinal("arrivalpointid")));
            connection.Close();
            return flight;
        }

        public void Update(Flight flight)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "UPDATE TOP(1) Flight SET cost = '" + flight.Cost + "', departingpointid = '" + flight.DepartingPoint + "', arrivalpointid = '" +flight.ArrivalPoint +"'  WHERE ID = '" + flight.ID + "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void Delete(int ID)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "DELETE FROM Flight WHERE ID = '" + ID + "'";
            SqlCommand command2 = connection.CreateCommand();
            command2.CommandText = "DELETE FROM Aeroplane WHERE flightid = '" + ID + "'";
            SqlCommand command3 = connection.CreateCommand();
            command3.CommandText = "DELETE FROM Ticket WHERE flightid = '" + ID + "'";
            connection.Open();
            command3.ExecuteNonQuery();
            command2.ExecuteNonQuery();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public List<Flight> ReadAll()
        {
            SqlConnection connection = ConnectionToServer.Connection;
            List<Flight> lf = new List<Flight>();
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Flight";
            connection.Open();
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                lf.Add(new Flight(reader.GetFieldValue<int>(reader.GetOrdinal("id")), reader.GetFieldValue<int>(reader.GetOrdinal("cost")), reader.GetFieldValue<int>(reader.GetOrdinal("departingpointid")), reader.GetFieldValue<int>(reader.GetOrdinal("arrivalpointid"))));
            }
            connection.Close();
            return lf;
        }
    }
}
