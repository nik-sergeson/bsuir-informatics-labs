package com.lab3.server;

import com.lab3.utils.IReferenceCounter;
import com.lab3.utils.ServerAddress;
import org.apache.log4j.Logger;

import java.io.*;
import java.net.*;
import java.nio.ByteBuffer;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.Random;


public class ReserveServer implements Runnable, IReferenceCounter{
    protected ServerSocket serverSocket;
    protected LinkedList<FileQueue> fileQueues;
    protected LinkedHashSet<ServerAddress> clients;
    protected ServerAddress appAddress;
    protected IServerConnected mainapp;
    protected boolean turnOn;
    protected boolean becameMainServer;
    protected int delay;
    protected int broadcastRefCount;
    protected int connectionDelay;
    protected  String broadCastHost="255.255.255.255";
    private ServerAddress serverAddress;
    protected int UDPport;
    private static final Logger log=Logger.getLogger(ReserveServer.class);

    public ReserveServer() throws UnknownHostException {
        fileQueues=new LinkedList<FileQueue>();
        clients=new LinkedHashSet<ServerAddress>();
        turnOn=true;
        becameMainServer=false;
        broadcastRefCount=0;
        delay=100;
        Random random=new Random();
        connectionDelay=1200+ random.nextInt(1000);
        appAddress=new ServerAddress(InetAddress.getLocalHost().getHostAddress(),0);
    }

    public ReserveServer(IServerConnected mainapp, int serverUdpPort) throws IOException {
        this();
        this.mainapp=mainapp;
        this.serverAddress=new ServerAddress(broadCastHost, 0);
        this.UDPport=serverUdpPort;
    }

    public FileQueue FindFileQueue(String path){
        for(FileQueue x:fileQueues){
            if(x.GetPath().equals(path))
                return x;
        }
        return null;
    }

    public ServerAddress GetRemoteServerAddress(){
        return serverAddress;
    }

    public ServerAddress GetLocalServerAddress(){return  appAddress;}

    public void Stop() throws InterruptedException, IOException {
        log.info("Stopping server "+appAddress.getHost()+" "+Integer.toString(appAddress.getPort()));
        if(turnOn) {
            turnOn = false;
            synchronized (this){
                serverSocket.close();
            }
        }
        mainapp.Disconect();
        Socket client = new Socket();
        client.connect(new InetSocketAddress(serverAddress.getHost(), serverAddress.getPort()), connectionDelay);
        OutputStream outToServer = client.getOutputStream();
        DataOutputStream out =
                new DataOutputStream(outToServer);
        out.writeInt(RequestType.Remove_Client.ordinal());
        out.writeUTF(appAddress.getHost());
        out.writeInt(appAddress.getPort());
        client.close();
    }

    public boolean BroadcastFinished(){
        return  broadcastRefCount==0;
    }


