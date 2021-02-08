/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.servlets;

import com.lab5.dao.Taskdao;
import com.lab5.dao.Userdao;
import com.lab5.model.Task;
import com.lab5.model.User;
import com.lab8.dao.JDBCXmlAdapter;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author nik-u
 */
@WebServlet("/output/xml")
public class GetXMLTask extends HttpServlet {

    private static final long serialVersionUID = 2123123L;

	@Override
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
	    try {
                response.setContentType("text/xml");
                JDBCXmlAdapter adapter = new JDBCXmlAdapter();
                ByteArrayOutputStream out = adapter.getXmlDataFromDatabase();
                byte[] data = out.toByteArray();
                response.setContentLength(data.length);
                OutputStream os = response.getOutputStream();
                os.write(data, 0, data.length);
                os.flush();
                } catch (Exception e) {
                    e.printStackTrace();
                }
	}

}
