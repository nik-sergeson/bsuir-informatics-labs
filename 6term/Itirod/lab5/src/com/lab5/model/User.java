package com.lab5.model;


public class User {
    private long ID=-1;
    private String login;
    private String name;
    private String email;
    private String password;

    public long getID() {
        return ID;
    }

    public void setID(long ID) {
        this.ID = ID;
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public User(String login,String name, String email, String password){
        this.login=login;
        this.name=name;
        this.email=email;
        this.password=password;
    }

    public User(){
        this.login="";
        this.name="";
        this.email="";
        this.password="";
    }
}
