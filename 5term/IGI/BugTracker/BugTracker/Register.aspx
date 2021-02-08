<%@ Page Language="C#"  MasterPageFile="~/master.master" AutoEventWireup="true" CodeBehind="Register.aspx.cs" Inherits="BugTracker.Register" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="head">
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="body">
 <form id="form1" runat="server">
    <div>
        <h2>
            Create a New Account
        </h2>
        <p>
            Use the form below to create a new account.
        </p>
        <p>
            Passwords are required to be a minimum of  <%= Membership.MinRequiredPasswordLength %> characters in length.
        </p>
        <span class="failureNotification">
            <asp:Literal ID="ErrorMessage" runat="server"></asp:Literal>
        </span>
        <asp:ValidationSummary ID="RegisterUserValidationSummary" runat="server" CssClass="failureNotification" 
                ValidationGroup="RegisterUserValidationGroup"/>
        <div class="accountInfo">
            <fieldset class="register">
                <legend>Account Information</legend>
                <p>
                    <asp:Label ID="UserNameLabel" runat="server" CssClass="contentItem" AssociatedControlID="wUserName">User Name:</asp:Label>
                    <asp:TextBox ID="wUserName" runat="server" CssClass="contentItem contentItemInput"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="UserNameRequired" runat="server" ControlToValidate="wUserName" 
                            CssClass="failureNotification" ErrorMessage="User Name is required." ToolTip="User Name is required." 
                            ValidationGroup="RegisterUserValidationGroup">*</asp:RequiredFieldValidator>
                </p>
                <p>
                    <asp:Label ID="PasswordLabel" runat="server" CssClass="contentItem" AssociatedControlID="wPassword">Password:</asp:Label>
                    <asp:TextBox ID="wPassword" runat="server" CssClass="contentItem contentItemInput"  TextMode="Password"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="PasswordRequired" runat="server" ControlToValidate="wPassword" 
                            CssClass="failureNotification" ErrorMessage="Password is required." ToolTip="Password is required." 
                            ValidationGroup="RegisterUserValidationGroup">*</asp:RequiredFieldValidator>
                </p>
                <p>
                    <asp:Label ID="ConfirmPasswordLabel" runat="server" CssClass="contentItem"  AssociatedControlID="wConfirmPassword">Confirm Password:</asp:Label>
                    <asp:TextBox ID="wConfirmPassword" runat="server" CssClass="contentItem contentItemInput" TextMode="Password"></asp:TextBox>
                    <asp:RequiredFieldValidator ControlToValidate="wConfirmPassword" CssClass="failureNotification" Display="Dynamic" 
                            ErrorMessage="Confirm Password is required." ID="ConfirmPasswordRequired" runat="server" 
                            ToolTip="Confirm Password is required." ValidationGroup="RegisterUserValidationGroup">*</asp:RequiredFieldValidator>
                    <asp:CompareValidator ID="PasswordCompare" runat="server" ControlToCompare="wPassword" ControlToValidate="wConfirmPassword" 
                            CssClass="failureNotification" Display="Dynamic" ErrorMessage="The Password and Confirmation Password must match."
                            ValidationGroup="RegisterUserValidationGroup">*</asp:CompareValidator>
                </p>
                <p>
                    <asp:Label ID="wFirstNameLabel" runat="server" CssClass="contentItem" AssociatedControlID="wFirstName">First name:</asp:Label>
                    <asp:TextBox ID="wFirstName" runat="server" CssClass="contentItem contentItemInput" ></asp:TextBox>
                    <asp:RequiredFieldValidator ID="EmailRequired" runat="server" ControlToValidate="wFirstName" 
                            CssClass="failureNotification" ErrorMessage="First name is required." ToolTip="E-mail is required." 
                            ValidationGroup="RegisterUserValidationGroup">*</asp:RequiredFieldValidator>
                </p>
                <p>
                    <asp:Label ID="wLastNameLabel" runat="server" CssClass="contentItem" AssociatedControlID="wLastName">Last name:</asp:Label>
                    <asp:TextBox ID="wLastName" runat="server" CssClass="contentItem contentItemInput" ></asp:TextBox>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ControlToValidate="wLastName" 
                            CssClass="failureNotification" ErrorMessage="Last name is required." ToolTip="E-mail is required." 
                            ValidationGroup="RegisterUserValidationGroup">*</asp:RequiredFieldValidator>
                </p>
            </fieldset>
            <p class="submitButton">
                <asp:Button ID="CreateUserButton" runat="server" CommandName="MoveNext" Text="Create User" 
                        ValidationGroup="RegisterUserValidationGroup" OnClick="AccountRegister" />
            </p>
        </div>
    </div>
     </form>
</asp:Content>