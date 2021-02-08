using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace PL.Controllers
{
    public class UserController : Controller
    {
        //
        // GET: /User/

        public ActionResult Index(string login)
        {
            ViewBag.User = BLL.UserLogic.Read(login,null);
            return View();
        }

        public ActionResult ViewAll()
        {
            ViewBag.Users = BLL.UserLogic.ReadAll();
            ViewBag.User = BLL.UserLogic.Read(User.Identity.Name, null);
            return View();
        }

        public ActionResult Delete(int? id)
        {
            BLL.UserLogic.Delete(id.Value, null);
            return RedirectToAction("ViewAll", "User");
        }

        public ActionResult Moderator(int? id)
        {
            BLL.UserLogic.ChangeGroup(id.Value, 2);
            return RedirectToAction("ViewAll", "User");
        }
    }
}
