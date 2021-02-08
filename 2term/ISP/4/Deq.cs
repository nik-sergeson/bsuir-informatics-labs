using System;

public class Deq : Queue
{
    protected new DoubleNode _head, _tail;

    public void AddBeg(string str)
    {

        DoubleNode item = new DoubleNode();
        ++Size;
        item.next = null;
        item.prev = null;
        item._str = str;
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

    public string DelEnd()
    {
        string DelStr = string.Empty;

        if (!(_tail == null))
        {
            DelStr = _tail._str;
            _tail = _tail.prev;
            if (_tail != null)
                _tail.next = null;
            --Size;
        }
        return DelStr;
    }

    public override void AddEnd(string str)
    {

        ++Size;
        DoubleNode item = new DoubleNode();
        item.next = null;
        item.prev = null;
        item._str = str;
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

    public override string DelBeg()
    {
        string DelStr = string.Empty;

        if (!(_head == null))
        {
            DelStr = _head._str;
            _head = _head.next;
            if (_head != null)
                _head.prev = null;
            --Size;
        }
        return DelStr;
    }

    public override string Wiev(int Num)
    {
        int count;
        DoubleNode item;

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
        return item._str;
    }            
}