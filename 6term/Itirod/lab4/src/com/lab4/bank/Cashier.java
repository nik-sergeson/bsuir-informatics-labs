package com.lab4.bank;

import org.apache.log4j.Logger;

import java.util.ArrayList;


public class Cashier {
    private boolean busy;
    private ArrayList<Bill> bills;
    private static final long delay=5;
    private Observer observer;
    private int id;
    public static final Logger log=Logger.getLogger(Observer.class);

    public Cashier(ArrayList<Bill> bills,Observer observer,int id){
        this.busy=false;
        this.bills=bills;
        this.observer=observer;
        this.id=id;
    }

    public boolean isBusy(){
        return busy;
    }

    public void BeginTalk(){
        busy=true;
        log.info("Cashier "+Integer.toString(id)+" started serving client");
    }

    public void EndTalk(){
        busy=false;
        log.info("Cashier "+Integer.toString(id)+ "is free");
    }

    public boolean Transfer(Bill source,Bill destination,long amount){
        while (true){
            synchronized (source){
                synchronized (destination){
                    if(observer.BillChecked(source.GetID())==observer.BillChecked(destination.GetID())){
                        if(amount>source.GetAmount()){
                            log.info("System hasnt enough money");
                            return false;
                        }
                        source.TakeMoney(amount);
                        destination.PutMoney(amount);
                        log.info("Transfer success");
                        return true;
                    }

                }
            }
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public boolean GetMoney(Bill source,Purse purse,long amount){
        while (true){
            synchronized (source){
                synchronized (purse){
                    if(observer.PurseChecked(purse.GetID())||!observer.BillChecked(source.GetID())){
                        if(amount>source.GetAmount()){
                            log.info("System hasnt enough money");
                            return false;
                        }
                        source.TakeMoney(amount);
                        purse.PutMoney(amount);
                        log.info("Transfer success");
                        return true;
                    }
                }
            }
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public boolean PutMoney(Purse purse,Bill destination, long amount){
        while (true){
            synchronized (purse){
                synchronized (destination){
                    if(observer.PurseChecked(purse.GetID())||!observer.BillChecked(destination.GetID())){
                        if(amount>purse.GetAmount()){
                            log.info("System hasnt enough money");
                            return false;
                        }
                        purse.TakeMoney(amount);
                        destination.PutMoney(amount);
                        log.info("Transfer success");
                        return true;
                    }
                }
            }
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
