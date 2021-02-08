using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.Http;
using System.Web.Mvc;
using System.Web.Optimization;
using System.Web.Routing;

namespace BugTracker
{
    // Note: For instructions on enabling IIS6 or IIS7 classic mode, 
    // visit http://go.microsoft.com/?LinkId=9394801

    public class MvcApplication : System.Web.HttpApplication
    {
        protected void Application_Start()
        {
            AreaRegistration.RegisterAllAreas();

            WebApiConfig.Register(GlobalConfiguration.Configuration);
            FilterConfig.RegisterGlobalFilters(GlobalFilters.Filters);
            RouteConfig.RegisterRoutes(RouteTable.Routes);
            BundleConfig.RegisterBundles(BundleTable.Bundles);
            AuthConfig.RegisterAuth();
            ScriptManager.ScriptResourceMapping.AddDefinition("jquery",
       new ScriptResourceDefinition
       {
           Path = "~/Scripts/jquery-1.7.1.min.js",
           DebugPath = "~/Scripts/jquery-1.7.1.min.js",
           CdnPath = "http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.9.1.min.js",
           CdnDebugPath = "http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.9.1.min.js"
       });
        }
    }
}