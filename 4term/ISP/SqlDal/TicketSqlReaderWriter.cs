using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using IDAL;

namespace SqlDal
{
    public class TicketSqlReaderWriter:ITicketStorable,IStorable<Ticket>
    {
        public void Add(Ticket ticket)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "INSERT INTO Ticket(aeroplaneid, ownerid, flightid, cost, id, seat) VALUES ('" + ticket.AeroplaneID + "', '" + ticket.OwnerID + "', '" + ticket.FlightID + "', '" + ticket.Cost + "', '" + ticket.ID + "', '" +ticket.Seat +"')";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public Ticket Read(int id)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM TIcket WHERE ID = '" + id + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            reader.Read();
            Ticket ticket = new Ticket() { ID = id, AeroplaneID = reader.GetFieldValue<int>(reader.GetOrdinal("aeroplineid")), OwnerID = reader.GetFieldValue<int>(reader.GetOrdinal("ownerid")), FlightID = reader.GetFieldValue<int>(reader.GetOrdinal("flightid")), Cost = reader.GetFieldValue<int>(reader.GetOrdinal("cost")), Seat = reader.GetFieldValue<int>(reader.GetOrdinal("seat")) };
            connection.Close();
            return ticket;
        }

        public void Update(Ticket ticket)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "UPDATE TOP(1) Ticket SET aeroplaneid = '" + ticket.AeroplaneID + "', ownerid = '" + ticket.OwnerID + "', flightid = '" + ticket.FlightID + "', cost = '" + ticket.Cost + "', seat = '" +ticket.Seat +"'  WHERE ID = '" + ticket.ID + "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void Delete(int id)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "DELETE FROM Ticket WHERE ID = '" + id + "'";
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();
        }

        public List<Ticket> ReadAllForPlane(int planeid)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            List<Ticket> lt=new List<Ticket>();
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Ticket WHERE aeroplaneid = '" + planeid + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            while(reader.Read()){
                lt.Add( new Ticket() {ID=reader.GetFieldValue<int>(reader.GetOrdinal("id")), AeroplaneID = reader.GetFieldValue<int>(reader.GetOrdinal("aeroplineid")), OwnerID = reader.GetFieldValue<int>(reader.GetOrdinal("ownerid")), FlightID = reader.GetFieldValue<int>(reader.GetOrdinal("flightid")), Cost = reader.GetFieldValue<int>(reader.GetOrdinal("cost")), Seat = reader.GetFieldValue<int>(reader.GetOrdinal("seat"))});
            }
            connection.Close();
            return lt;
        }

        public List<Ticket> ReadAllForClient(int ownerid)
        {
            SqlConnection connection = ConnectionToServer.Connection;
            List<Ticket> lt=new List<Ticket>();
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Ticket WHERE ownerid = '" + ownerid + "'";
            connection.Open();
            var reader = command.ExecuteReader();
            while(reader.Read()){
                lt.Add( new Ticket() {ID=reader.GetFieldValue<int>(reader.GetOrdinal("id")), AeroplaneID = reader.GetFieldValue<int>(reader.GetOrdinal("aeroplineid")), OwnerID = reader.GetFieldValue<int>(reader.GetOrdinal("ownerid")), FlightID = reader.GetFieldValue<int>(reader.GetOrdinal("flightid")), Cost = reader.GetFieldValue<int>(reader.GetOrdinal("cost")), Seat = reader.GetFieldValue<int>(reader.GetOrdinal("seat"))});
            }
            connection.Close();
            return lt;
        }

        public List<Ticket> ReadAll()
        {
            SqlConnection connection = ConnectionToServer.Connection;
            List<Ticket> lt = new List<Ticket>();
            SqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM Ticket";
            connection.Open();
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                lt.Add(new Ticket(reader.GetFieldValue<int>(reader.GetOrdinal("aeroplaneid")),reader.GetFieldValue<int>(reader.GetOrdinal("ownerid")),reader.GetFieldValue<int>(reader.GetOrdinal("flightid")),reader.GetFieldValue<int>(reader.GetOrdinal("cost")),reader.GetFieldValue<int>(reader.GetOrdinal("id")),reader.GetFieldValue<int>(reader.GetOrdinal("seat"))));
            }
            connection.Close();
            return lt;
        }

    }
}
