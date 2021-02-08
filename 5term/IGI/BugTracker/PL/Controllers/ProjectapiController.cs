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
    public class ProjectapiController : ApiController
    {
        // GET api/<controller>
        public IEnumerable<JsonProject> Get()
        {
            List<Project> pl = new List<Project>();
            pl = ProjectLogic.ReadAll(null);
            List<JsonProject> jl=new List<JsonProject>();
            foreach (var p in pl)
                jl.Add(new JsonProject(p));
            return jl;
        }

        // GET api/<controller>/5
        public JsonProject Get(int id)
        {
            return new JsonProject(ProjectLogic.Read(id, null));
        }

        // POST api/<controller>
        public void Post([FromBody]Project value)
        {
            ProjectLogic.Create(value, value.User.ID);
        }

        // PUT api/<controller>/5
        public void Put(int id, [FromBody]Project value)
        {
            ProjectLogic.Update(value, value.User.ID);
        }

        // DELETE api/<controller>/5
        public void Delete(int id)
        {
            ProjectLogic.Delete(id, null);
        }
    }
}