/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
    package com.lab8.servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.lab5.model.*;
import com.lab5.dao.*;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

@WebServlet("/view_reporter")
public class ViewReporter extends HttpServlet {
	private static final long serialVersionUID = 123124L;

	@Override
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		int id = ServletHelper.getIntParameter(request, "id", -1);
		Userdao udao = new Userdao();
		
		User user = null;
		try {
			user = udao.read(id);
		} catch (SQLException e) {
			throw new IOException("No reporter with such id");
		}

		String delete = request.getParameter("delete");
		if ("true".equals(delete)) {
			try {
				udao.delete(user);
			} catch (SQLException e) {
			}
			response.sendRedirect("view");
		}
		
		PrintWriter out = response.getWriter();
		out.print(ServletHelper.headWithTitle(user.getName()));		
	    out.println("<body><table class=\"title\">\n<tr><th>" + user.getName() + "</th></tr>");
	    out.println("<tr><td><a href=\"edit_reporter?id=" + id + "\">[ Edit ]</a>");
	    out.println("<a href=\"view_reporter?id=" + id + "&delete=true\">[ Delete ]</a></td></tr>");
	    out.println("</table><p/>");	    
	    out.println("<table><tr><th>Tasks: </th></tr>");
            Taskdao tdao=new Taskdao();
            try {
                ArrayList<Task> tasks=tdao.getAllbyUser(user.getID());
                for (Task t: tasks) {
	    	out.println("<tr><td><a href=\"view_task?id=" + t.getID() + "\">" + 
	    			t.getDescription() + "</a></td></tr>");
	    }
            } catch (SQLException ex) {
                Logger.getLogger(ViewReporter.class.getName()).log(Level.SEVERE, null, ex);
            }
	    out.println("</table></body></html>");
	}
}
