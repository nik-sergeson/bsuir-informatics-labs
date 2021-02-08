package com.lab4.bank;

import org.apache.log4j.Logger;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;


public class Observer implements Runnable {
    private ArrayList<Bill> bills;
    private ArrayList<Client> clients;
    private long summary;
    private static final long delay=1000;
    private HashSet<Long> checkedbills;
    private HashSet<Long> checkedpurses;
    public static final Logger log=Logger.getLogger(Observer.class);

    public Observer(ArrayList<Bill> bills,ArrayList<Client> clients,long summary){
        this.bills=bills;
        this.clients=clients;
        this.summary=summary;
        checkedbills=new HashSet<Long>();
        checkedpurses=new HashSet<Long>();
        log.info("Observer created");
    }

    public boolean BillChecked(long id){
        return checkedbills.contains(id);
    }

    public boolean PurseChecked(long id){return checkedpurses.contains(id);}

    public void run(){
        while (true){
            long money=0,amount=0;
            for(Bill x:bills){
                synchronized (x){
                    amount=x.GetAmount();
                    checkedbills.add(x.GetID());
                }
                if(amount<0)
                    log.info("Bill with negative balance: "+x.GetID());
                money+=amount;
            }
            for(Client x:clients){
                synchronized (x) {
                    amount = x.GetAmount();
                    checkedpurses.add(x.GetID());
                }
                if(amount<0)
                    log.info("Client with negative balance: "+x.GetID());
                money+=amount;
            }
            if(money==summary){
                log.info("Total amount isnt changed");
            }
            else{
                log.info("System amount is changed");
            }
            checkedbills.clear();
            checkedpurses.clear();
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
