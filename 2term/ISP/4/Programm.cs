using System;

class trymyclass
{

    static void Main()
    {
        string s = string.Empty;

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
                    QueueMenu Start = new QueueMenu();
                    Start.Menu();
                    break;
                case 'd':
                    DeqMenu Startd = new DeqMenu();
                    Startd.Menu();
                    break;
            }
        }
    }
}