package com.lab4.bank;

import org.apache.log4j.Logger;

import java.util.ArrayList;
import java.util.List;


public class Bank {
    public static final Logger log=Logger.getLogger(Observer.class);
    private ArrayList<Cashier> cachiers;
    private ArrayList<Client> clients;
    private ArrayList<Bill> bills;
    private long summary;
    private Observer observer;
    private Thread daemon;
    private ArrayList<Thread> clientthreads;

    public Bank(int cashiers,int clients, int bills, long summary){
        this.summary=summary;
        int perbill= (int) (summary/bills);
        this.bills=new ArrayList<Bill>();
        for(int i=1;i<bills;i++){
            this.bills.add(new Bill(perbill,i));
            this.summary-=perbill;
        }
        this.bills.add(new Bill(this.summary,this.bills.size()+1));
        this.summary=summary;
        this.clients=new ArrayList<Client>();
        for(int i=1;i<=clients;i++){
            this.clients.add(new Client(i,this,new Purse(0,i)));
        }
        observer=new Observer(this.bills,this.clients,summary);
        daemon=new Thread(observer);
        daemon.setDaemon(true);
        daemon.start();
        this.cachiers=new ArrayList<Cashier>();
        for(int i=0;i<cashiers;i++){
            this.cachiers.add(new Cashier(this.bills,this.observer,i));
        }
        clientthreads=new ArrayList<Thread>();
        for(int i=1;i<=clients;i++){
            clientthreads.add(new Thread(this.clients.get(i-1)));
            clientthreads.get(i-1).start();
        }
        log.info("Bank created");
    }

    public int BillCount(){
        return bills.size();
    }

    public Bill GetBill(int index){
        if(index<bills.size())
            return bills.get(index);
        else return null;
    }

    public synchronized Cashier GetCashier(){
        for(Cashier c:cachiers){
            if(!c.isBusy()){
                c.BeginTalk();
                return c;
            }
        }
        return null;
    }
}
