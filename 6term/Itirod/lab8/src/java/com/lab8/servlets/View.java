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
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.lab5.model.*;
import com.lab5.dao.*;

@WebServlet("/view")
public class View extends HttpServlet {
	private static final long serialVersionUID = 123123L;

	@Override
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
	    PrintWriter out = response.getWriter();
    
	    List<Task> tasks = null;
	    try {
		    Taskdao tdao = new Taskdao();
		    tasks=tdao.getAll();
	    } catch (SQLException e) {
	    	tasks = new ArrayList<Task>();
	    }
	    List<User> users = null;
	    try {
	    	Userdao udao = new Userdao();
	    	users = udao.getAll();
	    } catch (SQLException e) {
	    	users = new ArrayList<User>();
	    }
	    
	    String title = "All reporters and tasks";
	    out.print(ServletHelper.headWithTitle(title));
	    out.print("<body><table class=\"title\">\n<tr><th>" + title + 
	    		"</th></tr>\n</table>");
	    out.print("<fieldset>\n<legend>Reporters</legend>\n<ul>\n");
	    for (User a: users) {
	    	out.print("<li><a href=\"view_reporter?id=" + a.getID() + "\">" + a.getName() + "</a></li>");
	    }
	    out.print("</ul>\n</fieldset>\n<p/>\n");
	    
	    out.print("<fieldset>\n<legend>Tasks</legend>\n<ul>\n");
	    for (Task b: tasks) {
	    	out.print("<li><a href=\"view_task?id=" + b.getID() + "\">" +
	    			b.getDescription() + "</a></li>");
	    }
	    out.print("</ul>\n</fieldset>\n<p/>\n");
	    out.print("<a href=\"edit_reporter\">[ New reporter ]</a>");
	    out.print("<a href=\"edit_task\">[ New task ]</a>");
	    
	    out.print("</body></html>");
	}
	
}
