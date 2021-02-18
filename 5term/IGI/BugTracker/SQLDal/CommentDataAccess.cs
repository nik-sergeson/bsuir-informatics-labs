using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
using System.Data.SqlClient;
using Entities;
using DALInterfaces;

namespace SQLDal
{
    public static class CommentReaderWriter : ICommentDataAccess
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


        public static void Create(Comment com)
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "INSERT INTO Comment(id, text, authorid, creationtime, taskid) VALUES ('" + com.Id + "', '" + com.Text + "', '" + com.Author.Id + "', '" + com.CreationTime + "', '" +com.Task.Id + "')";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public static Comment Read(int id)
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                Comment com;
                command.CommandText = "SELECT * FROM Comment WHERE id = '" + id + "'";
                connection.Open();
                var reader = command.ExecuteReader();
                if (reader.Read())
                    com = new Comment(id, reader.GetFieldValue<string>(reader.GetOrdinal("text")),SqlFactory.GetFactory().GetUserDataAccess().Read(reader.GetFieldValue<string>(reader.GetOrdinal("authorid"))), reader.GetFieldValue<DateTime>(reader.GetOrdinal("creationtime")),SqlFactory.GetFactory().GetTaskDataAccess().Read(reader.GetFieldValue<int>(reader.GetOrdinal("taskid"))));
                else
                    com = null;
                connection.Close();
                return com;
            }
        }
        public static void Update(Comment com)
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "UPDATE Comment SET text = '" + com.Text + "', authorid = '" + com.Author.Id + "', creationtime = '" + com.CreationTime + "', taskid = '" + com.Task.Id + "'  WHERE id = '" + com.Id + "'";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public static void Delete(int ID)
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                command.CommandText = "DELETE FROM Comment WHERE id = '" + ID + "'";
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
        }

        public void Delete(Comment com)
        {
            Delete(com.Id);
        }

        public IEnumerable<Comment> ReadAll(int taskid)
        {
            using (SqlConnection connection = new SqlConnection(GetString()))
            {
                SqlCommand command = connection.CreateCommand();
                List<Comment> coms=new System.Collections.Generic.List<Comment>();
                command.CommandText = "SELECT * FROM Task WHERE taskid='"+taskid+"'";
                connection.Open();
                var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    coms.Add(new Comment(reader.GetFieldValue<int>(reader.GetOrdinal("id")), reader.GetFieldValue<string>(reader.GetOrdinal("text")),SqlFactory.GetFactory().GetUserDataAccess().Read(reader.GetFieldValue<string>(reader.GetOrdinal("authorid"))), reader.GetFieldValue<DateTime>(reader.GetOrdinal("creationtime")),SqlFactory.GetFactory().GetTaskDataAccess().Read(reader.GetFieldValue<int>(reader.GetOrdinal("taskid")))));
                }
                connection.Close();
                return coms;
            }
    }
    }
}
