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
    public static class ClientLogic
    {
        private static IClientStorable readerwriter;
        static ClientLogic()
        {
            ExeConfigurationFileMap map = new ExeConfigurationFileMap();
            map.ExeConfigFilename = @"D:\isp-3\ProjectEntities\BLL.config";
            Configuration cfg = ConfigurationManager.OpenMappedExeConfiguration(map, ConfigurationUserLevel.None);
            AppSettingsSection section = (cfg.GetSection("appSettings") as AppSettingsSection);
            if (section.Settings["dataSource"].Value == "SQL")
                readerwriter = new ClientSqlReaderWriter();
            else
                readerwriter = new ClientReaderWriter();
        }

        public static void AddClient(Client client)
        {
            readerwriter.Add(client);
        }

        public static void DeleteClient(int ID)
        {
            readerwriter.Delete(ID);
        }

        public static void UpdateClient(Client client)
        {
            readerwriter.Update(client);
        }

        public static List<Client> ReadAll()
        {
            return readerwriter.ReadAll();
        }

        public static Client Read(int id)
        {
            return readerwriter.Read(id);
        }
    }
}
