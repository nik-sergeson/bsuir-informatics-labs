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
    public static class AeroplaneLogic
    {
        private static IAeroplaneStorable readerwriter;
        static AeroplaneLogic()
        {
            ExeConfigurationFileMap map = new ExeConfigurationFileMap();
            map.ExeConfigFilename = @"D:\isp-3\ProjectEntities\BLL.config";
            Configuration cfg = ConfigurationManager.OpenMappedExeConfiguration(map, ConfigurationUserLevel.None);
            AppSettingsSection section = (cfg.GetSection("appSettings") as AppSettingsSection);
            if (section.Settings["dataSource"].Value == "SQL")
                readerwriter = new AeroplaneSqlReaderWriter();
            else
                readerwriter = new AeroplaneReaderWriter();
        }

        public static void ChangeFlight(Aeroplane aeroplane, int flightid)
        {
            aeroplane.FlightID = flightid;
            readerwriter.Update(aeroplane);
        }

        public static void AddPlane(Aeroplane aeroplane)
        {
            readerwriter.Add(aeroplane);
        }

        public static void DeletePlane(int ID)
        {
            readerwriter.Delete(ID);
        }

        public static List<Aeroplane> ReadAll()
        {
            return readerwriter.ReadAll();
        }

        public static void Update(Aeroplane plane)
        {
            readerwriter.Update(plane);
        }

        public static Aeroplane Read(int id)
        {
            return readerwriter.Read(id);
        }

        public static List<Aeroplane> FindByFlight(int flightid)
        {
            return new List<Aeroplane>(readerwriter.ReadAll().Where(x => x.FlightID == flightid));
        }
    }
}
