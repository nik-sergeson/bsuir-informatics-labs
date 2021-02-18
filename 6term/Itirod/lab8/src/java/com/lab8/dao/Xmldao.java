/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.dao;
import com.lab5.dao.Idao;
import com.lab5.model.Task;
import com.lab8.utils.IXmlUtil;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;


public class Xmldao implements  Idao<Task>{
    private InputStream in;
    private OutputStream out;
    private IXmlUtil xmlUtil;
    
    public IXmlUtil getXmlUtil() {
        return xmlUtil;
    }
    
    public void setXmlUtil(IXmlUtil xmlUtil) {
        this.xmlUtil = xmlUtil;
    }
    
    public InputStream getIn() {
        return in;
    }
    
    public void setIn(InputStream in) {
        this.in = in;
    }
    
    public OutputStream getOut() {
        return out;
    }
    
    public void setOut(OutputStream out) {
        this.out = out;
    }
    
    public Xmldao() {
    }
    
    public Xmldao(InputStream in, OutputStream out) {
        this.in = in;
        this.out = out;
    }
    
    public void create(Task task) {
    try {
        ArrayList<Task> tasks=xmlUtil.loadTasks(in);
        if (tasks == null)
            tasks = new ArrayList<Task>();
        tasks.add(task);
        xmlUtil.saveTasks(out, tasks);
    } catch (Exception ex) {
        ex.printStackTrace();
    }
}
    
    public Task read(long id) {
        Task task = null;
        try {
        ArrayList<Task> tasks = xmlUtil.loadTasks(in);
        if (tasks != null && tasks.size() > 0) {
            for (Task t : tasks) {
                if (t.getID()== id) {
                    task = t;
                    break;
                }
            }
        }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return task;
    }
    
    public void update(Task task) {
        try {
            ArrayList<Task> tasks = xmlUtil.loadTasks(in);
            if (tasks != null && tasks.size() > 0) {
                for (Task t : tasks) {
                    if (t.getID()== task.getID()) {
                        t.setDeadline(task.getDeadline());
                        t.setDescription(task.getDescription());
                        t.setID(task.getID());
                        t.setOpendate(task.getOpendate());
                        t.setPriority(task.getPriority());
                        t.setUser(task.getUser());
                    }
                }
            xmlUtil.saveTasks(out, tasks);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
    
    public void delete(Task task) {
        try {
            ArrayList<Task> tasks = xmlUtil.loadTasks(in);
            if (tasks != null && tasks.size() > 0) {
                int tIndex = -1;
                for (int i = 0; i < tasks.size(); i++) {
                    if (tasks.get(i).getID()== task.getID()) {
                        tIndex = i;
                        break;
                    }
                }
                tasks.remove(tIndex);
                xmlUtil.saveTasks(out, tasks);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
    
    public ArrayList<Task> getAll() {
        ArrayList<Task> result = null;
        try {
            if (in == null || xmlUtil == null)
                throw new Exception("XmlStudentDao fields not set.");
            result = xmlUtil.loadTasks(in);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return result;
    }
}
