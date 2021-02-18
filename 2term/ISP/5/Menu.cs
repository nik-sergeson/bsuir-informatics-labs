using System;

public class QueueMenu<T>
{
    protected int choice = 0, i;
    public string s { get; set; }

    public QueueMenu()
    {
        choice = 0;
    }

    public void Menu()
    {
        T Elem;
        Queue<T> StrSym = new Queue<T>();
        while (choice != 4)
        {
            Console.Clear();
            Console.Write("Current choice:Queue\n1)Input value\n2) View queue\n3)Del string\n4)Quit\n");
            string s1 = string.Empty;
            s1 = Console.ReadLine();
             if (int.TryParse(s1, out choice) == false)
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
                            {
                                try
                                {
                                    Elem = (T)Convert.ChangeType(s, typeof(T));
                                    StrSym.AddEnd(Elem);
                                }
                                catch
                                {
                                    Console.WriteLine("wrong value");
                                }

                            }
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
                        Console.WriteLine("Deleted string:\n{0}", StrSym.DelBeg());
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
