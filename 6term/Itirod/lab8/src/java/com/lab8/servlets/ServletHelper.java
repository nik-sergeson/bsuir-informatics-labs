/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.servlets;


import java.text.SimpleDateFormat;
import java.util.Date;
import javax.servlet.http.*;

public class ServletHelper {
  public static String headWithTitle(String title) {
    return("<!DOCTYPE html>\n" +
           "<html>\n" +
           "<head><title>" + title + "</title></head>\n");
  }
  
  public static int getIntParameter(HttpServletRequest request,
                                    String paramName,
                                    int defaultValue) {
    String paramString = request.getParameter(paramName);
    int paramValue;
    try {
      paramValue = Integer.parseInt(paramString);
    } catch(Exception nfe) { 
      paramValue = defaultValue;
    }
    return(paramValue);
  }
  
  public static double getDoubleParameter(HttpServletRequest request,
                                          String paramName,
                                          double defaultValue) {
    String paramString = request.getParameter(paramName);
    double paramValue;
    try {
      paramValue = Double.parseDouble(paramString);
    } catch(Exception nfe) { 
      paramValue = defaultValue;
    }
    return(paramValue);
  }
  
  public static Date getDateParameter(HttpServletRequest request,
                                          String paramName,
                                          Date defaultValue) {
    String paramString = request.getParameter(paramName);
    Date paramValue;
    try {
      paramValue = new SimpleDateFormat("yyyy-MM-dd").parse(paramString);
    } catch(Exception nfe) { 
      paramValue = defaultValue;
    }
    return(paramValue);
  }

  public static String filter(String input) {
    if (!hasSpecialChars(input)) {
      return(input);
    }
    StringBuilder filtered = new StringBuilder(input.length());
    char c;
    for(int i=0; i<input.length(); i++) {
      c = input.charAt(i);
      switch(c) {
        case '<': filtered.append("&lt;"); break;
        case '>': filtered.append("&gt;"); break;
        case '"': filtered.append("&quot;"); break;
        case '&': filtered.append("&amp;"); break;
        default: filtered.append(c);
      }
    }
    return(filtered.toString());
  }

  private static boolean hasSpecialChars(String input) {
    boolean flag = false;
    if ((input != null) && (input.length() > 0)) {
      char c;
      for(int i=0; i<input.length(); i++) {
        c = input.charAt(i);
        switch(c) {
          case '<': flag = true; break;
          case '>': flag = true; break;
          case '"': flag = true; break;
          case '&': flag = true; break;
        }
      }
    }
    return(flag);
  }
  
  private ServletHelper() {}
}

