package com.lab4.junit;

import com.lab4.bank.Bank;
import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class BankTest {

    @Test
    public void testGetBill() throws Exception {
        Bank bank=new Bank(0,0,2,10);
        Assert.assertNotNull(bank.GetBill(1));
        Assert.assertNull(bank.GetBill(10));
    }

    @Test
    public void testGetCashier() throws Exception {
        Bank bank=new Bank(1,0,2,10);
        Assert.assertNotNull(bank.GetCashier());
    }
}