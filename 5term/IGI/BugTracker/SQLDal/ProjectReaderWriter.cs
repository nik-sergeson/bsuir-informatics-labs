using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
using System.Data.SqlClient;
using DALInterfaces;
using Entities;

namespace SQLDal
{
    public static class ProjectReaderWriter:IProjectDataAccess
    {
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


        public static void Create(Project project)
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "INSERT INTO Project(id, name, description, creatorid) VALUES ('" + project.Id + "', '" + project.Name + "', '" + project.Description + "', '" + project.Creator + "')";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public Project Read(int id)
        {
            using (SqlConnection connection = new SqlConnection(GetString())){
                SqlCommand command = connection.CreateCommand();
                Project proj;
                command.CommandText = "SELECT * FROM Project WHERE id = '" + id + "'";
                connection.Open();
                var reader = command.ExecuteReader();
                if (reader.Read())
                    proj = new Project(id, reader.GetFieldValue<string>(reader.GetOrdinal("name")), reader.GetFieldValue<string>(reader.GetOrdinal("descritption")), SqlFactory.GetFactory().GetUserDataAccess().Read(reader.GetFieldValue<int>(reader.GetOrdinal("creatorid"))),SqlFactory.GetFactory().GetTaskDataAccess().ReadAll(id));
                else
                    proj = null;
                connection.Close();
                return proj;
            }
        }

        public void Update(Project proj)
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "UPDATE Project SET name = '" + proj.Name + "', description = '" + proj.Description + "', creatorid = '" + proj.Creator.Id + "'  WHERE id = '" + proj.Id + "'";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public void Delete(int ID)
        {
            List<Entities.Task> task=new List<Entities.Task>(SqlFactory.GetFactory().GetTaskDataAccess().ReadAll(ID));
            foreach (var tsk in task)
                SqlFactory.GetFactory().GetTaskDataAccess().Delete(tsk);
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "DELETE FROM Project WHERE id = '" + ID + "'";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public void Delete(Project proj)
        {
            Delete(proj.Id);
        }

        public IEnumerable<Project> ReadAll()
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                List<Project> proj = new List<Project>();
                command.CommandText = "SELECT * FROM Project";
                connection.Open();
                var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    proj.Add(new Project(reader.GetFieldValue<int>(reader.GetOrdinal("id")), reader.GetFieldValue<string>(reader.GetOrdinal("name")), reader.GetFieldValue<string>(reader.GetOrdinal("descritption")), SqlFactory.instance.GetUserDataAccess().Read(reader.GetFieldValue<int>(reader.GetOrdinal("creatorid"))), SqlFactory.instance.GetTaskDataAccess().ReadAll(reader.GetFieldValue<int>(reader.GetOrdinal("id")))));
                }
                connection.Close();
                return proj;
            }
        }

        public IEnumerable<Project> ReadAuthorProject(int creatorid)
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                List<Project> proj = new List<Project>();
                command.CommandText = "SELECT * FROM Project WHERE creatorid='"+creatorid+"'";
                connection.Open();
                var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    proj.Add(new Project(reader.GetFieldValue<int>(reader.GetOrdinal("id")), reader.GetFieldValue<string>(reader.GetOrdinal("name")), reader.GetFieldValue<string>(reader.GetOrdinal("descritption")), SqlFactory.instance.GetUserDataAccess().Read(reader.GetFieldValue<int>(reader.GetOrdinal("creatorid"))), SqlFactory.instance.GetTaskDataAccess().ReadAll(reader.GetFieldValue<int>(reader.GetOrdinal("id")))));
                }
                connection.Close();
                return proj;
            }
        }
    }
}
