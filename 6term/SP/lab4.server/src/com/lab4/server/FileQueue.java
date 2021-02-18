package com.lab4.server;

import java.util.LinkedList;


public class FileQueue {
    private String filename;
    private LinkedList<Long> pidqueue;

    public FileQueue(String filename){
        this.filename=filename;
        pidqueue=new LinkedList<Long>();
    }

    public void InsertPID(long pid){
        int index=pidqueue.indexOf(pid);
        if(index==-1)
            pidqueue.addLast(pid);
    }

    public void RemovePID(long pid){
        int index=pidqueue.indexOf(pid);
        if(index!=-1)
            pidqueue.remove(index);
    }

    public long GetFirst(){
        if(pidqueue.size()>0)
            return pidqueue.getFirst();
        else
            return 0;
    }

    public String GetPath(){
        return filename;
    }

    public int QueueSize(){
        return pidqueue.size();
    }
}
