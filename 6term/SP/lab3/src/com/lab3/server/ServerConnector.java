package com.lab3.server;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.ByteBuffer;


public class ServerConnector implements Runnable {
    private boolean turnOn;
    private int clientPort;
    private int delay;
    private int UDPport;
    private String broadCastHost;

    public ServerConnector(int clientPort,int UDPport, String broadCastHost){
        turnOn=true;
        this.clientPort=clientPort;
        this.UDPport=UDPport;
        delay=200;
        this.broadCastHost=broadCastHost;
    }

    public void Stop(){
        turnOn=false;
    }

    public void run(){
        ByteBuffer dbuf = ByteBuffer.allocate(8);
        dbuf.putInt(RequestType.Connect_To_Server.ordinal());
        dbuf.putInt(clientPort);
        byte[] buffer = dbuf.array();
        try {
            DatagramSocket dsocket = new DatagramSocket();
            dsocket.setBroadcast(true);
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length, InetAddress.getByName(broadCastHost), UDPport);
            while (turnOn) {
                dsocket.send(packet);
                Thread.sleep(delay);
            }
            dsocket.close();
        }
        catch (IOException ex){
            ex.printStackTrace();
        }
        catch (InterruptedException ix){
            ix.printStackTrace();
        }
    }
}
