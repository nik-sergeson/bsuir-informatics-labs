using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Web.Mvc;
using PL.Controllers;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using BLL;

namespace Bugtracker.Test
{
    [TestClass]
    public class BugControllerTest
    {
        [TestMethod]
        public void Index()
        {
            BugController controller = new BugController();
            ActionResult result = controller.Index(TaskLogic.ReadAll().FirstOrDefault().ID);
            Assert.IsInstanceOfType(result, typeof(ViewResult));
        }

        [TestMethod]
        public void ViewAll()
        {
            BugController controller = new BugController();
            ViewResult result = controller.ViewAll() as ViewResult;
            Assert.IsNotNull(result);
        }

        [TestMethod]
        public void EditTaskForm()
        {
            BugController controller = new BugController();
            ActionResult result = controller.EditTaskForm(TaskLogic.ReadAll().FirstOrDefault().ID);
            Assert.IsInstanceOfType(result,typeof(ViewResult));
            ViewResult vres=(ViewResult)result;
            Assert.IsNotNull(vres.ViewData["Task"]);
        }

        [TestMethod]
        public void EditTask()
        {
            BugController controller = new BugController();
            ActionResult result = controller.EditTask(BLL.TaskLogic.ReadAll().FirstOrDefault());
            Assert.IsInstanceOfType(result, typeof(RedirectToRouteResult));
            RedirectToRouteResult red = (RedirectToRouteResult)result;
            Assert.AreEqual("Bug", red.RouteValues["controller"]);
        }

        [TestMethod]
        public void EditCommentForm()
        {
            BugController controller = new BugController();
            List<Entities.Comment> lst = BLL.CommentLogic.ReadAll(TaskLogic.ReadAll().FirstOrDefault().ID, null);
            if (lst.Count > 0)
            {
                ActionResult result = controller.EditCommentForm(lst[0].ID);
                Assert.IsInstanceOfType(result, typeof(ViewResult));
                ViewResult vres = (ViewResult)result;
                Assert.IsNotNull(vres.ViewData["Comment"]);
            }
        }
    }
}
