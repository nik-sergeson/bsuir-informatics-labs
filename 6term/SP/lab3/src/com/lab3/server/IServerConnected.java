package com.lab3.server;

import com.lab3.utils.ServerAddress;


public interface IServerConnected {
    void Switch(ReserveServer reserveServer);
    ServerAddress GetServerAddress();
    ServerAddress GetLocalAddress();
    void Disconect();
}
