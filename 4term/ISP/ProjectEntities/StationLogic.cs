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
    public static class StationLogic
    {
        private static IStationStorable readerwriter;

        static StationLogic()
        {
            ExeConfigurationFileMap map = new ExeConfigurationFileMap();
            map.ExeConfigFilename = @"D:\isp-3\ProjectEntities\BLL.config";
            Configuration cfg = ConfigurationManager.OpenMappedExeConfiguration(map, ConfigurationUserLevel.None);
            AppSettingsSection section = (cfg.GetSection("appSettings") as AppSettingsSection);
            if (section.Settings["dataSource"].Value == "SQL")
                readerwriter = new StationSqlReaderWriter();
            else
                readerwriter = new StationReaderWriter();
        }

        public static void AddStation(Station station)
        {
            readerwriter.Add(station);
        }

        public static void UpdateStation(Station station)
        {
            readerwriter.Update(station);
        }

        public static void DeleteStation(int ID)
        {
            readerwriter.Delete(ID);
        }

        public static List<Station> ReadAll()
        {
            return readerwriter.ReadAll();
        }

        public static Station Read(int id)
        {
            return readerwriter.Read(id);
        }

        public static List<Station> FindByName(string name)
        {
            return new List<Station>(readerwriter.ReadAll().Where(x => x.Name == name));
        }
    }
}
