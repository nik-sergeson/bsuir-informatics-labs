package com.lab4.bank;


public class Bill {
    private long amount;
    private long id;

    public Bill(){
        amount=0;
    }

    public Bill(long amount,long id){
        this.amount=amount;
        this.id=id;
    }

    public long GetID(){return id;}

    public synchronized void TakeMoney(long amount){
        this.amount-=amount;
    }

    public synchronized void PutMoney(long amount){
        this.amount+=amount;
    }

    public synchronized long GetAmount(){
        return amount;
    }
}
