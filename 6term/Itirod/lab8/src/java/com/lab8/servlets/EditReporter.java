/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.servlets;


import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.lab5.model.*;
import com.lab5.dao.*;
import java.util.logging.Level;
import java.util.logging.Logger;

@WebServlet("/edit_reporter")
public class EditReporter extends HttpServlet {
	private static final long serialVersionUID = 123126L;
	
	private String notNull(String text) {
		return text == null ? "" : text;
	}

	@Override
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		
		int id = ServletHelper.getIntParameter(request, "id", -1);
		Userdao udao=new Userdao();
		
		User user = null;
		try {
			if (id < 0)
				user = new User("","","","");
			else
				user = udao.read(id);
		} catch (SQLException e) {
			throw new IOException("No reporter with such id");
		}
		
		PrintWriter out = response.getWriter();
		out.println(ServletHelper.headWithTitle("Edit reporter"));
		out.println("<body><form action=\"edit_reporter\" method=\"post\">");
		out.println("<input type=\"hidden\" name=\"id\" value=\"" + id + "\"/>");
		out.println("<p><b>Name</b>");
		out.println("<input type=\"text\" name=\"name\" value=\"" + 
				notNull(user.getName()) + "\"/></p>");
		out.println("<p><b>Login</b>");
		out.println("<input type=\"text\" name=\"login\" value=\"" + 
				notNull(user.getLogin()) + "\"/></p>");	
                out.println("<p><b>Password</b>");
		out.println("<input type=\"text\" name=\"password\" value=\"" + 
				notNull(user.getPassword()) + "\"/></p>");
                out.println("<p><b>Email</b>");
		out.println("<input type=\"text\" name=\"email\" value=\"" + 
				notNull(user.getEmail()) + "\"/></p>");
		out.println("<p><input type=\"submit\" value=\"Save\"/></p>");
		out.println("</form></body></html>");
	}

	@Override
	protected void doPost(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		String login,name,email,password;
		login=request.getParameter("login");
		name=request.getParameter("name");
                password=request.getParameter("password");
                email=request.getParameter("email");
		Userdao udao=new Userdao();
                User user=new User(login, name, email, password);
		int id = ServletHelper.getIntParameter(request, "id", -1);
		if (id > 0){
			user.setID(id);
                    try {
                        udao.update(user);
                    } catch (SQLException ex) {
                        Logger.getLogger(EditReporter.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }
                else{
                    try {
                            udao.create(user);
                    } catch (SQLException e) {
                    }
                }
		response.sendRedirect("view");
	}
}

