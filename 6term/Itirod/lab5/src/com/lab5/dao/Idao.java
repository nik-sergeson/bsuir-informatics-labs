package com.lab5.dao;

import java.sql.SQLException;
import java.util.List;


public interface Idao <T> {
    public void create(T obj) throws SQLException;
    public void delete(T obj) throws SQLException;
    public T read(long id) throws SQLException;
    public void update(T obj) throws SQLException;
    public List<T> getAll() throws SQLException;
}
