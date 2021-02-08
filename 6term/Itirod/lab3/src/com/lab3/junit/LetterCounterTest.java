package com.lab3.junit;

import com.lab3.statistics.LetterCounter;
import junit.framework.TestCase;
import org.junit.Assert;
import org.junit.*;

import java.util.ArrayList;

public class LetterCounterTest extends TestCase {

    @Test
    public void testGetTokens() throws Exception {
        LetterCounter lcount=new LetterCounter();
        ArrayList<Character> tokens=lcount.GetTokens("D:\\Labs\\labs.6term\\Java\\lab3\\in.txt");
        Assert.assertNotNull(tokens);
        Assert.assertTrue(tokens.size()>=lcount.GetStatistics("D:\\Labs\\labs.6term\\Java\\lab3\\in.txt").size());
    }
}