package com.lab3.server;

import com.lab3.utils.ServerAddress;
import org.apache.log4j.Logger;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.LinkedList;


public class ClientInitializer implements Runnable{
    private int serverPort;
    private ServerAddress clientAddress;
    private int delay;
    private LinkedHashSet<ServerAddress> clients;
    private LinkedList<FileQueue> fileQueues;
    private static final Logger log=Logger.getLogger(ClientInitializer.class);

    public ClientInitializer(int serverPort,ServerAddress clientAddress, LinkedList<FileQueue> fileQueues, LinkedHashSet<ServerAddress> clients){
        this.serverPort=serverPort;
        this.clientAddress=clientAddress;
        this.delay=2000;
        this.clients=clients;
        this.fileQueues=fileQueues;
    }

    public void run(){
        Iterator<ServerAddress> clientiterator=clients.iterator();
        while (clientiterator.hasNext()){
            if(clientiterator.next().equals(clientAddress))
                return;
        }
        try {
            Socket client = new Socket();
            client.connect(new InetSocketAddress(clientAddress.getHost(), clientAddress.getPort()), delay);
            log.info("Initializing client host: "+clientAddress.getHost()+" port: "+Integer.toString(clientAddress.getPort()));
            OutputStream outToServer = client.getOutputStream();
            DataOutputStream out =
                    new DataOutputStream(outToServer);
            out.writeInt(serverPort);
            out.writeInt(clients.size());
            for (ServerAddress sa : clients){
                out.writeUTF(sa.getHost());
                out.writeInt(sa.getPort());
            }
            out.writeInt(fileQueues.size());
            for (FileQueue fqueue : fileQueues) {
                out.writeInt(fqueue.QueueSize());
                out.writeUTF(fqueue.GetPath());
                Iterator<ServerAddress> addressIterator = fqueue.GetQueueIterator();
                while (addressIterator.hasNext()){
                    ServerAddress nextAddress=addressIterator.next();
                    out.writeUTF(nextAddress.getHost());
                    out.writeInt(nextAddress.getPort());
                }
            }
        }
        catch (IOException io){
            io.printStackTrace();
        }
    }
}
