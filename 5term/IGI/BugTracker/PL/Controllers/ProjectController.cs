using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace PL.Controllers
{
    public class ProjectController : Controller
    {
        //
        // GET: /Project/

        int currentproject = 0;

        public ActionResult Index(int? id)
        
        {
            if (id.HasValue)
            {
                ViewBag.Proj = BLL.ProjectLogic.Read(id.Value, null);
                ViewBag.Tasks = BLL.TaskLogic.ReadAll(id.Value, null);
                if(User!=null&&User.Identity.IsAuthenticated==true)
                    ViewBag.User = BLL.UserLogic.Read(User.Identity.Name, null);
                currentproject = id.Value;
            }
            return View();
        }

        public ActionResult ViewAll()
        {
            ViewBag.Proj = BLL.ProjectLogic.ReadAll(null);
            if(User!=null&&User.Identity.IsAuthenticated==true)
                ViewBag.User = BLL.UserLogic.Read(User.Identity.Name, null);
            return View();
        }

        public ActionResult NewProject()
        {
            return View();
        }

        [HttpPost]
        [AllowAnonymous]
        [ValidateAntiForgeryToken]
        public ActionResult AddProject(Entities.Project model)
        {
            model.User = BLL.UserLogic.Read(User.Identity.Name, null);
            BLL.ProjectLogic.Create(model, model.User.ID);
            return RedirectToAction("ViewAll", "Project");
        }

        public ActionResult EditProjectForm(int? id)
        {
            ViewBag.Project = BLL.ProjectLogic.Read(id.Value, null);
            return View();
        }

        public ActionResult DeleteProject(int? id)
        {
            BLL.ProjectLogic.Delete(id.Value, null);
            return RedirectToAction("ViewAll", "Project");
        }

        [HttpPost]
        [AllowAnonymous]
        [ValidateAntiForgeryToken]
        public ActionResult EditProject(Entities.Project model)
        {
            if (User != null)
            {
                model.User = BLL.UserLogic.Read(User.Identity.Name, null);
                BLL.ProjectLogic.Update(model, model.User.ID);
            }
            return RedirectToAction("ViewAll", "Project");
        }

        public ActionResult ProjectFormPartial()
        {
            return PartialView();
        }

        public ActionResult ProjectEditPartial()
        {
            return PartialView();
        }
    }

    public class JsonProject
    {
        public int ID { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public string User { get; set; }

        public JsonProject(Entities.Project p)
        {
            ID = p.ID;
            Name = p.Name;
            Description = p.Description;
            User = p.User.Name;
        }
    }
}
