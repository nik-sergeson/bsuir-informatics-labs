using System;

class Queue
{
    private int _head, _tail;
    private char[] turn;

    public char this[int i]
    {
        get { return turn[i]; }
        set { turn[i] = value; }
    }

    public Queue()
    {

        _head = 0;
        _tail = -1;
        turn = new char[0];
    }

    public void Add(char ch)
    {
        ++_tail;
        Array.Resize(ref turn, _tail+1);
        turn[_tail] = ch;
    }

    public char Del()
    {
        int i;
        char ch = '\0';

        if (_head <= _tail)
        {
            ch = turn[0];
            for (i = 1; i <= _tail; i++)
                turn[i - 1] = turn[i];
            Array.Resize(ref turn, _tail);
            --_tail;
        }
        return ch;
    }

    public void Print()
    {
        char ch;

        while ((ch = Del()) != '\0')
            Console.Write(ch);
    }
}

class trymyclass
{

    static void Main()
    {
        char ch = '\0';

        Queue StrSym = new Queue();
        while ((ch = (char)Console.Read()) != '\n')
            StrSym.Add(ch);
        StrSym.Print();
        Console.Write('\n');
        Console.Read();
    }
}