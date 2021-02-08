using System;

public class Deq<T> : Queue<T>
{
    protected new DoubleNode<T> _head, _tail;

    public new delegate void React();
    public new delegate void SizeReac(int i);
    public new event SizeReac OutOfRange;
    public new event SizeReac ObNumb;
    public new event React MemoryErr;
    public new event React IsEmpty;

    public new int Size
    {
        get
        {
           return _size;
        }
        set
        {
            _size = value;
            if (_size == 0)
            {
                if (IsEmpty != null)
                    IsEmpty();
            }
        }
    }

    public new int GetSize()
    {
        if (_size == 0)
        {
            if (IsEmpty != null)
                IsEmpty();
        }
        return _size;
    }

    public void AddBeg(string str)
    {
        T ELem;
        string Temp;
        try
        {
            Temp = str.ToString();
            if (Temp.Length == 0)
                throw new ArgumentOutOfRangeException();
            ELem = (T)Convert.ChangeType(str, typeof(T));
            DoubleNode<T> item = new DoubleNode<T>();
            ++Size;
            item.next = null;
            item.prev = null;
            item._item = ELem;
            if (_head == null)
            {
                _head = item;
                _tail = item;
            }
            else
            {
                _head.prev = item;
                item.next = _head;
                _head = item;
            }
        }
        catch (OutOfMemoryException){
            if (MemoryErr != null)
                MemoryErr();
        }   
   }

    public T DelEnd()
    {
        T DelStr = default(T);

        if (!(_tail == null))
        {
            DelStr = _tail._item;
            _tail = _tail.prev;
            if (_tail != null)
                _tail.next = null;
            --Size;
        }
        else
            if (IsEmpty != null)
                IsEmpty();
        return DelStr;
    }

    public override void AddEnd(string str)
    {
        string Temp;
        T Elem;

        try
        {
            Temp = str.ToString();
            if (Temp.Length == 0)
                throw new ArgumentOutOfRangeException();
            Elem = (T)Convert.ChangeType(str, typeof(T));
            ++Size;
            DoubleNode<T> item = new DoubleNode<T>();
            item.next = null;
            item.prev = null;
            item._item = Elem;
            if (_head == null)
            {
                _head = item;
                _tail = item;
            }
            else
            {
                _tail.next = item;
                item.prev = _tail;
                _tail = item;
            }
        }
        catch (OutOfMemoryException)
        {
            if (MemoryErr != null)
                MemoryErr();
        }
    }

    public override T DelBeg()
    {
        T DelStr =default(T);

        if (!(_head == null))
        {
            DelStr = _head._item;
            _head = _head.next;
            if (_head != null)
                _head.prev = null;
            --Size;
        }
        else
            if (IsEmpty != null)
                IsEmpty();
        return DelStr;
    }

    public override T Wiev(int Num)
    {
        int count;
        DoubleNode<T> item;

        if (Num > Size)
        {
            if (OutOfRange != null)
                OutOfRange(Num);
            return (default(T));
        }
        else
        {
            if (ObNumb != null)
                ObNumb(Num);
            if (Num > (Size / 2))
            {
                item = _tail;
                for (count = Size; count > Num; --count)
                    item = item.prev;
            }
            else
            {
                item = _head;
                for (count = 1; count < Num; ++count)
                    item = item.next;
            }
            return item._item;
        }
    }

    public static implicit operator string(Deq<T> x)
    {
        int i;
        string str = string.Empty;

        for (i = 1; i <= x.GetSize(); i++)
        {
            str += x.DelBeg().ToString();
        }
        return str;
    }

    public static explicit operator Deq<T>(T x){
        
        Deq<T> Elem=new Deq<T>();
        Elem.AddEnd(x.ToString());
        return Elem;
    }
}