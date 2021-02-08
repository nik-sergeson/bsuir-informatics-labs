using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace PL.Controllers
{
    public class WikiController : Controller
    {
        //
        // GET: /Wiki/

        public ActionResult Index(int id)
        {
            ViewBag.ID = id;
            return View();
        }

    }
}
