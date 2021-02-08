package com.lab2.matrix;

import org.apache.log4j.Logger;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Random;


public class ArrayMatrix extends Matrix implements Serializable{
    private ArrayList<ArrayList<Integer>> Matrix;
    public static final Logger log=Logger.getLogger(ArrayMatrix.class);

    @Override
    public String toString(){
        String outstr="";
        for(int i=0;i<RowCount();i++){
            for(int j=0;j<ColCount();j++)
                outstr+=Matrix.get(i).get(j)+" ";
            outstr+="\n";
        }
        return outstr;
    }

    public ArrayMatrix(){
        Matrix=new ArrayList<ArrayList<Integer>>();
    }

    public ArrayMatrix(ArrayList<ArrayList<Integer>> matrix){
        Matrix=matrix;
    }

    public ArrayMatrix(int i, int j){
        Matrix=new ArrayList<ArrayList<Integer>>();
        Random rand=new Random();
        for(int k=0;k<i;k++){
            ArrayList<Integer> item=new ArrayList<Integer>();
            for(int m=0;m<j;m++)
                item.add(rand.nextInt(200));
            Matrix.add(item);
        }
    }

    public Integer GetElem(int i,int j){
        return Matrix.get(i).get(j);
    }

    public void SetElem(int i,int j,int value){
        Matrix.get(i).set(j,value);
        log.info("element "+Integer.toString(i)+" "+Integer.toString(j)+" changed to "+Integer.toString(value));
    }

    public int RowCount(){
        return Matrix.size();
    }

    public int ColCount(){
       return Matrix.size()>0?Matrix.get(0).size():0;
    }

    public void Add(String vector){
        String[] svector=vector.split("\\s+");
        if(ColCount()==svector.length||RowCount()==0) {
            ArrayList<Integer> parsedvector = new ArrayList<Integer>();
            for (int i = 0; i < svector.length; i++)
                parsedvector.add(Integer.parseInt(svector[i]));
            Matrix.add(parsedvector);
            log.info(vector + " added to arraymatrix");
        }
    }

    public static ArrayMatrix Sum(ArrayMatrix matr1,ArrayMatrix matr2) {
        ArrayList<ArrayList<Integer>> summatr = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < matr1.RowCount(); i++) {
            ArrayList<Integer> summvector=new ArrayList<Integer>();
            for (int j = 0; j < matr1.ColCount(); j++)
                summvector.add(matr1.GetElem(i, j) + matr2.GetElem(i, j));
            summatr.add(summvector);
        }
        log.info("summ of matrix "+matr1.ColCount()+"x"+matr1.RowCount()+" found");
        return new ArrayMatrix(summatr);
    }

    public static ArrayMatrix Multiply(ArrayMatrix matr1,ArrayMatrix matr2) {
        ArrayList<ArrayList<Integer>> mulmatrix=new ArrayList<ArrayList<Integer>>();
        int result=0;
        if (matr1.ColCount() == matr2.RowCount()) {
            for (int i = 0; i <matr1.RowCount(); i++) {
                ArrayList<Integer> mulvector=new ArrayList<Integer>();
                for (int j = 0; j < matr2.ColCount(); j++) {
                    result=0;
                    for(int m=0;m<matr1.ColCount();m++){
                        result+=matr1.GetElem(i,m)*matr2.GetElem(m,j);
                    }
                    mulvector.add(result);
                }
                mulmatrix.add(mulvector);
            }
        }
        log.info("multiplication of maxtrix "+matr1.RowCount()+"x"+matr2.ColCount()+" perfomed");
        return new ArrayMatrix(mulmatrix);
    }

}
