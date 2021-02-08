/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.dao;

import com.lab5.dao.Taskdao;
import com.lab5.model.Task;
import com.lab8.utils.SaxParser;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.util.ArrayList;


public class JDBCXmlAdapter {
    private Taskdao jdbcDao;
    private Xmldao xmlDao;

    public void setJdbcDao(Taskdao jdbcDao) {
        this.jdbcDao = jdbcDao;
    }

    public void setXmlDao(Xmldao xmlDao) {
        this.xmlDao = xmlDao;
    }

    public Taskdao getJdbcDao() {
        return jdbcDao;
    }

    public Xmldao getXmlDao() {
        return xmlDao;
    }
    
    public JDBCXmlAdapter() {
        this.jdbcDao = new Taskdao();
        this.xmlDao = new Xmldao();
        this.xmlDao.setXmlUtil(new SaxParser());
    }
        
    public void saveXmlDataInDatabase(InputStream in) {
        try {
            this.xmlDao.setIn(in);
            ArrayList<Task> tasks = this.xmlDao.getAll();
            for (Task t : tasks) {
                this.jdbcDao.create(t);
        }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
    
    public ByteArrayOutputStream getXmlDataFromDatabase() {
        ByteArrayOutputStream out = null;
        try {
            ArrayList<Task> tasks = this.jdbcDao.getAll();
            out = new ByteArrayOutputStream();
            this.xmlDao.getXmlUtil().saveTasks(out, tasks);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return out;
    }
}
