using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace PL.Controllers
{
    public class BugController : Controller
    {
        //
        // GET: /Bug/

        int currenttask=1;

        public ActionResult Index(int? BugId)
        {
            if (BugId.HasValue)
            {
                Entities.Task x = BLL.TaskLogic.Read(BugId.Value, null); ;
                ViewBag.Task = x;
                currenttask = BugId.Value;
                ViewBag.ProjName = x.Project.Name;
                ViewBag.RepName = x.User.Name;
                ViewBag.Comments = BLL.CommentLogic.ReadAll(x, null);
                if(User!=null&&User.Identity.IsAuthenticated==true)
                    ViewBag.User = BLL.UserLogic.Read(User.Identity.Name, null);
            }
            return View();
        }

        public ActionResult ViewAll()
        {
            ViewBag.Bugs = BLL.TaskLogic.ReadAll().OrderBy(x => x.OpenDate);
            return View();
        }

        [HttpPost]
        [AllowAnonymous]
        [ValidateAntiForgeryToken]
        public ActionResult Comment(Entities.Comment model)
        {
            model.User = BLL.UserLogic.Read(User.Identity.Name, null);
            model.CreationTime = DateTime.Now;
            model.Task = BLL.TaskLogic.Read(currenttask, null);
            BLL.CommentLogic.Create(model,model.User.ID,model.Task.ID);
            return RedirectToAction("Index", "Bug", new { BugId = currenttask });
        }

        public ActionResult AddTask()
        {
            return View();
        }

        [HttpPost]
        [AllowAnonymous]
        [ValidateAntiForgeryToken]
        public ActionResult NewTask(Entities.Task model)
        {
            model.User = BLL.UserLogic.Read(User.Identity.Name, null);
            model.OpenDate = DateTime.Now;
            model.Priority = 1;
            model.Deadline = DateTime.Now;
            model.Project = BLL.ProjectLogic.Read(currenttask,null);
            BLL.TaskLogic.Create(model,model.User.ID,model.Project.ID);
            return RedirectToAction("Index", "Bug", new { BugId = currenttask });
        }

        public ActionResult EditTaskForm(int? id)
        {
            ViewBag.Task = BLL.TaskLogic.Read(id.Value, null);
            return View();
        }

        public ActionResult DeleteTask(int? id)
        {
            BLL.TaskLogic.Delete(id.Value, null);
            return RedirectToAction("ViewAll", "Bug");
        }

        [HttpPost]
        [AllowAnonymous]
        [ValidateAntiForgeryToken]
        public ActionResult EditTask(Entities.Task model)
        {
            if(User!=null&&User.Identity.IsAuthenticated==true)
                model.User = BLL.UserLogic.Read(User.Identity.Name, null);
            BLL.TaskLogic.Update(model, null);
            return RedirectToAction("ViewAll", "Bug");
        }

        public ActionResult EditCommentForm(int? id)
        {
            ViewBag.Comment = BLL.CommentLogic.Read(id.Value, null);
            return View();
        }

        public ActionResult DeleteComment(int? id)
        {
            BLL.CommentLogic.Delete(id.Value, null);
            return RedirectToAction("Index", "Bug", new { BugId = currenttask });
        }

        [HttpPost]
        [AllowAnonymous]
        [ValidateAntiForgeryToken]
        public ActionResult EditComment(Entities.Comment model)
        {
            model.User = BLL.UserLogic.Read(User.Identity.Name, null);
            BLL.CommentLogic.Update(model, model.User.ID);
            return RedirectToAction("Index", "Bug", new { BugId = currenttask });
        }

        public ActionResult CommentPartial()
        {
            return PartialView();
        }

        public ActionResult FormPartial()
        {
            return PartialView();
        }
    }

    public class JsonComment
    {
        public int ID { get; set; }
        public string Text { get; set; }
        public string User { get; set; }
        public DateTime CreationTime { get; set; }
        public int TaskID { get; set; }

        public JsonComment(Entities.Comment c)
        {
            ID = c.ID;
            Text = c.Text;
            User = c.User.Name;
            CreationTime = c.CreationTime;
            TaskID = c.Task.ID;
        }
    }

    public class JsonTask
    {
        public int ID { get; set; }
        public string Description { get; set; }
        public string User { get; set; }
        public DateTime OpenDate { get; set; }
        public DateTime Deadline { get; set; }
        public int Priority { get; set; }
        public string ProjectName { get; set; }
        public int ProjectID { get; set; }
        public string TaskStatus { get; set; }

        public JsonTask(Entities.Task t)
        {
            ID = t.ID;
            Description = t.Description;
            User = t.User.Name;
            OpenDate = t.OpenDate;
            Deadline = t.Deadline;
            Priority = t.Priority;
            ProjectName = t.Project.Name;
            ProjectID = t.Project.ID;
            TaskStatus = t.TaskStatus.Name;
        }
    }
}
