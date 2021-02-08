package com.lab2.junit;

import com.lab2.FileIO.FileReader;
import org.junit.Assert;

import java.util.ArrayList;

import static org.junit.Assert.*;

public class FileReaderTest {

    @org.junit.Test
    public void testReadMatrixList() throws Exception {
        FileReader reader=new FileReader();
        ArrayList<ArrayList<String>> flist=reader.ReadMatrixList("D:\\Labs\\labs.6term\\Java\\lab2\\in.txt");
        ArrayList<ArrayList<String>> slist=reader.ReadMatrixList("D:\\Labs\\labs.6term\\Java\\lab2\\in.txt");
        Assert.assertEquals(flist.size(),slist.size());
        for(int i=0;i<flist.size();i++){
            Assert.assertEquals(flist.get(i).size(),slist.get(i).size());
            for(int j=0;j<flist.get(i).size();j++){
                Assert.assertEquals(flist.get(i).get(j),slist.get(i).get(j));
            }
        }
    }

}