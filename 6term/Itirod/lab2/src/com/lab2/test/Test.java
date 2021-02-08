package com.lab2.test;

import com.lab2.FileIO.FileReader;
import com.lab2.matrix.ArrayMatrix;
import com.lab2.matrix.ListMatrix;

import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.util.ArrayList;


public class Test {
    public static void main(String[] args) throws FileNotFoundException {
        org.apache.log4j.BasicConfigurator.configure();
        FileReader reader=new FileReader();
        ArrayList<ArrayMatrix> matrixlist=new ArrayList<ArrayMatrix>();
        ArrayList<ArrayList<String>> rawmatrix=reader.ReadMatrixList("D:\\Labs\\labs.6term\\Java\\lab2\\in.txt");
        for(int i=0;i<rawmatrix.size();i++){
            ArrayMatrix matrix=new ArrayMatrix();
            for(int j=0;j<rawmatrix.get(i).size();j++){
                matrix.Add(rawmatrix.get(i).get(j));
            }
            matrixlist.add(matrix);
        }
        for(int i=0;i<matrixlist.size();i++){
            for(int j=i;j<matrixlist.size();j++){
                ArrayMatrix mulmatr=ArrayMatrix.Multiply(matrixlist.get(i),matrixlist.get(j));
                System.out.println(mulmatr);
                reader.WriteMatrix(mulmatr.toString(),mulmatr.RowCount(),"D:\\Labs\\labs.6term\\Java\\lab2\\out.txt");
            }
        }
        ArrayMatrix arrmatr1=new ArrayMatrix(100,100);
        ArrayMatrix arrmatr2=new ArrayMatrix(100,100);
        long start=System.nanoTime();
        ArrayMatrix.Multiply(arrmatr1,arrmatr2);
        long end=System.nanoTime()-start;
        System.out.println("ArrayList:");
        System.out.println(end);
        ListMatrix lmatr1=new ListMatrix(100,100);
        ListMatrix lmatr2=new ListMatrix(100,100);
        start=System.nanoTime();
        ListMatrix.Multiply(lmatr1,lmatr2);
        end=System.nanoTime()-start;
        System.out.println("LinkedList");
        System.out.println(end);
    }
}
