using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace PL.Controllers
{
    public class ForumController : Controller
    {
        //
        // GET: /Forum/

        public ActionResult Index(string str)
        {
            return View(new List<Entities.Comment>());
        }

    }
}
