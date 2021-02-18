using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Data;
using System.Web.UI.WebControls;

namespace BugTracker
{
    public partial class Main : System.Web.UI.Page
    {
        List<int> num = new List<int>();

        protected void Page_Load(object sender, EventArgs e)
        {
            DataTable myTable = new DataTable("MyTestTable");
            DataRow myRow = null;

            myTable.Columns.Add("MyColumn1");
            myTable.Columns.Add("MyColumn2");
            myTable.Columns.Add("MyColumn3");

            myRow = myTable.NewRow();

            myRow["MyColumn1"] = "hello";
            myRow["MyColumn2"] = "and";
            myRow["MyColumn3"] = "good-bye";

            myTable.Rows.Add(myRow);

            //Now we bind the DataTable to the GridView.

            this.GridView1.DataSource = myTable;
            this.GridView1.DataBind(); 
        }
    }
}