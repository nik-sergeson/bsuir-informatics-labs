package com.lab3.server;

import com.lab3.utils.IReferenceCounter;
import com.lab3.utils.ServerAddress;
import org.apache.log4j.Logger;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;
import java.nio.ByteBuffer;
import java.util.LinkedHashSet;
import java.util.LinkedList;


public class MulticastServerUDPListener implements Runnable {
    private boolean turnOn;
    private int UDPport, TCPport;
    private int bufferSize;
    private DatagramSocket dsocket;

    public LinkedHashSet<ServerAddress> getClients() {
        return clients;
    }

    public void setClients(LinkedHashSet<ServerAddress> clients) {
        this.clients = clients;
    }

    private LinkedHashSet<ServerAddress> clients;

    public LinkedList<FileQueue> getFileQueues() {
        return fileQueues;
    }

    public void setFileQueues(LinkedList<FileQueue> fileQueues) {
        this.fileQueues = fileQueues;
    }

    private LinkedList<FileQueue> fileQueues;
    private IReferenceCounter referenceCounter;
    private static final Logger log=Logger.getLogger(MulticastServerUDPListener.class);

    public MulticastServerUDPListener(int UDPport, int TCPport, LinkedHashSet<ServerAddress> clients, LinkedList<FileQueue> fileQueues, IReferenceCounter referenceCounter){
        turnOn=true;
        this.UDPport=UDPport;
        this.TCPport=TCPport;
        bufferSize=256;
        this.clients=clients;
        this.fileQueues=fileQueues;
        this.referenceCounter=referenceCounter;
    }

    public void Stop(){
        dsocket.close();
        turnOn=false;
    }

    public void run(){
        dsocket= null;
        int clientPort;
        try {
            dsocket = new DatagramSocket(UDPport);
        } catch (SocketException e) {
            e.printStackTrace();
        }
        while (turnOn) {
            try {
                byte[] buf = new byte[bufferSize];
                DatagramPacket packet = new DatagramPacket(buf, buf.length);
                dsocket.receive(packet);
                ByteBuffer wrapped = ByteBuffer.wrap(packet.getData());
                RequestType requestType=RequestType.values()[wrapped.getInt()];
                clientPort=wrapped.getInt();
                if(requestType==RequestType.Connect_To_Server){
                    ServerAddress connectedClient=new ServerAddress(packet.getAddress().getHostAddress(), clientPort);
                    new Thread(new ClientInitializer(TCPport, connectedClient, fileQueues, new LinkedHashSet<ServerAddress>(clients))).start();
                    BroadCast broadCast = new BroadCast(new LinkedHashSet<ServerAddress>(clients), connectedClient, RequestType.Add_Client, referenceCounter);
                    clients.add(connectedClient);
                    log.info("New client "+packet.getAddress().getHostAddress()+" "+Integer.toString(clientPort)+" connected");
                    new Thread(broadCast).start();
                }
            }
            catch (SocketException sx){
                return;
            }
            catch (IOException ex){
                ex.printStackTrace();
            }
        }
        dsocket.close();
    }
}
