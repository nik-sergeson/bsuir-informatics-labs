package com.lab4.junit;

import com.lab4.bank.Client;
import com.lab4.bank.Purse;
import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class ClientTest {

    @Test
    public void testGetID() throws Exception {
        Client client=new Client(1,null,null);
        Assert.assertTrue(client.GetID()==1);
    }

    @Test
    public void testGetAmount() throws Exception {
        Client client=new Client(1,null,new Purse(10,1));
        Assert.assertTrue(client.GetAmount()==10);
    }
}