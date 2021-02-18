using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL;
using SqlDal;
using System.Configuration;

namespace BLL
{
    public static class TicketLogic
    {
        private static ITicketStorable readerwriter;
        static TicketLogic()
        {
            ExeConfigurationFileMap map = new ExeConfigurationFileMap();
            map.ExeConfigFilename = @"D:\isp-3\ProjectEntities\BLL.config";
            Configuration cfg = ConfigurationManager.OpenMappedExeConfiguration(map, ConfigurationUserLevel.None);
            AppSettingsSection section = (cfg.GetSection("appSettings") as AppSettingsSection);
            if (section.Settings["dataSource"].Value == "SQL")
                readerwriter = new TicketSqlReaderWriter();
            else
                readerwriter = new TicketReaderWriter();
        }

        public static void AddTicket(Ticket ticket)
        {
            readerwriter.Add(ticket);
        }

        public static void ReturnTicket(Ticket ticket){
            ticket.OwnerID = 0;
            readerwriter.Update(ticket);
        }

        public static IEnumerable<Ticket> GetOrderedByCost(int aeroplaneid)
        {
            return readerwriter.ReadAllForPlane(aeroplaneid).OrderBy(x => x.Cost);
        }

        public static void BuyTicket(Ticket ticket,Client client)
        {
            ticket.OwnerID = client.ID;
            readerwriter.Update(ticket);
        }

        public static List<Ticket> GetAvailableTickets(int aeroplaneid)
        {
            return readerwriter.ReadAllForPlane(aeroplaneid).Where(x => x.OwnerID == 0).ToList<Ticket>();
        }

        public static int TicketsPrice(IEnumerable<Ticket> tickets)
        {
            int cost = 0;
            foreach (var ticket in tickets)
                cost += ticket.Cost;
            return cost;
        }

        public static List<Ticket> GetClientTickets(int id)
        {
            return readerwriter.ReadAllForClient(id);
        }

        public static Ticket SeatIsAvailable(int aeroplaneid, int seat)
        {
            return readerwriter.ReadAllForPlane(aeroplaneid).First(x => x.Seat == seat);
        }

        public static List<Ticket> ReadAll()
        {
            return readerwriter.ReadAll();
        }

        public static void DeleteTicket(int ID)
        {
            readerwriter.Delete(ID);
        }

        public static void Update(Ticket ticket)
        {
            readerwriter.Update(ticket);
        }

        public static Ticket Read(int id)
        {
            return readerwriter.Read(id);
        }
    }
}
