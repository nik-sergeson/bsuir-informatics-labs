package com.lab5.dao;

import com.lab5.model.Task;
import com.mysql.jdbc.Statement;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Locale;


public class Taskdao implements Idao<Task> {

    public Task read(long id) throws SQLException {
        Task task;
        int userid=0;
        String sql = "SELECT * FROM task WHERE id=?";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setLong(1, id);
        ResultSet result = statement.executeQuery();
        if(result.next()) {
            String description = result.getString("description");
            userid=result.getInt("userid");
            Date opendate=result.getDate("opendate");
            Date deadline=result.getDate("deadline");
            int priority=result.getInt("priority");
            task = new Task(description,null,opendate,deadline,priority);
            task.setID(id);
        }
        else
            task=null;
        conn.close();
        Userdao userdao=new Userdao();
        if (task!=null)
            task.setUser(userdao.read(userid));
        return task;
    }

    public void create(Task task) throws SQLException {
        String sql = "INSERT INTO task (description, userid, opendate, deadline, priority) VALUES (?, ?, ?, ?, ?)";
        Userdao udao=new Userdao();
        if(udao.read(task.getUser().getID())==null)
            udao.create(task.getUser());
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
        statement.setString(1,task.getDescription());
        statement.setLong(2, task.getUser().getID());
        statement.setDate(3, new java.sql.Date(task.getOpendate().getTime()));
        statement.setDate(4,new java.sql.Date(task.getDeadline().getTime()));
        statement.setInt(5,task.getPriority());
        statement.executeUpdate();
        ResultSet set = statement.getGeneratedKeys();
        if(set.next())
            task.setID(set.getInt(1));
        conn.close();
    }

    public void update(Task task) throws SQLException {
        String sql = "UPDATE task SET description=?, userid=?, opendate=?, deadline=?, priority=? WHERE id=?";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setString(1,task.getDescription());
        statement.setLong(2, task.getUser().getID());
        statement.setDate(3, new java.sql.Date(task.getOpendate().getTime()));
        statement.setDate(4,new java.sql.Date(task.getDeadline().getTime()));
        statement.setInt(5,task.getPriority());
        statement.setLong(6, task.getID());
        statement.executeUpdate();
        conn.close();
    }

    public void delete(Task task) throws SQLException {
        String sql = "DELETE FROM task WHERE id=?";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setLong(1, task.getID());
        statement.executeUpdate();
        conn.close();
    }

    public ArrayList<Task> getAll() throws SQLException {
        Task task;
        ArrayList<Task> listtask=new ArrayList<Task>();
        HashMap<Long,Integer> usertask=new HashMap<Long, Integer>();
        String sql = "SELECT * FROM task";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        ResultSet result = statement.executeQuery();
        while (result.next()) {
            long id=result.getInt("id");
            String description = result.getString("description");
            int userid=result.getInt("userid");
            Date opendate=result.getDate("opendate");
            Date deadline=result.getDate("deadline");
            int priority=result.getInt("priority");
            task = new Task(description,null,opendate,deadline,priority);
            task.setID(id);
            usertask.put(id,userid);
            listtask.add(task);
        }
        conn.close();
        Userdao userdao=new Userdao();
        for(Task task1:listtask){
            Integer currentid=usertask.get(task1.getID());
            task1.setUser(userdao.read(currentid.intValue()));
        }
        return listtask;
    }

    public ArrayList<Task> getAllbyUser(long userid) throws SQLException {
        Task task;
        ArrayList<Task> listtask=new ArrayList<Task>();
        HashMap<Long,Long> usertask=new HashMap<Long, Long>();
        String sql = "SELECT * FROM task WHERE userid=?";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setLong(1, userid);
        ResultSet result = statement.executeQuery();
        while (result.next()) {
            long id=result.getInt("id");
            String description = result.getString("description");
            Date opendate=result.getDate("opendate");
            Date deadline=result.getDate("deadline");
            int priority=result.getInt("priority");
            task = new Task(description,null,opendate,deadline,priority);
            task.setID(id);
            usertask.put(id,userid);
            listtask.add(task);
        }
        conn.close();
        Userdao userdao=new Userdao();
        for(Task task1:listtask){
            Long currentid=usertask.get(task1.getID());
            task1.setUser(userdao.read(currentid.intValue()));
        }
        return listtask;
    }
}
