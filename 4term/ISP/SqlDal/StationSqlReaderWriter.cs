using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using IDAL;

namespace SqlDal
{
    public class StationSqlReaderWriter:IStationStorable,IStorable<Station>
    {
        public void Add(Station station)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "INSERT INTO Station(ID, country, name, arrivaltime, departingtime) VALUES ('" + station.ID + "', '" + station.Country + "', '" + station.Name + "', " + station.ArrivalTime.Year + "-" + station.ArrivalTime.Month + "-" + station.ArrivalTime.Day + "', '" + station.DepartingTime.Year + "-" + station.DepartingTime.Month + "-" + station.DepartingTime.Day + "')";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public Station Read(int id)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Station WHERE ID = '" + id + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            reader.Read();
            Station stat = new Station(reader.GetFieldValue<DateTime>(reader.GetOrdinal("departingtime")), reader.GetFieldValue<DateTime>(reader.GetOrdinal("arrivaltime")), reader.GetFieldValue<string>(reader.GetOrdinal("name")), reader.GetFieldValue<string>(reader.GetOrdinal("country")), reader.GetFieldValue<int>(reader.GetOrdinal("id")));
            connection.Close();
            return stat;
        }

        public void Update(Station stat)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "UPDATE TOP(1) Station SET departingtime = '" + stat.DepartingTime.Year + "-" + stat.DepartingTime.Month + "-" + stat.DepartingTime.Day + "', arrivaltime = '" + stat.ArrivalTime.Year + "-" + stat.ArrivalTime.Month + "-" + stat.ArrivalTime.Day + "', name = '" + stat.Name + "', country = '" + stat.Country + "'  WHERE ID = '" + stat.ID + "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void Delete(int ID)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            List<int> flightids = new List<int>();
            SqlCommand command = connection.CreateCommand();
            SqlCommand command1 = connection.CreateCommand();
            command.CommandText = "DELETE FROM Station WHERE ID = '" + ID + "'";
            connection.Open();
            command1.CommandText = "SELECT * FROM Flight WHERE arrivalpointid = '" + ID + "'";
            var reader = command1.ExecuteReader();
            while(reader.Read())
                flightids.Add(reader.GetFieldValue<int>(reader.GetOrdinal("id")));
            command1.CommandText = "SELECT * FROM Flight WHERE departingpoint = '" + ID + "'";
            reader = command1.ExecuteReader();
            while (reader.Read())
                flightids.Add(reader.GetFieldValue<int>(reader.GetOrdinal("id")));
            foreach (var id in flightids)
            {
                SqlCommand command4 = connection.CreateCommand();
                command.CommandText = "DELETE FROM Ticket WHERE flightid = '" + id + "'";
                command4.ExecuteNonQuery();
                command.CommandText = "DELETE FROM Aeroplane WHERE flightid = '" + id + "'";
                command4.ExecuteNonQuery();
                command.CommandText = "DELETE FROM Flight WHERE ID = '" + id + "'";
                command4.ExecuteNonQuery();
            }
            command.ExecuteNonQuery();
            connection.Close();
        }

        public List<Station> ReadAll()
        {
            SqlConnection connection = ConnectionToServer.Connection;
            List<Station> ls = new List<Station>();
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Station" ;
            connection.Open();
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                ls.Add(new Station(reader.GetFieldValue<DateTime>(reader.GetOrdinal("departingtime")), reader.GetFieldValue<DateTime>(reader.GetOrdinal("arrivaltime")), reader.GetFieldValue<string>(reader.GetOrdinal("name")), reader.GetFieldValue<string>(reader.GetOrdinal("country")), reader.GetFieldValue<int>(reader.GetOrdinal("id"))));
            }
            connection.Close();
            return ls;
        }
    }
}
