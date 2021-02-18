package com.lab5;

import com.lab5.dao.Taskdao;
import com.lab5.dao.Userdao;
import com.lab5.model.Task;
import com.lab5.model.User;

import java.sql.SQLException;
import java.util.Date;


public class Test {
    public static void main(String[] args){
        User nik=new User("nik","nik","nik","nik"),james=new User("james","james","james","james");
        Task test=new Task("test",nik,new Date(5000000),1);
        Userdao userdao=new Userdao();
        Taskdao taskdao=new Taskdao();
        try {
            taskdao.getAll();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
