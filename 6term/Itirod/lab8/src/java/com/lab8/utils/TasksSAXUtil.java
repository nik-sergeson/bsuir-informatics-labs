/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package com.lab8.utils;

import com.lab5.model.Task;
import com.lab5.model.User;
import com.lab8.utils.SaxIDHelper;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;


public class TasksSAXUtil extends DefaultHandler {
    
    private ArrayList<Task> tasks = null;
    private Task task = null;
    private User user=null;
    private String propertyvalue;
    private SaxIDHelper ids;
    private int propertyid;
 
 
    public ArrayList<Task> getTasks() {
        return tasks;
    }
    
    public TasksSAXUtil(){
        tasks=new ArrayList<Task>();
        propertyvalue="";
        ids=new SaxIDHelper();
    }
 
    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) {
        
        if (qName.equalsIgnoreCase("com.lab5.model.Task")) {
            task=new Task();
            propertyid=-1;
        } else if (qName.equalsIgnoreCase("user")) {
            user=new User();
            propertyid=-1;
        }
        else if (qName.equalsIgnoreCase("id")&&user==null) {
            propertyid=ids.getTaskid();
        }else if (qName.equalsIgnoreCase("description")) {
            propertyid=ids.getDescription();
        }else if (qName.equalsIgnoreCase("id")) {
            propertyid=ids.getUserid();
        }else if (qName.equalsIgnoreCase("login")) {
            propertyid=ids.getLogin();
        }else if (qName.equalsIgnoreCase("name")) {
            propertyid=ids.getName();
        }else if (qName.equalsIgnoreCase("email")) {
            propertyid=ids.getEmail();
        }else if (qName.equalsIgnoreCase("password")) {
            propertyid=ids.getPassword();
        }else if (qName.equalsIgnoreCase("opendate")) {
            propertyid=ids.getOpendate();
        }else if (qName.equalsIgnoreCase("deadline")) {
            propertyid=ids.getDeadline();
        }else if (qName.equalsIgnoreCase("priority")) {
            propertyid=ids.getPriority();
        }
    }
 
 
    @Override
    public void endElement(String uri, String localName, String qName)  {
        if (qName.equalsIgnoreCase("com.lab5.model.Task")) {
            tasks.add(task);
            task=null;
            user=null;
        }
        else if (qName.equalsIgnoreCase("user")){
            task.setUser(user);
            user=null;
        }
        else if (qName.equalsIgnoreCase("list")){
            return;
        }
        else if (propertyid==ids.getTaskid()){
            task.setID(Long.parseLong(propertyvalue));
        }
        else if (propertyid==ids.getDescription()){
            task.setDescription(propertyvalue);
        }
        else if (propertyid==ids.getUserid()){
            user.setID(Long.parseLong(propertyvalue));
        }
        else if (propertyid==ids.getLogin()){
            user.setLogin(propertyvalue);
        }
        else if (propertyid==ids.getName()){
            user.setName(propertyvalue);
        }
        else if (propertyid==ids.getEmail()){
            user.setEmail(propertyvalue);
        }
        else if (propertyid==ids.getPassword()){
            user.setPassword(propertyvalue);
        }
        else if (propertyid==ids.getOpendate()){
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            try {
                task.setOpendate(sdf.parse(propertyvalue));
            } catch (ParseException ex) {
                ex.printStackTrace();
            }
        }
        else if (propertyid==ids.getDeadline()){
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            try {
                task.setDeadline(sdf.parse(propertyvalue));
            } catch (ParseException ex) {
                ex.printStackTrace();
            }
        }
        else if (propertyid==ids.getPriority()){
            try {
                task.setPriority(Integer.parseInt(propertyvalue));
            }
            catch (NumberFormatException ne){
                ne.printStackTrace();
            }
        }
    }
 
 
    @Override
    public void characters(char ch[], int start, int length)  {
         propertyvalue = new String(ch, start, length);
    }
    
}
