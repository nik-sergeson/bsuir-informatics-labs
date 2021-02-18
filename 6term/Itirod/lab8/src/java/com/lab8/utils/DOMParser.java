/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import com.lab5.model.*;
import com.lab8.utils.IXmlUtil;
import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;


public class DOMParser implements IXmlUtil {
    
    public ArrayList<Task> loadTasks(InputStream in) {
        ArrayList<Task> tasks = null;
        Document doc = this.getDocument(in);
        try {
            tasks = this.parseDocument(doc);
        } catch (ParseException e) {
            e.printStackTrace();
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
    
    private Document getDocument(InputStream in) {
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        Document doc = null;
        try {        
            DocumentBuilder db = dbf.newDocumentBuilder();
            doc = db.parse(in);
        } catch (ParserConfigurationException ex) {
            Logger.getLogger(DOMParser.class.getName()).log(Level.SEVERE, null, ex);
        } catch (SAXException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return doc;
    }
    
    private ArrayList<Task> parseDocument(Document doc) throws ParseException {
        ArrayList<Task> tasks=new ArrayList<Task>();
        Element root = doc.getDocumentElement();
        NodeList nList = root.getElementsByTagName("com.lab5.model.Task");
        for (int temp = 0; temp < nList.getLength(); temp++) { 
            Node nNode = nList.item(temp);
            Element eElement = (Element) nNode;
            long id=Long.parseLong(eElement.getElementsByTagName("ID").item(0).getTextContent());
            String descr=eElement.getElementsByTagName("description").item(0).getTextContent();
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            Date opendate=sdf.parse(eElement.getElementsByTagName("opendate").item(0).getTextContent());
            Date deadline=sdf.parse(eElement.getElementsByTagName("deadline").item(0).getTextContent());
            int priority=Integer.parseInt(eElement.getElementsByTagName("priority").item(0).getTextContent());
            eElement = (Element) eElement.getElementsByTagName("user").item(0);
            long userid=Long.parseLong(eElement.getElementsByTagName("ID").item(0).getTextContent());
            String name=eElement.getElementsByTagName("name").item(0).getTextContent();
            String login=eElement.getElementsByTagName("login").item(0).getTextContent();
            String email=eElement.getElementsByTagName("email").item(0).getTextContent();
            String password=eElement.getElementsByTagName("password").item(0).getTextContent();
            User reporter=new User(login,name,email,password);
            reporter.setID(userid);
            Task task=new Task(descr,reporter,opendate,deadline,priority);
            tasks.add(task);
	}
    return tasks;
    }
    
}
