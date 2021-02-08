package com.lab5.dao;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public final class Settings {
    static final String DATABASE = "jdbc:mysql://localhost:3306/bugtracker"
            + "?autoReconnect=true&useUnicode=true&characterEncoding=utf8";
    static final String USERNAME = "nik";
    static final String DRIVERNAME = "com.mysql.jdbc.Driver";

    public static Connection getConnection() throws SQLException {
        try {
            Class.forName(DRIVERNAME);
            return DriverManager.getConnection(DATABASE, USERNAME, null);
        } catch (ClassNotFoundException e) {
            System.err.println(e.toString());
            return null;
        }
    }
}
