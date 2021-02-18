using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace BugTracker
{
    public partial class Register : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void AccountRegister(object sender, EventArgs e)
        {
           /* var userInfo = new VLuserinfo();
            userInfo.Firstname = wFirstName.Text;
            userInfo.Lastname = wLastName.Text;
            if (VLUserManager.IsLoginExist(wUserName.Text))
            {
                wUserName.BackColor = Color.Red;
                return;
            }

            wUserName.BackColor = Color.White;
            var session = VLUserManager.RegisterUser(wUserName.Text, wPassword.Text, userInfo);
            Session["CURRENT_SESSION"] = session;
            WebHelper.NavigateToHome();*/
        }
    }
}