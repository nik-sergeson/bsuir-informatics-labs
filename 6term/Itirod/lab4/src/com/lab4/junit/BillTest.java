package com.lab4.junit;

import com.lab4.bank.Bill;
import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class BillTest {
    @Test
    public void testTakeMoney() throws Exception {
        Bill bill=new Bill(10,1);
        bill.TakeMoney(10);
        Assert.assertEquals(0, bill.GetAmount());
    }

    @Test
    public void testPutMoney() throws Exception {
        Bill bill=new Bill(10,1);
        bill.PutMoney(10);
        Assert.assertEquals(20,bill.GetAmount());
    }

}