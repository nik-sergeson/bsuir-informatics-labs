using System;

public class Queue
{
    protected SingleNode _head, _tail;
    public int Size{get;set;}

    public Queue()
    {
        _head = null;
        _tail = null;
        Size=0;
    }

    public virtual void AddEnd(string str){

        ++Size;
        SingleNode item = new SingleNode();
        item.next = null;
        item._str = str;
        if(_head==null){
            _head=item;
            _tail =item;
        }
        else{
            _tail.next=item;
            _tail=item;
        }
    }

    public virtual string DelBeg()
    {
        string DelStr=string.Empty;

        if (!(_head==null))
        {
            DelStr = _head._str;
            _head = _head.next;
            --Size;
        }
        return DelStr;
    }

    public virtual string Wiev(int Num)
    {
        int count;
        SingleNode item;

            item = _head;
            for (count = 1; count < Num; ++count)
                item = item.next;
           return item._str;
    }            
}