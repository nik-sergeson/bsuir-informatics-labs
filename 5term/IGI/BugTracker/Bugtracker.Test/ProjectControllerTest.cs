using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using PL.Controllers;
using Entities;
using System.Web.Mvc;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using BLL;

namespace Bugtracker.Test
{
    [TestClass]
    public class ProjectControllerTest
    {
        [TestMethod]
        public void Index()
        {
            ProjectController controller = new ProjectController();
            ActionResult result = controller.Index(ProjectLogic.ReadAll(null).FirstOrDefault().ID);
            Assert.IsInstanceOfType(result, typeof(ViewResult));
        }

        [TestMethod]
        public void ViewAll()
        {
            ProjectController controller = new ProjectController();
            ViewResult result = controller.ViewAll() as ViewResult;
            Assert.IsNotNull(result);
        }

        [TestMethod]
        public void EditProjectForm()
        {
            ProjectController controller = new ProjectController();
            ActionResult result = controller.EditProjectForm(ProjectLogic.ReadAll(null).FirstOrDefault().ID);
            Assert.IsInstanceOfType(result, typeof(ViewResult));
            ViewResult vres = (ViewResult)result;
            Assert.IsNotNull(vres.ViewData["Project"]);
        }

        [TestMethod]
        public void EditProject()
        {
            ProjectController controller = new ProjectController();
            ActionResult result = controller.EditProject(BLL.ProjectLogic.Read(ProjectLogic.ReadAll(null).FirstOrDefault().ID, null));
            Assert.IsInstanceOfType(result, typeof(RedirectToRouteResult));
            RedirectToRouteResult red = (RedirectToRouteResult)result;
            Assert.AreEqual("Project", red.RouteValues["controller"]);
            Assert.AreEqual("ViewAll", red.RouteValues["action"]);
        }
    }
}
