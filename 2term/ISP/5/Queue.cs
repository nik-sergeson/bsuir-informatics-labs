using System;

public class Queue<T>
{
    protected Node<T> _head, _tail;
    public int Size { get; set; }

    public Queue()
    {
        _head = null;
        _tail = null;
        Size = 0;
    }

    public void AddEnd(T str)
    {

        ++Size;
        Node<T> Elem = new Node<T>();
        Elem.next = null;
        Elem.prev = null;
        Elem._item = str;
        if (_head == null)
        {
            _head = Elem;
            _tail = Elem;
        }
        else
        {
            _tail.next = Elem;
            Elem.prev = _tail;
            _tail = Elem;
        }
    }

    public T DelBeg()
    {
        T DelStr=default(T);

        if (!(_head == null))
        {
            DelStr = _head._item;
            _head = _head.next;
            if (_head != null)
                _head.prev = null;
            --Size;
        }
        return DelStr;
    }

    public T Wiev(int Num)
    {
        int count;
        Node<T> item;

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