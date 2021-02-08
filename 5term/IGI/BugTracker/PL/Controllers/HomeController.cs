using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using BLL;
using Entities;
namespace PL.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            List<Task> open, resolv;
            List<Task> all = TaskLogic.ReadAll();
            open = all.Where(x => x.TaskStatus.Name == "Opened").ToList();
            resolv = all.Where(x => x.TaskStatus.Name == "Resolved").ToList();
            ViewBag.open=open;
            ViewBag.resolv = resolv;
            return View();
        }
    }
}
