using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Entities;
using BLL;

namespace PL.Controllers
{
    public class BugapiController : ApiController
    {
        // GET api/<controller>
        public IEnumerable<JsonTask> Get()
        {
            List<Task> l = new List<Task>();
            l = TaskLogic.ReadAll();
            List<JsonTask> jl = new List<JsonTask>();
            foreach (var t in l)
                jl.Add(new JsonTask(t));
            return jl;
        }

        // GET api/<controller>/5
        public JsonTask Get(int id)
        {
            return  new JsonTask(TaskLogic.Read(id, null));
        }

        // POST api/<controller>
        public void Post([FromBody]Task value)
        {
            TaskLogic.Create(value, value.User.ID, value.Project.ID);
        }

        // PUT api/<controller>/5
        public void Put(int id, [FromBody]Task value)
        {
            TaskLogic.Update(value, null);
        }

        // DELETE api/<controller>/5
        public void Delete(int id)
        {
            TaskLogic.Delete(id,null);
        }
    }
}