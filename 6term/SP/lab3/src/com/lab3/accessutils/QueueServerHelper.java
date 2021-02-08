package com.lab3.accessutils;

import com.lab3.server.IServerConnected;
import com.lab3.server.RequestType;
import com.lab3.server.ResponseType;
import com.lab3.utils.ServerAddress;

import java.io.*;
import java.net.InetSocketAddress;
import java.net.Socket;


public class QueueServerHelper extends QueueHelper {

    private int connectionDelay;
    private IServerConnected serverConnected;

    public QueueServerHelper(String path, IServerConnected serverConnected){
        super(path);
        this.serverConnected=serverConnected;
        connectionDelay=15000;
    }

    public void AppendToQueue() throws IOException {
        Socket client = new Socket();
        client.connect(new InetSocketAddress(serverConnected.GetServerAddress().getHost(), serverConnected.GetServerAddress().getPort()), connectionDelay);
        OutputStream outToServer = client.getOutputStream();
        DataOutputStream out =
                new DataOutputStream(outToServer);
        out.writeInt(RequestType.Add_To_File_Queue.ordinal());
        out.writeUTF(serverConnected.GetLocalAddress().getHost());
        out.writeInt(serverConnected.GetLocalAddress().getPort());
        out.writeUTF(path);
        client.close();
    }

    public boolean AccessGranted() throws IOException {
        ResponseType responseType;
        Socket client = new Socket();
        client.connect(new InetSocketAddress(serverConnected.GetServerAddress().getHost(), serverConnected.GetServerAddress().getPort()), connectionDelay);
        OutputStream outToServer = client.getOutputStream();
        DataOutputStream out =
                new DataOutputStream(outToServer);
        out.writeInt(RequestType.Get_Access_To_File.ordinal());
        out.writeUTF(serverConnected.GetLocalAddress().getHost());
        out.writeInt(serverConnected.GetLocalAddress().getPort());
        out.writeUTF(path);
        InputStream inFromServer = client.getInputStream();
        DataInputStream in =
                new DataInputStream(inFromServer);
        responseType=ResponseType.values()[in.readInt()];
        client.close();
        return responseType==ResponseType.Accepted;
    }

    public boolean FileIsOpened() throws IOException {
        ResponseType responseType;
        Socket client = new Socket();
        client.connect(new InetSocketAddress(serverConnected.GetServerAddress().getHost(), serverConnected.GetServerAddress().getPort()), connectionDelay);
        OutputStream outToServer = client.getOutputStream();
        DataOutputStream out =
                new DataOutputStream(outToServer);
        out.writeInt(RequestType.Get_Access_To_File.ordinal());
        out.writeUTF(serverConnected.GetLocalAddress().getHost());
        out.writeInt(serverConnected.GetLocalAddress().getPort());
        out.writeUTF(path);
        InputStream inFromServer = client.getInputStream();
        DataInputStream in =
                new DataInputStream(inFromServer);
        responseType=ResponseType.values()[in.readInt()];
        client.close();
        return responseType==ResponseType.True;
    }

    public void DequeFromQueue() throws IOException {
        Socket client = new Socket();
        client.connect(new InetSocketAddress(serverConnected.GetServerAddress().getHost(), serverConnected.GetServerAddress().getPort()), connectionDelay);
        OutputStream outToServer = client.getOutputStream();
        DataOutputStream out =
                new DataOutputStream(outToServer);
        out.writeInt(RequestType.Remove_From_File_Queue.ordinal());
        out.writeUTF(serverConnected.GetLocalAddress().getHost());
        out.writeInt(serverConnected.GetLocalAddress().getPort());
        out.writeUTF(path);
        client.close();
    }
}