    private boolean Initialize() throws IOException {
        int size=0, queueSize;
        String path;
        Socket server_connection = null;
        ServerConnector serverConnector=null;
        try {
            serverSocket = new ServerSocket(0);
            appAddress.setPort(serverSocket.getLocalPort());
            serverConnector=new ServerConnector(appAddress.getPort(), UDPport, broadCastHost);
            log.info("Listening to "+Integer.toString(appAddress.getPort())+ " port");
            new Thread(serverConnector).start();
            log.info("Searching for main server");
            serverSocket.setSoTimeout(connectionDelay);
            server_connection=serverSocket.accept();
        }
        catch (SocketTimeoutException ste){
            serverConnector.Stop();
            log.info("Main server doesnt excist");
            StartMulticastServer();
            serverSocket.close();
            return false;
        }
        catch (IOException e) {
            serverConnector.Stop();
            log.info("Main server doesnt excist");
            StartMulticastServer();
            serverSocket.close();
            return false;
        }
        try {
            serverConnector.Stop();
            log.info("Initializing server");
            DataInputStream in = new DataInputStream(server_connection.getInputStream());
            serverAddress.setPort(in.readInt());
            serverAddress.setHost(server_connection.getInetAddress().getHostAddress());
            size=in.readInt();
            for(int i=1;i<=size;i++)
                clients.add(new ServerAddress(in.readUTF(), in.readInt()));
            size=in.readInt();
            for(int i=1;i<=size;i++){
                queueSize=in.readInt();
                path=in.readUTF();
                FileQueue fqueue=new FileQueue(path);
                for(int j=1;j<=queueSize;j++)
                    fqueue.Insert(new ServerAddress(in.readUTF(), in.readInt()));
                fileQueues.add(fqueue);
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            server_connection.close();
        }
        return true;
    }

    public void StartMulticastServer() throws IOException {
        if(!becameMainServer) {
            MulticastServer multicastServer = null;
            multicastServer = new MulticastServer(this.fileQueues, this.clients, mainapp, UDPport);
            mainapp.Switch(multicastServer);
            new Thread(multicastServer).start();
            turnOn=false;
        }
    }

    public void run() {
        ServerAddress requestclient;
        FileQueue fileQueue;
        String path;
        RequestType requestType;
        try {
            if(!Initialize())
                return;
            serverSocket.setSoTimeout(0);
        } catch (IOException e) {
            e.printStackTrace();
        }
        while (turnOn) {
            try {
                Socket server = serverSocket.accept();
                synchronized (this) {
                    DataInputStream in = new DataInputStream(server.getInputStream());
                    log.info("Get request from server :"+serverAddress.getHost()+" "+Integer.toString(serverAddress.getPort()));
                    requestType = RequestType.values()[in.readInt()];
                    if (requestType == RequestType.Add_Client) {
                        requestclient = new ServerAddress(in.readUTF(), in.readInt());
                        clients.add(requestclient);
                    }
                    else if(requestType==RequestType.Remove_Client) {
                        requestclient = new ServerAddress(in.readUTF(), in.readInt());
                        clients.remove(requestclient);
                        for(FileQueue fq:fileQueues) {
                            fq.Remove(requestclient);
                            break;
                        }
                    }
                    else if(requestType==RequestType.Became_Main_Server){
                        becameMainServer = true;
                    }
                    else if (requestType == RequestType.Remove_From_File_Queue) {
                        requestclient = new ServerAddress(in.readUTF(), in.readInt());
                        path = in.readUTF();
                        fileQueue = FindFileQueue(path);
                        if (fileQueue != null) {
                            fileQueue.Remove(requestclient);
                            if (fileQueue.QueueSize() == 0)
                                fileQueues.remove(fileQueue);
                            }
                        }
                    else if (requestType==RequestType.Add_To_File_Queue) {
                        requestclient = new ServerAddress(in.readUTF(), in.readInt());
                        path = in.readUTF();
                        fileQueue = FindFileQueue(path);
                        if (fileQueue == null) {
                            fileQueue = new FileQueue(path);
                            fileQueues.addLast(fileQueue);
                        }
                        fileQueue.Insert(requestclient);
                    }
                    else if(requestType== RequestType.Recieve_Server_Address){
                        serverAddress.setHost(in.readUTF());
                        serverAddress.setPort(in.readInt());
                    }
                    server.close();
                    if (becameMainServer) {
                        clients.remove(appAddress);
                        if (turnOn == true) {
                            MulticastServer multicastServer = new MulticastServer(this.fileQueues, this.clients, mainapp, appAddress, UDPport);
                            mainapp.Switch(multicastServer);
                            new Thread(multicastServer).start();
                        } else {
                            Iterator<ServerAddress> portIterator = clients.iterator();
                            if (portIterator.hasNext()) {
                                BroadCast broadCast = new BroadCast(this.clients, appAddress, RequestType.Remove_Client, this);
                                broadCast.run();
                                ServerAddress nextaddress=portIterator.next();
                                Socket client = new Socket(nextaddress.getHost(), nextaddress.getPort());
                                OutputStream outToServer = client.getOutputStream();
                                DataOutputStream out =
                                        new DataOutputStream(outToServer);
                                out.writeInt(RequestType.Became_Main_Server.ordinal());
                                client.close();
                            }
                        }
                        turnOn = false;
                    }
                }
            } catch (SocketTimeoutException s) {
                System.out.println("Socket timed out!");
                break;
            }catch (SocketException m){
                return;
            }
            catch (IOException e) {
                e.printStackTrace();
                break;
            }
        }
    }

    public synchronized void Add() {
        ++broadcastRefCount;
    }

    public synchronized void Remove() {
        --broadcastRefCount;
    }
}
