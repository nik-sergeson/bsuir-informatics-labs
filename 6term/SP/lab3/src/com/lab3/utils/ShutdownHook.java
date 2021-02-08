package com.lab3.utils;


public class ShutdownHook extends Thread {
    private IShutDown shudownactor;

    public  ShutdownHook(IShutDown shudownactor){
        this.shudownactor=shudownactor;
    }

    public void run()
    {
        shudownactor.ShutDownAction();
    }
}
