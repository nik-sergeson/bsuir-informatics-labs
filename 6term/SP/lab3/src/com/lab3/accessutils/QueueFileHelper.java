package com.lab3.accessutils;

import com.lab3.utils.PIDHelper;

import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;
import java.util.ArrayList;


public class QueueFileHelper extends QueueHelper {
    private int pidsize;

    public QueueFileHelper(String path, int pidsize){
        super(path);
        this.pidsize=pidsize;
    }

    public void AppendToQueue() throws IOException {
        FileLock lock=null;
        File f = new File(path);
        RandomAccessFile raf=null;
        if(f.exists() && !f.isDirectory()) {
            try {
                raf = new RandomAccessFile(f, "rw");
                FileChannel channel = raf.getChannel();
                lock = channel.lock();
                raf.seek(raf.length());
                raf.writeLong(PIDHelper.getPID());
            } finally {
                if(lock!=null)
                    lock.release();
                raf.close();
            }
        }
        else {
            AppendToNewQueue();
        }
    }

    private void AppendToNewQueue() throws IOException {
        RandomAccessFile raf=null;
        try {
            raf = new RandomAccessFile(path, "rw");
            raf.seek(raf.length());
            raf.writeLong(PIDHelper.getPID());
        }
        finally {
            raf.close();
        }
    }

    public boolean AccessGranted() throws IOException {
        FileLock lock=null;
        File f = new File(path);
        long pid=0;
        RandomAccessFile raf=null;
        if(f.exists() && !f.isDirectory()&&f.length()!=0) {
            try {
                raf = new RandomAccessFile(f, "rw");
                FileChannel channel = raf.getChannel();
                lock = channel.lock();
                raf.seek(0);
                pid=raf.readLong();
            } finally {
                if(lock!=null)
                    lock.release();
                raf.close();
            }
            return pid==PIDHelper.getPID();
        }
        return pid==PIDHelper.getPID();
    }

    public boolean FileIsOpened(){
        File f=new File(path);
        if(f.exists()&&f.length()!=0)
            return true;
        else
            return false;
    }

    public void DequeFromQueue() throws IOException {
        FileLock lock=null;
        RandomAccessFile raf=null;
        FileChannel channel=null;
        File f = new File(path);
        if(f.exists() && !f.isDirectory()&&f.length()!=0) {
            try {
                raf = new RandomAccessFile(f, "rw");
                channel = raf.getChannel();
                lock = channel.lock();
                if(raf.length()!=pidsize) {
                    ArrayList<Long> vals=new ArrayList<Long>();
                    long curpid= PIDHelper.getPID();
                    int count= (int) (raf.length()/pidsize);
                    raf.seek(0);
                    for(int i=0;i<count;i++){
                        long readpid=raf.readLong();
                        if(readpid==curpid)
                            continue;
                        else
                            vals.add(readpid);
                    }
                    channel.truncate(pidsize);
                    raf.seek(0);
                    for(Long pid:vals)
                        raf.writeLong(pid.longValue());
                }
                else {
                    raf.setLength(0);
                }
            }
            finally {
                if(lock!=null)
                    lock.release();
                raf.close();
            }

        }
    }

}
