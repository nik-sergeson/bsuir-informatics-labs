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

@WebServlet("/view_task")
public class ViewTask extends HttpServlet {
	private static final long serialVersionUID = 123125L;

	@Override
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		int id = ServletHelper.getIntParameter(request, "id", -1);
		Taskdao tdao=new Taskdao();
		
		Task task = null;
		try {
			task=tdao.read(id);
		} catch (SQLException e) {
			throw new IOException("No task with such id");
		}

		String delete = request.getParameter("delete");
		if ("true".equals(delete)) {
			try {
				tdao.delete(task);
			} catch (SQLException e) {
			}
			response.sendRedirect("view");
		}
		
		PrintWriter out = response.getWriter();
		out.print(ServletHelper.headWithTitle(Long.toString(task.getID())));
		
	    out.println("<body><table class=\"title\">\n<tr><th>" + Long.toString(task.getID()) + "</th></tr>");
	    out.println("<tr><td><a href=\"edit_task?id=" + id + "\">[ Edit ]</a>");
	    out.println("<a href=\"view_task?id=" + id + "&delete=true\">[ Delete ]</a></td></tr>");
	    out.println("</table><p/>");
	    
	    if (task.getDescription() != null) {
	    	out.println("<b>Description: </b> " + task.getDescription());
	    	out.println("<p/>");
	    }
	    out.println("<b>Opendate: </b>" +task.getOpendate() + "<p/>");
            out.println("<b>Deadline: </b>" + task.getDeadline() + "<p/>");
            out.println("<b>Priority: </b>" + task.getPriority() + "<p/>");
	    out.println("</table></body></html>");
	}
}
