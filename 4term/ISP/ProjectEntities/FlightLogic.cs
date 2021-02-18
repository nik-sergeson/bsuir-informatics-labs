using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL;
using SqlDal;
using System.Configuration;
using IDAL;

namespace BLL
{
    public static class FlightLogic
    {
        private static IFlightStorable readerwriter;
        static FlightLogic()
        {
            ExeConfigurationFileMap map = new ExeConfigurationFileMap();
            map.ExeConfigFilename = @"D:\isp-3\ProjectEntities\BLL.config";
            Configuration cfg = ConfigurationManager.OpenMappedExeConfiguration(map, ConfigurationUserLevel.None);
            AppSettingsSection section = (cfg.GetSection("appSettings") as AppSettingsSection);
            if (section.Settings["dataSource"].Value == "SQL")
                readerwriter = new FlightSqlReaderWriter();
            else
                readerwriter = new FlightReaderWriter();
        }

        public static void AddFlight(Flight flight)
        {
            readerwriter.Add(flight);
        }

        public static void DeleteFlight(int ID)
        {
            readerwriter.Delete(ID);
        }

        public static void UpdateFlight(Flight flight)
        {
            readerwriter.Update(flight);
        }

        public static void UpdateFlight(Station departingstation, Station arrivalstation, Flight flight)
        {
            flight.DepartingPoint = departingstation.ID;
            flight.ArrivalPoint = arrivalstation.ID;
            readerwriter.Update(flight);
        }

        public static TimeSpan FlyingTime(Flight flight)
        {
            return StationLogic.ReadAll().First(x => x.ID == flight.ArrivalPoint).ArrivalTime - StationLogic.ReadAll().First(x => x.ID == flight.DepartingPoint).DepartingTime;
        }

        public static List<Flight> ReadAll()
        {
            return readerwriter.ReadAll();
        }

        public static Flight Read(int id)
        {
            return readerwriter.Read(id);
        }

        public static List<Flight> FindByArrivalPoint(string arrivalpoint)
        {
            List<Station> arrival = StationLogic.FindByName(arrivalpoint);
            List<Flight> flights = new List<Flight>(), allflights = readerwriter.ReadAll();
            foreach (var stat in arrival)
            {
                IEnumerable<Flight> suitflights = allflights.Where(x => x.ArrivalPoint == stat.ID);
                foreach (var fl in suitflights)
                    flights.Add(fl);
            }
            return flights;
        }
    }
}
