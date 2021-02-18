package com.lab4.junit;

import com.lab4.bank.Purse;
import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class PurseTest {

    @Test
    public void testTakeMoney() throws Exception {
        Purse purse=new Purse(10,1);
        purse.TakeMoney(10);
        Assert.assertEquals(0,purse.GetAmount());
    }

    @Test
    public void testPutMoney() throws Exception {
        Purse purse=new Purse(10,1);
        purse.PutMoney(10);
        Assert.assertEquals(20,purse.GetAmount());
    }
}