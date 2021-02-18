using System;

class Program
{
    static void Main(string[] args)
    {
        string s;
        int choice;

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
                        QueueMenu<int> Menu = new QueueMenu<int>();
                        Menu.Menu();
                        break;
                    case 2:
                        QueueMenu<double> Menu2 = new QueueMenu<double>();
                        Menu2.Menu();
                        break;
                        
                    case 3:
                        QueueMenu<string> Menu3 =new QueueMenu<string>();
                        Menu3.Menu();
                        break;
                }

            }
        }
    }
}