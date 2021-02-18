package com.lab3.server;

import com.lab3.utils.ServerAddress;

import java.util.Iterator;
import java.util.LinkedList;


public class FileQueue {
    private String filename;
    private LinkedList<ServerAddress> clientqueue;

    public FileQueue(String filename){
        this.filename=filename;
        clientqueue =new LinkedList<ServerAddress>();
    }

    public void Insert(ServerAddress serverAddress){
        clientqueue.add(serverAddress);
    }

    public void Remove(ServerAddress serverAddress) {
        clientqueue.remove(serverAddress);
    }

    public ServerAddress GetFirst(){
        if(clientqueue.size()>0)
            return clientqueue.getFirst();
        else
            return null;
    }

    public boolean HasClient(ServerAddress client){
        Iterator<ServerAddress> clientiterator=clientqueue.iterator();
        while (clientiterator.hasNext()){
            if(clientiterator.next().equals(client))
                return true;
        }
        return false;
    }

    public void UpdateClient(ServerAddress old, ServerAddress newAddress){
        Iterator<ServerAddress> clientiterator=clientqueue.iterator();
        while (clientiterator.hasNext()){
            ServerAddress nextCl=clientiterator.next();
            if(nextCl.equals(old)){
                nextCl.setHost(newAddress.getHost());
                nextCl.setPort(newAddress.getPort());
            }
        }
    }

    public String GetPath(){
        return filename;
    }

    public int QueueSize(){
        return clientqueue.size();
    }

    public Iterator<ServerAddress> GetQueueIterator(){
        return clientqueue.iterator();
    }
}

