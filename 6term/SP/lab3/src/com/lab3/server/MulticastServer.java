package com.lab3.server;

import com.lab3.utils.ServerAddress;
import org.apache.log4j.Logger;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.*;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.LinkedList;


public class MulticastServer extends ReserveServer {

    private BroadCast broadCast;
    private int TCPport;
    private static final Logger log=Logger.getLogger(MulticastServer.class);
    private MulticastServerUDPListener multicastServerUDPListener;

    public MulticastServer(IServerConnected mainapp,int UDPport) throws IOException {
        serverSocket = new ServerSocket(0);
        this.TCPport=serverSocket.getLocalPort();
        appAddress=new ServerAddress(InetAddress.getLocalHost().getHostAddress(), TCPport);
        this.mainapp = mainapp;
        this.becameMainServer = true;
        this.UDPport=UDPport;
        log.info("Starting main server on host: "+ InetAddress.getLocalHost().getHostAddress()+" UDP port: "+Integer.toString(UDPport)+" TCP port: "+Integer.toString(TCPport));
        multicastServerUDPListener=new MulticastServerUDPListener(UDPport,TCPport, clients, fileQueues, this);
        new Thread(multicastServerUDPListener).start();
    }

    public MulticastServer(LinkedList<FileQueue> fileQueues,LinkedHashSet<ServerAddress> clients,IServerConnected mainapp, int UDPport) throws IOException {
        this(mainapp, UDPport);
        this.fileQueues=fileQueues;
        this.clients=clients;
        multicastServerUDPListener.setClients(clients);
        multicastServerUDPListener.setFileQueues(fileQueues);
        new Thread(new BroadCast(new LinkedHashSet<ServerAddress>(clients), new ServerAddress(InetAddress.getLocalHost().getHostAddress(), serverSocket.getLocalPort()), RequestType.Recieve_Server_Address, this));
    }

    public MulticastServer(LinkedList<FileQueue> fileQueues,LinkedHashSet<ServerAddress> clients,IServerConnected mainapp, ServerAddress oldSever, int UDPport) throws IOException {
        this(fileQueues, clients, mainapp, UDPport);
        for(FileQueue fq:fileQueues){
            if(fq.HasClient(oldSever))
                fq.UpdateClient(oldSever, appAddress);
        }
        broadCast=new BroadCast(new LinkedHashSet<ServerAddress>(clients), oldSever, RequestType.Remove_Client, this);
        new Thread(broadCast).run();
    }

    @Override
    public ServerAddress GetRemoteServerAddress(){
        return appAddress;
    }

    @Override
    public ServerAddress GetLocalServerAddress(){
        return GetRemoteServerAddress();
    }

    @Override
    public void Stop() throws InterruptedException, IOException {
        Iterator<ServerAddress> clientIterator=clients.iterator();
        turnOn=false;
        log.info("Stoping main server");
        new Thread(new BroadCast(clients, new ServerAddress(InetAddress.getLocalHost().getHostAddress(), TCPport), RequestType.Remove_Client, this)).start();
        synchronized (this) {
            multicastServerUDPListener.Stop();
            serverSocket.close();
            if (clientIterator.hasNext()) {
                Socket client = null;
                ServerAddress nextServer=clientIterator.next();
                client = new Socket(nextServer.getHost(), nextServer.getPort());
                OutputStream outToServer = client.getOutputStream();
                DataOutputStream out =
                        new DataOutputStream(outToServer);
                out.writeInt(RequestType.Became_Main_Server.ordinal());
                client.close();
                appAddress=nextServer;
                //mainapp.Disconect();
            }
        }
    }

    @Override
    public void run() {
        ServerAddress clientAddress=new ServerAddress("",  0);
        FileQueue fileQueue;
        RequestType requestType;
        String path;
        while (turnOn) {
            try {
                Socket server = serverSocket.accept();
                synchronized (this) {
                    DataInputStream in = new DataInputStream(server.getInputStream());
                    requestType = RequestType.values()[in.readInt()];
                    clientAddress=new ServerAddress(in.readUTF(), in.readInt());
                    log.info("Client "+clientAddress.getHost()+" "+Integer.toString(clientAddress.getPort())+" sent request");
                    if (requestType == RequestType.Remove_Client) {
                        clients.remove(clientAddress);
                        broadCast = new BroadCast(clients, new ServerAddress(clientAddress), RequestType.Remove_Client, this);
                        new Thread(broadCast).start();
                    }
                    else if (requestType == RequestType.Remove_From_File_Queue) {
                        path=in.readUTF();
                        broadCast = new BroadCast(clients, path, new ServerAddress(clientAddress), RequestType.Remove_From_File_Queue, this);
                        new Thread(broadCast).start();
                        fileQueue = FindFileQueue(path);
                        if (fileQueue != null) {
                            fileQueue.Remove(clientAddress);
                            if (fileQueue.QueueSize() == 0)
                                fileQueues.remove(fileQueue);
                        }
                    }
                    else if(requestType==RequestType.Is_File_Opened){
                        path=in.readUTF();
                        fileQueue = FindFileQueue(path);
                        DataOutputStream out =
                                new DataOutputStream(server.getOutputStream());
                        if (fileQueue != null)
                            out.writeInt(ResponseType.True.ordinal());
                        else
                            out.writeInt(ResponseType.False.ordinal());
                    }
                    else if (requestType==RequestType.Get_Access_To_File) {
                        path=in.readUTF();
                        fileQueue = FindFileQueue(path);
                        DataOutputStream out =
                                new DataOutputStream(server.getOutputStream());
                        if (fileQueue != null) {
                            if (fileQueue.GetFirst().equals(clientAddress))
                                out.writeInt(ResponseType.Accepted.ordinal());
                            else
                                out.writeInt(ResponseType.Rejected.ordinal());
                        } else
                            out.writeInt(ResponseType.Rejected.ordinal());
                    }
                    else if(requestType==RequestType.Add_To_File_Queue) {
                        path=in.readUTF();
                        broadCast = new BroadCast(clients, path, new ServerAddress(clientAddress), RequestType.Add_To_File_Queue, this);
                        new Thread(broadCast).start();
                        fileQueue = FindFileQueue(path);
                        if (fileQueue == null) {
                            fileQueue = new FileQueue(path);
                            fileQueues.addLast(fileQueue);
                        }
                        fileQueue.Insert(clientAddress);
                    }
                    server.close();
                }
            } catch (SocketTimeoutException s) {
                System.out.println("Socket timed out!");
                break;
            }
            catch (SocketException se){
                return;
            }
            catch (IOException e) {
                e.printStackTrace();
                break;
            }
        }

    }
}

