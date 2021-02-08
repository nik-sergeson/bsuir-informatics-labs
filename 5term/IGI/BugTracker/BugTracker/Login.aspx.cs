using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace BugTracker
{
    public partial class Login : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void AccountLogin(object sender, EventArgs e)
        {
           /* var login = UserName.Text;
            var password = Password.Text;
            var session = VLUserManager.LoginUser(login, password);
            Session["CURRENT_SESSION"] = session;
            if (Request.QueryString["ReturnUrl"] != null)
                Response.Redirect(Request.QueryString["ReturnUrl"]);
            else
                WebHelper.NavigateToHome();*/
        }
    }
}