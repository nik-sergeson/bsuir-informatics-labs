package com.lab3.server;

import com.lab3.utils.IReferenceCounter;
import com.lab3.utils.ServerAddress;
import org.apache.log4j.Logger;
import sun.rmi.runtime.Log;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.Iterator;
import java.util.LinkedHashSet;


public class BroadCast implements Runnable{
    private LinkedHashSet<ServerAddress> clients;
    private RequestType broadCastType;
    private String path;
    private ServerAddress activeClient;
    private boolean finished;
    private IReferenceCounter referenceCounter;
    private int connectionDelay;
    private static final Logger log=Logger.getLogger(BroadCast.class);

    public boolean IsFinished(){
        return finished;
    }

    public BroadCast(LinkedHashSet<ServerAddress> clients, ServerAddress client, RequestType requestType, IReferenceCounter referenceCounter){
        this.clients=clients;
        this.activeClient =client;
        this.broadCastType=requestType;
        this.referenceCounter=referenceCounter;
        this.connectionDelay=1500;
        this.finished=false;
    }

    public BroadCast(LinkedHashSet<ServerAddress> clients, String path, ServerAddress client, RequestType requestType,IReferenceCounter referenceCounter){
        this(clients, client, requestType, referenceCounter);
        this.path=path;
    }

    public void run(){
        referenceCounter.Add();
        Iterator<ServerAddress> it=clients.iterator();
        ServerAddress nextClient;
        while (it.hasNext()){
            Socket clientSocket = null;
            nextClient=it.next();
            log.info("Broadcasting to host"+nextClient.getHost()+" port: "+Integer.toString(nextClient.getPort()));
            synchronized (nextClient) {
                try {
                    clientSocket = new Socket();
                    clientSocket.connect(new InetSocketAddress(nextClient.getHost(), nextClient.getPort()), connectionDelay);
                    OutputStream outToServer = clientSocket.getOutputStream();
                    DataOutputStream out = new DataOutputStream(outToServer);
                    out.writeInt(broadCastType.ordinal());
                    out.writeUTF(activeClient.getHost());
                    out.writeInt(activeClient.getPort());
                    if (broadCastType == RequestType.Add_To_File_Queue || broadCastType==RequestType.Get_Access_To_File|| broadCastType==RequestType.Remove_From_File_Queue) {
                        out.writeUTF(path);
                    }
                    clientSocket.close();
                } catch (IOException e) {
                    continue;
                }
            }
        }
        finished=true;
        referenceCounter.Remove();
    }
}
