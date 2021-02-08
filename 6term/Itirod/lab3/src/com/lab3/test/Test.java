package com.lab3.test;

import com.lab3.statistics.LetterCounter;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;


public class Test {
    public static void main(String[] args) throws IOException {
        LetterCounter counter=new LetterCounter();
        org.apache.log4j.BasicConfigurator.configure();
        HashMap<Character,Integer> stat=counter.GetStatistics("D:\\Labs\\labs.6term\\Java\\lab3\\in.txt");
        for(Map.Entry<Character,Integer> entry:stat.entrySet()){
            System.out.println(entry.getKey()+"-"+entry.getValue()+"-"+String.format("%.2f",entry.getValue()/(double)counter.getTotalamount()));
        }
    }
}
