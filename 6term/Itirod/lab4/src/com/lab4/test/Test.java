package com.lab4.test;

import com.lab4.bank.Bank;

import java.util.prefs.BackingStoreException;


public class Test {
    public static void main(String[] args){
        org.apache.log4j.BasicConfigurator.configure();
        Bank bank=new Bank(10,4,100,100000);
    }
}
