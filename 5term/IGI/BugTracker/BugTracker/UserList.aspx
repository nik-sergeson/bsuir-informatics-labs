<%@ Page Language="C#"  MasterPageFile="~/master.master" AutoEventWireup="true" CodeBehind="UserList.aspx.cs" Inherits="BugTracker.UserList" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="head">
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="body"> 
     <form id="form1" runat="server">
<div>
        <div id="sitename" style="text-align: center;">
	        Bugtracker
        </div>
         <div id="usermenu">             
            <asp:Table ID="width100" CssClass="width100" runat="server">
			<asp:TableRow>
				<asp:TableCell CssClass="menu">
				<asp:HyperLink ID="HyperLink1" runat="server" Text="Home" NavigateUrl="Main.aspx"></asp:HyperLink> | 
				<asp:HyperLink ID="HyperLink2"  runat="server" Text="Forum" NavigateUrl='<%# "~/Album.aspx?id=" + Eval("Id") %>'><%# Eval("Name") %></asp:HyperLink> | 
				<asp:HyperLink ID="HyperLink3" runat="server" Text="Wiki" NavigateUrl='<%# "~/Album.aspx?id=" + Eval("Id") %>'><%# Eval("Name") %></asp:HyperLink> |  |
				<asp:HyperLink ID="HyperLink4" runat="server" Text="Register" NavigateUrl="~/Register.aspx"></asp:HyperLink> 
				</asp:TableCell>                       
             </asp:TableRow>                    
        </asp:Table>
        </div>
        <div id="projectmenu">             
        <asp:Table ID="hide" CssClass="hide" runat="server">
			<asp:TableRow>
				<asp:TableCell CssClass="login-info-left">
				<asp:HyperLink ID="HyperLink5" runat="server" Text="Login" NavigateUrl="ChangePassword.aspx"></asp:HyperLink>
				</asp:TableCell>                 
                <asp:TableCell CssClass="login-info-right" >
                <asp:HyperLink ID="HyperLink6" runat="server" Text="Projects" NavigateUrl="Projects.aspx"></asp:HyperLink>
                </asp:TableCell>      
             </asp:TableRow>                    
        </asp:Table>
         </div>
        <div id="submenu">             
            <asp:Table ID="subtable" CssClass="width100" runat="server">
			<asp:TableRow>
				<asp:TableCell CssClass="menu">
				<asp:HyperLink ID="Allissues" runat="server" Text="All issues" NavigateUrl="Main.aspx"></asp:HyperLink> | 
				<asp:HyperLink ID="Changelog"  runat="server" Text="Changelog" NavigateUrl='<%# "~/Album.aspx?id=" + Eval("Id") %>'><%# Eval("Name") %></asp:HyperLink> | 
				<asp:HyperLink ID="Roadmap" runat="server" Text="Roadmap" NavigateUrl='<%# "~/Album.aspx?id=" + Eval("Id") %>'><%# Eval("Name") %></asp:HyperLink> |  
				</asp:TableCell>                       
             </asp:TableRow>                    
        </asp:Table>
        </div>
        <div id="page">
        <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="true"> 
      </asp:GridView>
          <asp:GridView ID="GridView2" runat="server" AutoGenerateColumns="true"> 
      </asp:GridView>
        </div>
    </div>
         </form>
</asp:Content>