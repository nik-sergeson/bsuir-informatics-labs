package com.lab3.utils;


public class ServerAddress {
    private int port;
    private String host;

    public ServerAddress(String host, int port){
        this.port=port;
        this.host=host;
    }

    public ServerAddress(ServerAddress serverAddress){
        this.host=serverAddress.getHost();
        this.port=serverAddress.getPort();
    }

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    @Override
    public boolean equals(Object serverAddress){
        ServerAddress address=(ServerAddress)serverAddress;
        return this.host.equals(address.getHost()) && this.port==address.getPort();
    }
}
