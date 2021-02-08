package com.lab5.model;

import java.util.Date;


public class Task {
    private long ID;
    private String description;
    private User user;
    private Date opendate;
    private Date deadline;
    private int priority;

    public long getID() {
        return ID;
    }

    public void setID(long ID) {
        this.ID = ID;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public Date getOpendate() {
        return opendate;
    }

    public void setOpendate(Date opendate) {
        this.opendate = opendate;
    }

    public Date getDeadline() {
        return deadline;
    }

    public void setDeadline(Date deadline) {
        this.deadline = deadline;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public Task(String description,User user,Date deadline,int priority){
        this.description=description;
        this.user=user;
        this.opendate=new Date();
        this.deadline=deadline;
        this.priority=priority;
    }

    public Task(String description,User user,Date opendate,Date deadline,int priority){
        this.description=description;
        this.user=user;
        this.opendate=opendate;
        this.deadline=deadline;
        this.priority=priority;
    }

    public Task(){
        this.description="";
        this.user=null;
        this.opendate=new Date();
        this.deadline=new Date();
        this.priority=0;
    }
}
