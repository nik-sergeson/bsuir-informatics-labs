using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using System.Reflection;
using System.Globalization;
using System.Data.SqlClient;


namespace DALInterfaces
{
    public abstract class DataAccessFactory
    {
        public static DataAccessFactory instance;

        public static DataAccessFactory GetFactory()
        {
            if (instance == null)
            {
                string assemblyName = null, factoryName = null, factoryConfig = null;
                try
                {
                    ExeConfigurationFileMap map = new ExeConfigurationFileMap();
                    map.ExeConfigFilename = @"D:\Labs\labs.5term\IGI\BugTracker\DALInterfaces\App.config";
                    Configuration cfg = ConfigurationManager.OpenMappedExeConfiguration(map, ConfigurationUserLevel.None);
                    AppSettingsSection section = (cfg.GetSection("appSettings") as AppSettingsSection);
                    assemblyName = section.Settings["dataAccessAssemblyName"].Value;
                    factoryName = section.Settings["dataAccessFactoryName"].Value;
                    if (factoryName == "SQLDal.SQLFactory")
                    {
                        var builder = new SqlConnectionStringBuilder();
                        builder.PersistSecurityInfo = false;
                        builder.DataSource = section.Settings["dataSource"].Value;
                        builder.InitialCatalog = section.Settings["dbname"].Value;
                        builder.IntegratedSecurity = true;
                        instance = new SQLDal.SqlFactory(builder.ConnectionString);
                    }
                }
                catch (Exception e)
                {
                    throw new Exception("Error while loading configuration parameters", e);
                }

               // var assembly = Assembly.LoadFrom(assemblyName);
                //instance = assembly.CreateInstance(factoryName, false, BindingFlags.Default,
                   // null, new object[] { factoryConfig }, CultureInfo.InvariantCulture, null) as DataAccessFactory;
            }
            return instance;
        }

        public static string GetString()
        {
            ExeConfigurationFileMap map = new ExeConfigurationFileMap();
            map.ExeConfigFilename = @"D:\Labs\labs.5term\IGI\BugTracker\DALInterfaces\App.config";
            Configuration cfg = ConfigurationManager.OpenMappedExeConfiguration(map, ConfigurationUserLevel.None);
            AppSettingsSection section = (cfg.GetSection("appSettings") as AppSettingsSection);
            var builder = new SqlConnectionStringBuilder();
            builder.PersistSecurityInfo = false;
            builder.DataSource = section.Settings["dataSource"].Value;
            builder.InitialCatalog = section.Settings["dbname"].Value;
            builder.IntegratedSecurity = true;
            return builder.ConnectionString;
        }

        public DataAccessFactory(string config) { }
        public abstract ITaskDataAccess GetTaskDataAccess();
        public abstract IUserDataAccess GetUserDataAccess();
        public abstract IProjectDataAccess GetProjectDataAccess();
        public abstract ICommentDataAccess GetCommentDataAccess();
    }
}
