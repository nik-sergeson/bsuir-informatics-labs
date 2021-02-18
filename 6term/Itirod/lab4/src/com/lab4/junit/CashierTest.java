package com.lab4.junit;

import com.lab4.bank.Bill;
import com.lab4.bank.Cashier;
import com.lab4.bank.Observer;
import com.lab4.bank.Purse;
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.*;

public class CashierTest {

    @Test(timeout = 10000)
    public void testTransfer() throws Exception {
        Bill bill1=new Bill(10,5),bill2=new Bill(10,4);
        ArrayList<Bill> bills=new ArrayList<Bill>();
        bills.add(bill1);
        bills.add(bill2);
        Cashier cashier=new Cashier(bills,new Observer(null,null,0),1);
        cashier.Transfer(bill1,bill2,10);
        Assert.assertTrue(bill1.GetAmount()==0);
        Assert.assertTrue(bill2.GetAmount()==20);
    }

    @Test
    public void testGetMoney() throws Exception {
        Bill bill1=new Bill(10,5);
        Purse purse=new Purse(10,5);
        ArrayList<Bill> bills=new ArrayList<Bill>();
        bills.add(bill1);
        Cashier cashier=new Cashier(bills,new Observer(null,null,0),1);
        cashier.GetMoney(bill1, purse, 10);
        Assert.assertTrue(bill1.GetAmount()==0);
        Assert.assertTrue(purse.GetAmount()==20);
    }

    @Test
    public void testPutMoney() throws Exception {
        Bill bill1=new Bill(10,5);
        Purse purse=new Purse(10,5);
        ArrayList<Bill> bills=new ArrayList<Bill>();
        bills.add(bill1);
        Cashier cashier=new Cashier(bills,new Observer(null,null,0),1);
        cashier.PutMoney(purse,bill1,10);
        Assert.assertTrue(bill1.GetAmount()==20);
        Assert.assertTrue(purse.GetAmount()==0);
    }
}