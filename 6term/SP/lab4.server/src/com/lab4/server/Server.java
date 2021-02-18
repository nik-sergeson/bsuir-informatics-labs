package com.lab4.server;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketTimeoutException;
import java.util.ArrayList;
import java.util.LinkedList;


public class Server implements Runnable {
    private ServerSocket serverSocket;
    private LinkedList<FileQueue> fileQueues;

    public Server(int port) throws IOException {
        serverSocket = new ServerSocket(port);
        fileQueues=new LinkedList<FileQueue>();
    }

    public FileQueue FindFileQueue(String path){
        for(FileQueue x:fileQueues){
            if(x.GetPath().equals(path))
                return x;
        }
        return null;
    }

    public void run() {
        while (true) {
            try {
                long pid;
                FileQueue fileQueue;
                String path,request;
                Socket server = serverSocket.accept();
                DataInputStream in = new DataInputStream(server.getInputStream());
                request=in.readUTF();
                String[] parsedrequest=request.split("\\s+");
                path=parsedrequest[0];
                pid = Long.parseLong(parsedrequest[1]);
                DataOutputStream out =
                        new DataOutputStream(server.getOutputStream());
                if(pid<0){
                    pid=Math.abs(pid);
                    fileQueue= FindFileQueue(path);
                    if(fileQueue!=null){
                        fileQueue.RemovePID(pid);
                        if(fileQueue.QueueSize()==0)
                            fileQueues.remove(fileQueue);
                        out.writeUTF(Integer.toString(0));
                    }
                    else
                        out.writeUTF(Integer.toString(1));
                }
                else if(pid==0){
                    fileQueue=FindFileQueue(path);
                    if(fileQueue!=null)
                        out.writeUTF(Long.toString(fileQueue.GetFirst()));
                    else
                        out.writeUTF(Long.toString(0));
                }
                else {
                    fileQueue=FindFileQueue(path);
                    if (fileQueue==null) {
                        fileQueue=new FileQueue(path);
                        fileQueues.addLast(fileQueue);
                    }
                    fileQueue.InsertPID(pid);
                    out.writeUTF(Integer.toString(0));
                }
                server.close();
            } catch (SocketTimeoutException s) {
                System.out.println("Socket timed out!");
                break;
            } catch (IOException e) {
                e.printStackTrace();
                break;
            }
        }

    }

    public static void main(String [] args)
    {
        PropertiesReader pr=new PropertiesReader("D:\\Labs\\labs.6term\\SP\\lab4.server\\src\\com\\lab4\\config.properties");
        try
        {
            int port = pr.GetIntProperty("port");
            new Thread(new Server(port)).start();
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
}
