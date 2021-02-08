/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.utils;

import com.lab5.model.Task;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;

/**
 *
 * @author nik-u
 */
public interface IXmlUtil {
      public ArrayList<Task> loadTasks(InputStream in) ;
      public void saveTasks(OutputStream out, ArrayList<Task> tasks) throws FileNotFoundException, IOException;
      public String saveTasks(ArrayList<Task> tasks);
}
