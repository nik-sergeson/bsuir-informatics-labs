package com.lab2.FileIO;
import org.apache.log4j.Logger;

import java.io.*;
import java.util.ArrayList;

public class FileReader {

    public  static final Logger log=Logger.getLogger(FileReader.class);

    public ArrayList<ArrayList<String>> ReadMatrixList(String path) throws FileNotFoundException {
        ArrayList<ArrayList<String>> matrixlist=new ArrayList<ArrayList<String>>();
        try {
            BufferedReader reader=new BufferedReader(new java.io.FileReader(path));
            log.info("file "+path+" opened");
            String str;
            while ((str=reader.readLine())!=null){
                int matrixsize=Integer.parseInt(str);
                ArrayList<String> matrix=new ArrayList<String>();
                for(int j=0;j<matrixsize;j++){
                    matrix.add(reader.readLine());
                }
                matrixlist.add(matrix);
            }
            reader.close();
            log.info(matrixlist.size()+" matrix read");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return matrixlist;
    }

    public void WriteMatrix(String matrix,int rowcount,String path){
        try {
            BufferedWriter writer=new BufferedWriter(new FileWriter(path,true));
            writer.write(Integer.toString(rowcount)+'\n');
            writer.write(matrix);
            log.info("matrix wrote to file "+path);
            writer.close();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
