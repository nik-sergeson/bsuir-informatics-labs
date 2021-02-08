package com.lab3.statistics;

import junit.framework.Assert;
import org.apache.log4j.Logger;
import org.junit.Test;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import org.junit.*;


public class LetterCounter {
    private HashMap<Character,Integer> amount;
    private int totalamount;
    public static final Logger log=Logger.getLogger(LetterCounter.class);

    public LetterCounter(){
        amount=new HashMap<Character, Integer>();
    }

    public ArrayList<Character> GetTokens(String path) throws IOException {
        FileReader reader=new FileReader(path);
        ArrayList<Character> chararray=new ArrayList<Character>();
        log.info("file "+path+" successfully opened");
        int ch;
        while ((ch=reader.read())!=-1&&Character.isLetter(ch)){
            chararray.add((char)ch);
        }
        log.info(chararray.size()+" character read");
        reader.close();
        return chararray;
    }

    public HashMap<Character,Integer> GetStatistics(String path) throws IOException {
        amount=new HashMap<Character, Integer>();
        ArrayList<Character> charlist=GetTokens(path);
        totalamount=charlist.size();
        for(char ch:charlist){
            if(!amount.containsKey(Character.toLowerCase(ch))){
                amount.put(Character.toLowerCase(ch),1);
            }
            else {
                amount.put(Character.toLowerCase(ch),amount.get(Character.toLowerCase(ch))+1);
            }
        }
        log.info(amount.size()+" unique character found");
        return amount;
    }

    public int getTotalamount() {
        return totalamount;
    }

    public void setTotalamount(int totalamount) {
        this.totalamount = totalamount;
    }
}
