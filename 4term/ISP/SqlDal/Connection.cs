using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using System.Configuration;

namespace SqlDal
{
    public static class ConnectionToServer
    {
        public static SqlConnection Connection { get; set; }

        static ConnectionToServer()
        {
            var builder = new SqlConnectionStringBuilder();
            builder.PersistSecurityInfo = false;
            ExeConfigurationFileMap map = new ExeConfigurationFileMap();
            map.ExeConfigFilename = @"D:\isp-3\SqlDal\SqlDal.config";
            Configuration cfg = ConfigurationManager.OpenMappedExeConfiguration(map, ConfigurationUserLevel.None);
            AppSettingsSection section = (cfg.GetSection("appSettings") as AppSettingsSection);
            builder.DataSource = section.Settings["dataSource"].Value;
            builder.InitialCatalog = section.Settings["dbname"].Value;
            builder.IntegratedSecurity = true;
            Connection = new SqlConnection(builder.ConnectionString);
        }
    }
}
