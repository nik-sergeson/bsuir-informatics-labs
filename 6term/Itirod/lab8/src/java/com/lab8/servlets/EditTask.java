/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.servlets;

import com.lab5.model.*;
import com.lab5.dao.*;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/edit_task")
public class EditTask extends HttpServlet {
	private static final long serialVersionUID = 124123L;
	
	private String notNull(String text) {
		return text == null ? "" : text;
	}

	@Override
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		
		int id = ServletHelper.getIntParameter(request, "id", -1);
		Taskdao tdao=new Taskdao();
		
		Task task = null;
		try {
			if (id < 0)
				task=new Task("",null,new Date(),0);
			else
				task=tdao.read(id);
		} catch (SQLException e) {
			throw new IOException("No task with such id");
		}
		
		PrintWriter out = response.getWriter();
		out.println(ServletHelper.headWithTitle("Edit task"));
		out.println("<body><form action=\"edit_task\" method=\"post\">");
		out.println("<input type=\"hidden\" name=\"id\" value=\"" + id + "\"/>");
		out.println("<p><b>Description</b>");
		out.println("<input type=\"text\" name=\"description\" value=\"" + 
				notNull(task.getDescription()) + "\"/></p>");
		if(task.getUser()==null){
                    out.println("<p><b>Reporterid</b>");
                    out.println("<input type=\"text\" name=\"reporterid\" value=-1></p>");
                }
                else{
                    out.println("<p><b>Reporterid</b>");
                    out.println("<input type=\"text\" name=\"reporterid\" value=\"" + 
				task.getUser().getID() + "\"/></p>");
                }
		out.println("<p><b>Deadline</b>");
		out.println("<input type=\"datetime\" name=\"deadline\" value=\"" + 
				task.getDeadline() + "\"/></p>");
                out.println("<p><b>Priority</b>");
		out.println("<input type=\"text\" name=\"priority\" value=\"" + 
				task.getPriority() + "\"/></p>");
		out.println("<p><input type=\"submit\" value=\"Save\"/></p>");
		out.println("</form></body></html>");
	}

	
	@Override
	protected void doPost(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
                int id = ServletHelper.getIntParameter(request, "id", -1);
                String description=request.getParameter("description");
		int reporterid = ServletHelper.getIntParameter(request, "reporterid", -1);
		Date deadline = ServletHelper.getDateParameter(request, "deadline", new Date());
                int priority = ServletHelper.getIntParameter(request, "priority", 0);
                Userdao udao=new Userdao();
                User user=null;
                try {
                    user=udao.read(reporterid);
                } catch (SQLException ex) {
                    Logger.getLogger(EditTask.class.getName()).log(Level.SEVERE, null, ex);
                }
		Task task=new Task(description,user,deadline,priority);
                Taskdao tdao=new Taskdao();
		if (id > 0){
			task.setID(id);
                    try {
                        tdao.update(task);
                    } catch (SQLException ex) {
                        Logger.getLogger(EditTask.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }
                else{
                    try {
                            tdao.create(task);
                    } catch (SQLException e) {
                    }
                }
		response.sendRedirect("view");
	}
}
