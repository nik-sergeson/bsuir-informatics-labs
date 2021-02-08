package com.lab5.dao;

import com.lab5.model.Task;
import com.lab5.model.User;

import javax.jws.soap.SOAPBinding;
import java.beans.Statement;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import com.lab5.model.User;

/**
 * Created by nik-u on 21.02.2015.
 */
public class Userdao implements Idao<User> {

    public User read(long id) throws SQLException {
        User user;
        String sql = "SELECT * FROM user WHERE id=?";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setLong(1, id);
        ResultSet result = statement.executeQuery();
        if(result.next()) {
            String login = result.getString("login");
            String name=result.getString("name");
            String emal=result.getString("email");
            String password=result.getString("password");
            user=new User(login,name,emal,password);
            user.setID(id);
        }
        else
            user=null;
        conn.close();
        return user;
    }

    public User readbylogin(String login) throws SQLException {
        User user;
        String sql = "SELECT id, name, email, password FROM user WHERE login=?";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setString(1, login);
        ResultSet result = statement.executeQuery();
        if(result.next()) {
            String name=result.getString("name");
            String emal=result.getString("email");
            String password=result.getString("password");
            user=new User(login,name,emal,password);
            user.setID(result.getInt("id"));
        }
        else
            user=null;
        conn.close();
        return user;
    }

    public void create(User user) throws SQLException {
        String sql = "INSERT INTO user (login, name, email, password) VALUES (?, ?, ?, ?)";
        if(readbylogin(user.getLogin())==null) {
            Connection conn = Settings.getConnection();
            PreparedStatement statement = conn.prepareStatement(sql, com.mysql.jdbc.Statement.RETURN_GENERATED_KEYS);
            statement.setString(1, user.getLogin());
            statement.setString(2, user.getName());
            statement.setString(3, user.getEmail());
            statement.setString(4, user.getPassword());
            statement.executeUpdate();
            ResultSet set = statement.getGeneratedKeys();
            if(set.next())
                user.setID(set.getInt(1));
            conn.close();
        }
    }

    public void update(User user) throws SQLException {
        String sql = "UPDATE user SET login=?, name=?, email=?, password=? WHERE id=?";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setString(1, user.getLogin());
        statement.setString(2, user.getName());
        statement.setString(3, user.getEmail());
        statement.setString(4, user.getPassword());
        statement.setLong(5,user.getID());
        statement.executeUpdate();
        conn.close();
    }

    public void delete(User user) throws SQLException {
        String sql = "DELETE FROM user WHERE id=?";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setLong(1, user.getID());
        statement.executeUpdate();
        sql = "DELETE FROM task WHERE userid=?";
        statement = conn.prepareStatement(sql);
        statement.setLong(1, user.getID());
        statement.executeUpdate();
        conn.close();
    }

    public ArrayList<User> getAll() throws SQLException {
        User user;
        ArrayList<User> users=new ArrayList<User>();
        String sql = "SELECT * FROM user";
        Connection conn=Settings.getConnection();
        PreparedStatement statement = conn.prepareStatement(sql);
        ResultSet result = statement.executeQuery();
        while (result.next()) {
            int id=result.getInt("id");
            String login = result.getString("login");
            String name=result.getString("name");
            String emal=result.getString("email");
            String password=result.getString("password");
            user=new User(login,name,emal,password);
            user.setID(id);
            users.add(user);
        }
        conn.close();
        return users;
    }
}
