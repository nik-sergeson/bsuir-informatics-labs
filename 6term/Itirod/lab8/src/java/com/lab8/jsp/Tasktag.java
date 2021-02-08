/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.jsp;

import com.lab5.model.Task;
import java.io.IOException;
import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.tagext.SimpleTagSupport;


public class Tasktag extends SimpleTagSupport {
    
    private Task task;
    
    public void setTask(Task task){
        this.task=task;
    }
    
    public Task getTask(){
        return task;
    }

  public void doTag() throws JspException, IOException {
    JspWriter out = getJspContext().getOut();		
    if(task!=null){
        out.println("<body><table class=\"title\">\n<tr><th>" + Long.toString(task.getID()) + "</th></tr>");
        out.println("<tr><td><a href=\"edit_task?id=" + task.getID() + "\">[ Edit ]</a>");
        out.println("<a href=\"view_task?id=" + task.getID() + "&delete=true\">[ Delete ]</a></td></tr>");
        out.println("</table><p/>");
        if (task.getDescription() != null) {
            out.println("<b>Description: </b> " + task.getDescription());
            out.println("<p/>");
        }
        out.println("<b>Reporter: </b>" +task.getUser().getLogin()+ "<p/>");
        out.println("<b>Opendate: </b>" +task.getOpendate() + "<p/>");
        out.println("<b>Deadline: </b>" + task.getDeadline() + "<p/>");
        out.println("<b>Priority: </b>" + task.getPriority() + "<p/>");
        out.println("</table></body></html>");
    }
  }
}
