package com.lab3.timers;


public class Waiter implements Runnable {
    private  long delay=5000;
    private String path;
    private boolean active=true;
    private IQueueWaiter waiter;

    public Waiter(String path,IQueueWaiter waiter){
        this.path=path;
        this.waiter=waiter;
    }

    public void disable(){
        active=false;
    }

    public void enable(){
        active=true;
    }

    public void run(){
        while (!waiter.AccessGranted()&&active) {
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e1) {
                e1.printStackTrace();
            }
        }
        if(active)
            waiter.GetAccessAction();
    }
}
