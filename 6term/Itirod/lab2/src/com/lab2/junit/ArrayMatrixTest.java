package com.lab2.junit;

import com.lab2.matrix.ArrayMatrix;
import junit.framework.TestCase;
import org.junit.Assert;
import org.junit.Test;

public class ArrayMatrixTest{

    @Test
    public void testGetElem() throws Exception {
        ArrayMatrix matr=new ArrayMatrix(3,3);
        matr.SetElem(1,1,1);
        Assert.assertTrue(matr.GetElem(1,1)==1);
    }

    @Test
    public void testSetElem() throws Exception {
        ArrayMatrix matr=new ArrayMatrix(3,3);
        int old=matr.GetElem(1,1);
        matr.SetElem(1,1,matr.GetElem(1,1));
        Assert.assertTrue(old==matr.GetElem(1,1));
    }

    @Test
    public void testAdd() throws Exception {
        int[] arr={1,2};
        ArrayMatrix matrix=new ArrayMatrix(2,2);
        matrix.Add("1 2");
        Assert.assertTrue(matrix.GetElem(2,0)==arr[0]);
        Assert.assertTrue(matrix.GetElem(2,1)==arr[1]);
    }

    @Test
    public void testSum() throws Exception {
        ArrayMatrix matr1=new ArrayMatrix(2,2),zero=new ArrayMatrix(2,2),identity=new ArrayMatrix(2,2);
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                zero.SetElem(i,j,0);
                if(i==j){
                    identity.SetElem(i,i,1);
                }
                else
                    identity.SetElem(i,j,0);
            }
        }
        ArrayMatrix summ0=ArrayMatrix.Sum(matr1,zero),summ1=ArrayMatrix.Sum(matr1,identity);
        for(int i=0;i<2;i++) {
            for (int j = 0; j < 2; j++) {
                Assert.assertTrue(summ0.GetElem(i, j).intValue() == matr1.GetElem(i, j).intValue());
                if (i == j) {
                    Assert.assertTrue(summ1.GetElem(i, i).intValue() == matr1.GetElem(i, i).intValue() + 1);
                } else
                    Assert.assertTrue(summ1.GetElem(i, j).intValue() == matr1.GetElem(i, j).intValue());
            }
        }
    }

    @Test
    public void testMultiply() throws Exception {
        ArrayMatrix matr1=new ArrayMatrix(2,2),zero=new ArrayMatrix(2,2),identity=new ArrayMatrix(2,2);
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                zero.SetElem(i,j,0);
                if(i==j){
                    identity.SetElem(i,i,1);
                }
                else
                    identity.SetElem(i,j,0);
            }
        }
        ArrayMatrix summ0=ArrayMatrix.Multiply(matr1, zero),summ1=ArrayMatrix.Multiply(matr1,identity);
        for(int i=0;i<2;i++) {
            for (int j = 0; j < 2; j++) {
                Assert.assertTrue(summ0.GetElem(i, j).intValue() == 0);
                Assert.assertTrue(summ1.GetElem(i, j).intValue() == matr1.GetElem(i, j).intValue());
            }
        }
    }
}