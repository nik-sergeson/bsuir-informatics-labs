package com.lab2.matrix;

import java.util.LinkedList;
import java.util.Random;


public abstract class Matrix {

    public Matrix(){}

    public Matrix(LinkedList<LinkedList<Integer>> matrix){ }

    public Matrix(int i, int j){  }

    public abstract Integer GetElem(int i,int j);

    public abstract void SetElem(int i,int j,int value);

    public abstract int RowCount();

    public abstract int ColCount();

    public abstract void Add(String vector);
}
