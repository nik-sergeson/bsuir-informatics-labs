using System;

public class Queue<T>
{
    protected SingleNode<T> _head, _tail;

    public delegate void React();
    public delegate void SizeReac(int i);
    public event SizeReac ObNumb;
    public event SizeReac OutOfRange;
    public event React MemoryErr;
    public event React IsEmpty;

    public int Size
    {
        get {
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
    protected int _size;

    public int GetSize()
    {
        if (_size == 0)
        {
            if (IsEmpty != null)
                IsEmpty();
        }
        return _size;
    }

    public Queue()
    {
        _head = null;
        _tail = null;
        Size = 0;
    }

    public virtual void AddEnd(string str)
    {
        T item;
        string Temp;

        try
        {
            Temp = str.ToString();
            if (Temp.Length == 0)
                throw new ArgumentOutOfRangeException();
            item = (T)Convert.ChangeType(str, typeof(T));
            ++Size;
            SingleNode<T> Elem = new SingleNode<T>();
            Elem.next = null;
            Elem._item = item;
            if (_head == null)
            {
                _head = Elem;
                _tail = Elem;
            }
            else
            {
                _tail.next = Elem;
                _tail = Elem;
            }
        }
        catch (OutOfMemoryException)
        {
            if (MemoryErr != null)
                MemoryErr();
        }
    }

    public virtual T DelBeg()
    {
        T DelStr = default(T);

        if (!(_head == null))
        {
            DelStr = _head._item;
            _head = _head.next;
            --Size;
        }
        else
            if (IsEmpty != null)
                IsEmpty();
        return DelStr;
    }

    public virtual T Wiev(int Num)
    {
        int count;
        SingleNode<T> item;

        if (Num > Size)
        {
            if (OutOfRange != null)
                OutOfRange(Num);
            return default(T);
        }
        else
        {
            if (ObNumb != null) 
                ObNumb(Num);
            item = _head;
            for (count = 1; count < Num; ++count)
                item = item.next;
            return item._item;
        }
    }


    public static implicit operator string(Queue<T> x)
    {
        int i;
        string str = string.Empty;

        for (i = 1; i <= x.GetSize(); i++)
        {
            str += x.DelBeg().ToString();
        }
        return str;
    }

    public static explicit operator Queue<T>(T x)
    {

        Queue<T> Elem = new Queue<T>();
        Elem.AddEnd(x.ToString());
        return Elem;
    }
}