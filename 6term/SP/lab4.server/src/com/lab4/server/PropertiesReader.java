package com.lab4.server;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;


public class PropertiesReader {

    private String path;

    public PropertiesReader(String path){
        this.path=path;
    }

    public String GetStringProperty(String name) throws IOException {
        Properties property = new Properties();
        FileInputStream fis = new FileInputStream(path);
        property.load(fis);
        String prop = property.getProperty(name);
        fis.close();
        return prop;
    }

    public int GetIntProperty(String name) throws IOException {
        Properties property = new Properties();
        FileInputStream fis = new FileInputStream(path);
        property.load(fis);
        String time = property.getProperty(name);
        fis.close();
        return Integer.parseInt(time);
    }
}
