using System;

public class QueueMenu
{
    protected int choice = 0, i;
    public string s{get;set;}

    public QueueMenu()
    {
        choice = 0;
    }

    public virtual void Menu()
    {
        Queue StrSym = new Queue();
        while (choice != 4)
        {
            Console.Clear();
            Console.Write("Current choice:Queue\n1)Input Text\n2) View queue\n3)Del string\n4)Quit\n");
            s = Console.ReadLine();
            if (int.TryParse(s, out choice) == false)
                continue;
            else
            {
                switch (choice)
                {
                    case 1:
                        Console.Clear();
                        while (true)
                        {
                            s = Console.ReadLine();
                            if ((s.Length) == 0)
                                break;
                            else
                                StrSym.AddEnd(s);
                        }
                        break;
                    case 2:
                        Console.Clear();
                        for (i = 1; i <= StrSym.Size; i++)
                            Console.WriteLine(StrSym.Wiev(i));
                        Console.Read();
                        break;
                    case 3:
                        Console.Clear();
                        Console.WriteLine("Deleted string:\n{0}",StrSym.DelBeg());
                        Console.Read();
                        break;
                    case 4:
                        choice = 4;
                        break;
                }
            }

        }
    }
}

public class DeqMenu : QueueMenu
{

    public override void Menu()
    {
        Deq StrSym = new Deq();
        while (choice != 6)
        {
            Console.Clear();
            Console.Write("Current choice:Queue\n1)Input Text(add to end)\n2)Input Text(add to begin)\n3) View queue\n4)Del string(from begin)\n5)Del string(from end)\n6)Quit\n");
            s = Console.ReadLine();
            if (int.TryParse(s, out choice) == false)
                continue;
            else
            {
                switch (choice)
                {
                    case 1:
                        Console.Clear();
                        while (true)
                        {
                            s = Console.ReadLine();
                            if ((s.Length) == 0)
                                break;
                            else
                                StrSym.AddEnd(s);
                        }
                        break;
                    case 2:
                        Console.Clear();
                        while (true)
                        {
                            s = Console.ReadLine();
                            if ((s.Length) == 0)
                                break;
                            else
                                StrSym.AddBeg(s);
                        }
                        break;
                    case 3:
                        Console.Clear();
                        for (i = 1; i <= StrSym.Size; i++)
                            Console.WriteLine(StrSym.Wiev(i));
                        Console.Read();
                        break;
                    case 4:
                        Console.Clear();
                        Console.WriteLine("Deleted string:\n{0}", StrSym.DelBeg());
                        Console.Read();
                        break;
                    case 5:
                        Console.Clear();
                        Console.WriteLine("Deleted string:\n{0}", StrSym.DelEnd());
                        Console.Read();
                        break;
                    case 6:
                        choice = 6;
                        break;
                }
            }

        }
    }
}