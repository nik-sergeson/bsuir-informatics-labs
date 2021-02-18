using System;

class Program
{
    public delegate void AddDel(string str);
    public delegate T DelDel<out T>();
    public delegate T ViewDel<out T>(int Num);
    public delegate T DelEnd<out T>();
    public delegate void AddBegDel(string str);
    public delegate int Size();

    public static void Reaction()
    {
        Console.Clear();
        Console.WriteLine("No elements available");
    }

    static void Main(string[] args)
    {
        string s;
        int choice;

        while (true)
        {
            Console.Clear();
            Console.WriteLine("Would you like queue or deq?(q/d)");
            s = Console.ReadLine();
            if (s.Length == 0)
                break;
            switch (s[0])
            {
                case 'q':
                    while (true)
                    {
                        Console.Clear();
                        Console.WriteLine("What type of queue?\n1)Int\n2)Double\n3)String\n");
                        s = Console.ReadLine();
                        if (s.Length == 0)
                            break;
                        if (int.TryParse(s, out choice) == false)
                            continue;
                        else
                        {
                            switch (choice)
                            {
                                case 1:
                                    Queue<int> StrSym = new Queue<int>();
                                    StrSym.IsEmpty += Reaction;
                                    StrSym.MemoryErr+=()=>Console.WriteLine("Programm is using too much memory");
                                    StrSym.OutOfRange += (Num) => Console.WriteLine("There aren't {0} elements", Num);
                                    StrSym.ObNumb += (Num) => Console.Write("{0})", Num);
                                    QueueMenu<int>.Menu(StrSym.AddEnd,StrSym.DelBeg,StrSym.GetSize,StrSym.Wiev);
                                    break;
                                case 2:
                                    Queue<double> StrSym2 = new Queue<double>();
                                    StrSym2.IsEmpty += Reaction;
                                    StrSym2.MemoryErr+=()=>Console.WriteLine("Programm is using too much memory");
                                    StrSym2.OutOfRange += (Num) => Console.WriteLine("There aren't {0} elements", Num);
                                    StrSym2.ObNumb += (Num) => Console.Write("{0})", Num);
                                    QueueMenu<double>.Menu(StrSym2.AddEnd, StrSym2.DelBeg, StrSym2.GetSize,StrSym2.Wiev);
                                    break;

                                case 3:
                                    Queue<string> StrSym3 = new Queue<string>();
                                    StrSym3.IsEmpty += Reaction;
                                    StrSym3.MemoryErr+=()=>Console.WriteLine("Programm is using too much memory");
                                    StrSym3.OutOfRange += (Num) => Console.WriteLine("There aren't {0} elements", Num);
                                    StrSym3.ObNumb += (Num) => Console.Write("{0})", Num);
                                    QueueMenu<string>.Menu(StrSym3.AddEnd, StrSym3.DelBeg, StrSym3.GetSize,StrSym3.Wiev);
                                    break;
                            }

                        }
                    }
                    break;
                case 'd':
                    while (true)
                    {
                        Console.Clear();
                        Console.WriteLine("What type of queue?\n1)Int\n2)Double\n3)String\n");
                        s = Console.ReadLine();
                        if (s.Length == 0)
                            break;
                        if (int.TryParse(s, out choice) == false)
                            continue;
                        else
                        {
                            switch (choice)
                            {
                                case 1:
                                    Deq<int> StrSym = new Deq<int>();
                                    StrSym.IsEmpty += Reaction;
                                    StrSym.MemoryErr += () => Console.WriteLine("Programm is using too much memory");
                                    StrSym.OutOfRange += (Num) => Console.WriteLine("There aren't {0} elements", Num);
                                    StrSym.ObNumb += (Num) => Console.Write("{0})", Num);
                                    DeqMenu<int>.Menu(StrSym.AddEnd,StrSym.DelBeg,StrSym.Wiev,StrSym.GetSize,StrSym.DelEnd,StrSym.AddBeg);
                                    break;
                                case 2:
                                    Deq<double> StrSym2 = new Deq<double>();
                                    StrSym2.IsEmpty += Reaction;
                                    StrSym2.MemoryErr += () => Console.WriteLine("Programm is using too much memory");
                                    StrSym2.OutOfRange += (Num) => Console.WriteLine("There aren't {0} elements", Num);
                                    StrSym2.ObNumb += (Num) => Console.Write("{0})", Num);
                                    DeqMenu<double>.Menu(StrSym2.AddEnd,StrSym2.DelBeg,StrSym2.Wiev,StrSym2.GetSize,StrSym2.DelEnd,StrSym2.AddBeg);
                                    break;

                                case 3:
                                    Deq<string> StrSym3 = new Deq<string>();
                                    StrSym3.IsEmpty += Reaction;
                                    StrSym3.MemoryErr += () => Console.WriteLine("Programm is using too much memory");
                                    StrSym3.OutOfRange += (Num) => Console.WriteLine("There aren't {0} elements", Num);
                                    StrSym3.ObNumb += (Num) => Console.Write("{0})", Num);
                                    DeqMenu<string>.Menu(StrSym3.AddEnd,StrSym3.DelBeg,StrSym3.Wiev,StrSym3.GetSize,StrSym3.DelEnd,StrSym3.AddBeg);
                                    break;
                            }

                        }
                    }
                    break;
            }
        }
    }
}