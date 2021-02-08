<%@page import="java.io.IOException"%>
<%@page import="java.io.FileInputStream"%>
<%@page import="java.util.ArrayList"%>
<%@page import="java.sql.SQLException"%>
<%@page import="java.util.LinkedList"%>
<%@page import="com.lab5.dao.Taskdao"%>
<%@page import="com.lab5.model.Task"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ taglib prefix="own" uri="WEB-INF/custom.tld"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Task Page</title>
    </head>
    <body>
         <%
        Taskdao tdao = new Taskdao();
        ArrayList<Task> list = null;
        try {
            list = new ArrayList<Task>(tdao.getAll());
        } catch (SQLException e) {
            list = new ArrayList<Task>();
        }
        
    %>

    <own:iterator list="<%= list %>" item = "task">
        <own:task task="${task}"/>
    </own:iterator>
    </body>
</html>
