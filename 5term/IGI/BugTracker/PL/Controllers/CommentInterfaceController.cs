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
    public class CommentInterfaceController : ApiController
    {
        // GET api/<controller>
        public IEnumerable<JsonComment> Get()
        {
            List<Comment> l = new List<Comment>();
            l = CommentLogic.ReadAll(1, null);
            List<JsonComment> jcom = new List<JsonComment>();
            foreach (var com in l)
                jcom.Add(new JsonComment(com));
            return jcom;
        }

        // GET api/<controller>/5
        public JsonComment Get(int id)
        {
            return new JsonComment(CommentLogic.Read(id, null));
        }

        // POST api/<controller>
        public void Post([FromBody]Comment value)
        {
            CommentLogic.Create(value, value.User.ID, value.Task.ID);
        }

        // PUT api/<controller>/5
        public void Put(int id, [FromBody]Comment value)
        {
            CommentLogic.Update(value, value.User.ID);
        }

        // DELETE api/<controller>/5
        public void Delete(int id)
        {
            CommentLogic.Delete(id,null);
        }
    }
}