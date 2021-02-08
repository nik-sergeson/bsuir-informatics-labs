package com.lab2.FileIO;

import org.apache.log4j.Logger;

import java.io.*;


public class Serializator<T extends Serializable> {

    public static final Logger log=Logger.getLogger(Serializator.class);

    public void WriteObject(T object,String path) throws IOException {
        ObjectOutputStream out=new ObjectOutputStream(new FileOutputStream(path));
        out.writeObject(object);
        out.close();
        log.info("object of class "+object.getClass().getName()+" serialized");
    }

    public T ReadObject(String path) throws IOException, ClassNotFoundException {
        ObjectInputStream in=new ObjectInputStream(new FileInputStream(path));
        T object=(T)in.readObject();
        in.close();
        log.info("object of class "+object.getClass().getName()+" read");
        return object;
    }
}
