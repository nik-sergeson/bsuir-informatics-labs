package com.lab3.accessutils;

import java.io.IOException;


public abstract class QueueHelper {

    protected String path;

    public QueueHelper(String path){
        this.path=path;
    }

    public abstract void AppendToQueue() throws IOException;
    public abstract boolean AccessGranted() throws IOException;
    public abstract void DequeFromQueue() throws IOException;
    public abstract boolean FileIsOpened() throws IOException;
}
