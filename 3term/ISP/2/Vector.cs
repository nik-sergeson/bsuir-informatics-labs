using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Runtime.Serialization;

[Serializable]
[DataContract]
public class Vector<CellType> : IEnumerable<Cell<CellType>>, IDisposable, IEquatable<Vector<CellType>>
    where CellType:struct
{
    [DataMember(Name="Cells")]
    public List<Cell<CellType>> Numbers{get; set;}
    [NonSerialized]
    private List<Cell<CellType>> NumCash;
    public Matrix<CellType> Matr{get; set;}

    private class VectorEnumerator : IEnumerator<Cell<CellType>>
    {
        private int _position = -1;
        private List<Cell<CellType>> _edata;

        public VectorEnumerator(List<Cell<CellType>> _data)
        {
            _edata = new List<Cell<CellType>>(_data);
        }

        public void Dispose()
        {
        }

        public bool MoveNext()
        {
            if (_position < _edata.Count - 1)
            {
                _position++;
                return true;
            }
            else
                return false;
        }

        public Cell<CellType> Current
        {
            get { return _edata[_position]; }
        }

        public void Reset()
        {
            _position = -1;
        }

        object IEnumerator.Current
        {
            get { return _edata[_position]; }
        }

    }

    public IEnumerator<Cell<CellType>> GetEnumerator()
    {
        return new VectorEnumerator(Numbers);
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    public void Dispose()
    {
    }

    public Vector()
    {
        Numbers = new List<Cell<CellType>>();
        NumCash = new List<Cell<CellType>>();
        Matr = null;
    }

    public Vector(Cell<CellType>[] ValC, int Dim,Matrix<CellType> Tmatr)
    {
        if (ValC.Length != Dim)
            Numbers = new List<Cell<CellType>>();
        else
            Numbers = new List<Cell<CellType>>(ValC);
        NumCash = new List<Cell<CellType>>();
        Matr = Tmatr;
    }

    public Vector (int Dim,Matrix<CellType> Tmatr)
    {
        Numbers = new List<Cell<CellType>>(Dim);
        NumCash = new List<Cell<CellType>>();
        Matr = Tmatr;
    }

    public void Add(Cell<CellType> Num)
    {
        NumCash.Add(Num);
    }

    public void AddVec(Cell<CellType> Num)
    {
        Numbers.Add(Num);
    }

    public void DeleteIndex(int Ind)
    {
        if (Ind < Numbers.Count)
        {
            Numbers.RemoveAt(Ind - 1);
            if (NumCash != null)
            {
                Numbers.Add(NumCash[0]);
                NumCash.RemoveAt(0);
            }
            else
                Numbers.Add(new Cell<CellType>());
        }

    }

    public int Search(CellType Num)
    {
        int Ind = 0;

        Numbers.Add(new Cell<CellType> { _value = Num });
        while (!(Numbers[Ind].Equals(Num)))
            Ind++;
        Numbers.RemoveAt(Numbers.Count - 1);
        return Ind;
    }

    public void DeleteNum(CellType Num)
    {
        int Ind = 0,j=0, MatrDim = Numbers.Count;

        while (Ind < Numbers.Count)
        {
            if (Numbers[Ind].Equals(Num))
                Numbers.RemoveAt(Ind);
            Ind++;
        }
        while (Ind < MatrDim)
        {
            if (NumCash.Count != 0)
            {
                if ((!(NumCash[j].Equals(Num)))&&(j<NumCash.Count))
                {
                    Numbers.Add(NumCash[j]);
                    NumCash.RemoveAt(j);
                    Ind++;
                }
                else
                    j++;
            }
            else
            {
                if (!(new Cell<CellType>().Equals(Num)))
                {
                    Numbers.Add(new Cell<CellType>());
                    Ind++;
                }
                else
                    throw new ArgumentOutOfRangeException();
            }
        }
    }

    public void Resize(int size)
    {
        if (size >= 0)
        {
            for (int i = 1; i <= size; i++)
            {
                if (NumCash.Count > 0)
                {
                    Numbers.Add(NumCash[0]);
                    NumCash.RemoveAt(0);
                }
                else
                    Numbers.Add(new Cell<CellType>());
            }
        }
        else
            Numbers.RemoveRange(Numbers.Count + size - 1, Math.Abs(size));
    }

    public int Lenght
    {
        get { return Numbers.Count; }
    }

    public int Cashlength
    {
        get { return NumCash.Count; }
    }

    public bool Equals(Vector<CellType> other)
    {
        if ((!(object.ReferenceEquals(null,other)))&&(other.Lenght==this.Lenght))
        {
            for (int i = 0; i < other.Lenght; i++)
                if (!(this.Numbers[i].Equals(other.Numbers[i])))
                    return false;
        }
        return true;
    }

    public override string ToString()
    {
        string str=string.Empty;
        foreach (var x in Numbers)
            str = str + x.ToString()+' ';
        return str;
    }

}