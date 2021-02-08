/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.jsp;
import com.lab5.model.Task;
import java.util.ArrayList;
import java.util.Iterator;
import javax.servlet.jsp.JspException;
import javax.servlet.jsp.tagext.TagSupport;

/**
 *
 * @author nik-u
 */
public class IteratorTag extends TagSupport{
    private Iterator<Task> iterator = null;
    private ArrayList<Task> list = null;
    private String item = null;

    public String getitem() {
        return item;
    }
	
    public void setitem(String item) {
	this.item=item;
    }
	
    public ArrayList<Task> getlist() {
	return list;
    }

    public void setlist(ArrayList<Task> list) {
        this.list = list;
    }

    private static final long serialVersionUID = 321321L;

    @Override
	public int doStartTag() throws JspException {
            iterator = list.iterator();
            return EVAL_BODY_INCLUDE;
	}

	@Override
	public int doAfterBody() throws JspException {
	if (iterator.hasNext()) {
            Task task = iterator.next();
            pageContext.setAttribute(item, task);
            return (EVAL_BODY_AGAIN);
	} else {
            iterator = null;
            return (SKIP_BODY);
	}
	}
}
