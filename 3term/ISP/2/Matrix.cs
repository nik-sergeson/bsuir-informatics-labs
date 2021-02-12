using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.IO;
using System.Xml;
using System.Xml.Serialization;
using System.Runtime.Serialization;

[Serializable]
[DataContract]
public class Matrix<Elemtype> : IEnumerable<Vector<Elemtype>>, IEnumerable, IDisposable, IEquatable<Matrix<Elemtype>>
where Elemtype : struct
{
    [DataMember(Name="Vectors")]
    private List<Vector<Elemtype>> _vecrows;
    [DataMember]
    private int _colls;

    private class MatrixEnumerator : IEnumerator<Vector<Elemtype>>
    {
        private List<Vector<Elemtype>> _data;
        private int _position = -1;

        public MatrixEnumerator(List<Vector<Elemtype>> _value)
        {
            _data = new List<Vector<Elemtype>>(_value);
        }

        public void Dispose()
        {
        }

        public Vector<Elemtype> Current
        {
            get { return _data[_position]; }
        }

        public bool MoveNext()
        {
            if (_position < _data.Count - 1)
            {
                _position++;
                return true;
            }
            else
                return false;
        }

        public void Reset()
        {
            _position = 1;
        }

        object IEnumerator.Current
        {
            get { return _data[_position]; }
        }
    }

    public IEnumerator<Vector<Elemtype>> GetEnumerator()
    {
        return new MatrixEnumerator(_vecrows);
    }

    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    public int Rows { get ; set; }
    public int Colls
    {
        get { return _colls; }
        set
        {
            foreach (var x in _vecrows)
                x.Resize(value - Colls);
            _colls = value;
        }
    }

    public void Dispose()
    {
        foreach (Vector<Elemtype> x in _vecrows)
            x.Dispose();
    }

    public void Add(Vector<Elemtype> Row)
    {
        _vecrows.Add(Row);
        Rows++;
    }

    public Vector<Elemtype> this[int i]
    {
        get { return _vecrows[i]; }
        set { _vecrows[i] = value; }
    }

    public Matrix()
    {
        _vecrows = new List<Vector<Elemtype>>();
        Rows = 0;
        _colls = 0;
    }

    public Matrix(Vector<Elemtype>[] RawMatr)
    {
        if (RawMatr != null)
        {
            int MinDim = RawMatr[0].Lenght;
            _vecrows = new List<Vector<Elemtype>>(RawMatr);
            Rows = RawMatr.Length;
            for (int i = 1; i < RawMatr.Length; i++)
                if (RawMatr[i].Lenght < MinDim)
                    MinDim = RawMatr[i].Lenght;
            foreach (Vector<Elemtype> x in _vecrows)
            {
                x.Resize(MinDim - x.Lenght);
                x.Matr = this;
            }
            Colls = MinDim;
            Rows = RawMatr.Length;
        }
    }

    public Matrix(int RowC, int CollC)
    {
        _vecrows = new List<Vector<Elemtype>>(RowC);
        for (int i = 0; i < CollC;i++ )
        {
            _vecrows.Add(new Vector<Elemtype>(CollC,this));
        }
        _colls = CollC;
        Rows = RowC;
    }

    public void RemoveRange(int Ind, int Count)
    {
        if((Ind+Count<Rows)&&(Ind>-1)){
            _vecrows.RemoveRange(Ind - 1, Count);
            Rows=Rows-Count;
        }
    }

    public int Search(Vector<Elemtype> Row)
    {
        int Ind=0;
        _vecrows.Add(Row);
        while (!(_vecrows[Ind].Equals(Row)))
        {
            Ind++;
        }
        _vecrows.RemoveAt(_vecrows.Count - 1);
        return Ind;
    }

    public void ShowMatr()
    {
        foreach (var x in _vecrows)
        {
            foreach (var y in x)
            {
                Console.Write(y.ToString()+' ');
            }
            Console.WriteLine();
        }
    }

    public bool Equals(Matrix<Elemtype> smatr)
    {
        if ((this.Rows == smatr.Rows) && (this.Colls == smatr.Colls))
        {
            for (int i = 1; i <= this.Rows; i++)
                if (!(this[i].Equals(smatr[i])))
                    return false;
            return true;
        }
        else
            return false;
    }

    public Matrix<Elemtype> Summ(Matrix<Elemtype> Other)
    {
        if((this.Colls==Other.Colls)&&(this.Rows==Other.Rows)){
        Matrix<Elemtype>SummMatr=new Matrix<Elemtype>(this.Colls,this.Rows);
        for (int i = 0; i < this.Rows; i++)
            for (int j = 0; j < this.Colls;j++)
               SummMatr[i].AddVec(new Cell<Elemtype> { _value =this[i].Numbers[j]+ Other[i].Numbers[j]});
        return SummMatr;
        }
        return null;
    }

    public Matrix<Elemtype> Transpose()
    {
        Matrix<Elemtype> Temp = new Matrix<Elemtype>(this.Colls, this.Rows);
        for (int i = 0; i < this.Rows; i++)
            for (int j = 0; j < this.Colls; j++)
                Temp[j].AddVec(new Cell<Elemtype> { _value = this[i].Numbers[j]._value});
        return Temp;
    }

    public Matrix<Elemtype> Mulp(Matrix<Elemtype> Smatr)
    {
        if ((this.Colls == Smatr.Rows) && (this.Rows == Smatr.Colls))
        {
            Matrix<Elemtype> Temp = new Matrix<Elemtype>(this.Colls, this.Rows);
            for (int i = 0; i < this.Rows; i++)
                for (int j = 0; j < this.Colls; j++)
                    for (int k = 0; k <= this.Colls; k++)
                        Temp[i].AddVec(new Cell<Elemtype> { _value = Temp[i].Numbers[j] +this[i].Numbers[k] * Smatr[k].Numbers[j]});
            return Temp;
        }
        else
            return null;
    }

    public void NegMatr()
    {
        for (int i = 0; i < this.Rows; i++)
            for (int j = 0; j < this.Colls; j++)
                this[i].Numbers[j]._value = -this[i].Numbers[j];
    }

    public static Elemtype Determinant(Matrix<Elemtype> Matr)
    {
        Elemtype Summ=default(Elemtype);
        if (Matr.Rows == 1)
            return Matr[0].Numbers[0]._value;
        else
        {
            for (int i = 0; i < Matr.Colls; i++)
            {
                var SElem = new Cell<Elemtype> { _value = Math.Sign(Math.Pow(-1, i)) * Matr[0].Numbers[i] };
                var MAElem = new Cell<Elemtype> { _value = SElem * Determinant(DelRow(Matr, i)) };
                Summ =MAElem + Summ;
            }
            return Summ;
        }
    }

    public static Matrix<Elemtype> DelRow(Matrix<Elemtype> SMatr, int Row)
    {
        Matrix<Elemtype> Temp = new Matrix<Elemtype>(SMatr.Rows-1, SMatr.Colls-1);
        for (int i = 0; i < SMatr.Rows - 1; i++)
        {
            for (int j = 0; j < SMatr.Colls-1; j++)
            {
                Temp[i].AddVec(new Cell<Elemtype> ());
            }
        }
        for (int i = 0; i < SMatr.Rows-1; i++)
                for (int j=0; j <Row; j++)
                    Temp[i].Numbers[j]=SMatr[i+1].Numbers[j];
        for (int i = 0; i < SMatr.Rows - 1; i++)
            for (int j = Row; j < SMatr.Colls-1; j++)
                Temp[i].Numbers[j] = SMatr[i + 1].Numbers[j + 1];

        return Temp;
    }

    public int Find(Vector<Elemtype> vec)
    {
        return _vecrows.FindIndex(tvec=>tvec.Equals(vec));
    }
 }