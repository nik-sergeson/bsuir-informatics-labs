using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;
using System.Data.SqlClient;
using Entities;
using DALInterfaces;

namespace SQLDal
{
    public static class TaskReaderWriter : ITaskDataAccess
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

        public void Create(Entities.Task task)
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "INSERT INTO Task(id, statucid, description, reporterid, opendate, deadline,priority, projectid) VALUES ('" + task.Id + "', '" + task.Status.Id + "', '" + task.Description + "', '" + task.Reporter.Id + "', '" + task.OpenDate + "', '" + task.Deadline + "', '" + task.Priority + "', '" + task.Project.Id + "')";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public Entities.Task Read(int id)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                Task task;
                command.CommandText = "SELECT * FROM Task WHERE id = '" + id + "'";
                connection.Open();
                var reader = command.ExecuteReader();
                if (reader.Read())
                    task = new Task(id,SqlFactory.GetFactory().GetUserDataAccess().Read(reader.GetFieldValue<int>(reader.GetOrdinal("reporterid"))), reader.GetFieldValue<string>(reader.GetOrdinal("description")), reader.GetFieldValue<DateTime>(reader.GetOrdinal("opendate")), reader.GetFieldValue<DateTime>(reader.GetOrdinal("deadline")), reader.GetFieldValue<int>(reader.GetOrdinal("priority")),SqlFactory.GetFactory().GetProjectDataAccess().Read(reader.GetFieldValue<int>(reader.GetOrdinal("projectid"))),SqlFactory.GetFactory().GetCommentDataAccess().ReadAll(id));
                else
                    task = null;
                connection.Close();
                return task;
            }
        }
        public void Update(Task task)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "UPDATE Task SET statusid = '" + task.Status.Id + "', description = '" + task.Description + "', reporterid = '" + task.Reporter.Id + "', opendate = '" + task.OpenDate + "', deadline = '" + task.Deadline + "', priority = '" + task.Priority + "', projectid = '" + task.Project.Id + "'  WHERE id = '" + task.Id + "'";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public void Delete(int ID)
        {
            List<Comment> coms = new List<Comment>(SqlFactory.GetFactory().GetCommentDataAccess().ReadAll(ID));
            foreach (var com in coms)
                SqlFactory.GetFactory().GetCommentDataAccess().Delete(com);
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "DELETE FROM Task WHERE id = '" + ID + "'";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public void Delete(Task task)
        {
            Delete(task.Id);
        }

        public IEnumerable<Task> ReadAll(int projectid)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                List<Task> task = new List<Task>();
                command.CommandText = "SELECT * FROM Task WHERE projectid='"+projectid+"'";
                connection.Open();
                var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    int id=reader.GetFieldValue<int>(reader.GetOrdinal("id"));
                    task.Add(new Task(id,SqlFactory.GetFactory().GetUserDataAccess().Read(reader.GetFieldValue<int>(reader.GetOrdinal("reporterid"))), reader.GetFieldValue<string>(reader.GetOrdinal("description")), reader.GetFieldValue<DateTime>(reader.GetOrdinal("opendate")), reader.GetFieldValue<DateTime>(reader.GetOrdinal("deadline")), reader.GetFieldValue<int>(reader.GetOrdinal("priority")),SqlFactory.GetFactory().GetProjectDataAccess().Read(reader.GetFieldValue<int>(reader.GetOrdinal("projectid"))),SqlFactory.GetFactory().GetCommentDataAccess().ReadAll(id)));
                }
                connection.Close();
                return task;
            }
    }
    }
}