package com.lab4.bank;

import org.apache.log4j.Logger;

import java.util.Locale;
import java.util.Random;


public class Client implements Runnable{
    private Purse purse;
    private long id;
    private Bank bank;
    private static final long delay=1000;
    private static final int maxperoperation=100;
    public static final Logger log=Logger.getLogger(Observer.class);

    public Client(long id,Bank bank,Purse purse){
        this.id=id;
        this.bank=bank;
        this.purse=purse;
    }

    public long GetID(){
        return id;
    }

    public long GetAmount(){
        return purse.GetAmount();
    }

    public void run(){
        Random generator=new Random();
        while (true){
            Cashier cashier;
            while ((cashier=bank.GetCashier())==null) {
                try {
                    Thread.sleep(delay);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            if(generator.nextBoolean()){
                long amount=generator.nextInt(maxperoperation);
                int fbillindex=generator.nextInt(bank.BillCount()),sbillindex=generator.nextInt(bank.BillCount());
                boolean succ=cashier.Transfer(bank.GetBill(fbillindex),bank.GetBill(sbillindex),amount);
                if(succ)
                    log.info(Long.toString(amount)+" moved from "+Integer.toString(fbillindex)+" to "+Integer.toString(sbillindex)+" successfully, client:"+Long.toString(id));
                else
                    log.info(Long.toString(amount)+" moved from "+Integer.toString(fbillindex)+" to "+Integer.toString(sbillindex)+" with failure, client:"+Long.toString(id));
            }
            else {
                if(generator.nextBoolean()){
                    long amount=generator.nextInt(maxperoperation);
                    int billindex=generator.nextInt(bank.BillCount());
                    boolean succ=cashier.GetMoney(bank.GetBill(billindex),this.purse,amount);
                    if(succ)
                        log.info(Long.toString(amount)+" moved from"+Integer.toString(billindex)+" to purse successfully, client:"+Long.toString(id));
                    else
                        log.info(Long.toString(amount)+" moved from"+Integer.toString(billindex)+" to purse with failure, client:"+Long.toString(id));
                }
                if (generator.nextBoolean()){
                    long amount=generator.nextInt(maxperoperation);
                    int billindex=generator.nextInt(bank.BillCount());
                    boolean succ=cashier.PutMoney(purse,bank.GetBill(billindex),amount);
                    if(succ)
                        log.info(Long.toString(amount)+" moved from purse to "+Integer.toString(billindex)+" successfully, client:"+Long.toString(id));
                    else
                        log.info(Long.toString(amount)+" moved from purse to "+Integer.toString(billindex)+" with failure, client:"+Long.toString(id));
                }
            }
            cashier.EndTalk();
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
