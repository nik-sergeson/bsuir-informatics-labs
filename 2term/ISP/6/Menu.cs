using System;

public static class QueueMenu<T>
{
    public delegate void AddDel(string str);
    public delegate T DelDel();
    public delegate T ViewDel(int Num);
    public delegate int Size();
    
    public static void Menu(AddDel AD,DelDel DD,Size Sz,ViewDel VD)
    {
        int choice = 0, i;
        string s;

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
                            try
                            {                         
                                    AD(s);
                            }
                            catch (ArgumentOutOfRangeException)
                            {
                               break;
                            }
                            catch (FormatException)
                            {
                                Console.WriteLine("Wrong value");
                            }

                            }
                        break;
                    case 2:
                        Console.Clear();
                        for (i = 1; i <= Sz(); i++)
                            Console.WriteLine(VD(i));
                        Console.Read();
                        break;
                    case 3:
                        Console.Clear();
                        if(Sz()>0)
                            Console.WriteLine("Deleted string:\n{0}", DD());
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

public static class DeqMenu<T> 
{
    public delegate void AddDel(string str);
    public delegate T DelDel();
    public delegate T ViewDel(int Num);
    public delegate T DelEnd();
    public delegate void AddBegDel(string str);
    public delegate int Size();

    public static void Menu(AddDel AD,DelDel DD,ViewDel VD,Size Sz,DelEnd DED,AddBegDel ABD)
    {
        int choice = 0, i;
        string s;

        while (choice != 6)
        {
            Console.Clear();
            Console.Write("Current choice:Deq\n1)Input Text(add to end)\n2)Input Text(add to begin)\n3) View deq\n4)Del string(from begin)\n5)Del string(from end)\n6)Quit\n");
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
                                try
                                {
                                    AD(s);
                                }
                                catch (ArgumentOutOfRangeException)
                                {
                                        break;
                                }
                                catch(FormatException)
                                {
                                    Console.WriteLine("Wrong value");
                                }

                            }
                        break;
                    case 2:
                        Console.Clear();
                        while (true)
                        {
                            s = Console.ReadLine();
                                try
                                {
                                    ABD(s);
                                }
                                catch (ArgumentOutOfRangeException)
                                {
                                        break;
                                }
                                catch(FormatException)
                                {
                                    Console.WriteLine("Wrong value");
                                }

                            }
                        break;
                    case 3:
                        Console.Clear();
                        for (i = 1; i <= Sz(); i++)
                            Console.WriteLine(VD(i));
                        Console.Read();
                        break;
                    case 4:
                        Console.Clear();
                        if(Sz()>0)
                            Console.WriteLine("Deleted string:\n{0}",DD);
                        Console.Read();
                        break;
                    case 5:
                        Console.Clear();
                        if(Sz()>0)
                            Console.WriteLine("Deleted string:\n{0}", DED());
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