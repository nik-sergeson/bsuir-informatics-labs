/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.utils;

import com.lab5.model.Task;
import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.SAXException;


public class SaxParser implements IXmlUtil {

    public ArrayList<Task> loadTasks(InputStream in) {
        ArrayList<Task> tasks = null;
        try {
            tasks = this.parseDocument(in);
        } catch (Exception ex) {
        }
        return tasks;
    }
    
    public void saveTasks(OutputStream out, ArrayList<Task> tasks) throws FileNotFoundException, IOException {
        XStream xs = new XStream(new DomDriver());
        xs.toXML(tasks,out);
        out.close();
    }
    
    public String saveTasks(ArrayList<Task> tasks) {
        XStream xs = new XStream(new DomDriver());
        return xs.toXML(tasks);
    }
    
    private ArrayList<Task> parseDocument(InputStream in) {
        SAXParserFactory spf = SAXParserFactory.newInstance();
        ArrayList<Task> tasks = null;
        try {
            SAXParser sp = spf.newSAXParser();
            TasksSAXUtil helper = new TasksSAXUtil();
            sp.parse(in, helper);
            tasks = helper.getTasks();
        } catch (SAXException se) {
            se.printStackTrace();
        } catch (ParserConfigurationException pce) {
            pce.printStackTrace();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return tasks;
    }

}
