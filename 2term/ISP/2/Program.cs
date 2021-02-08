using System;

class Count
{
    static void Main()
    {
        int Length = 1;
        double[] data = new double[Length];
        ConsoleKeyInfo keypress;
        double X, Y, Z;
        string s;

        do
        {           
            Console.Write("Input X: \n");
            s = Console.ReadLine();
            while (double.TryParse(s, out X) == false)
            {
                Console.WriteLine("Wrong value");
                Console.Write("Input X: \n");
                s = Console.ReadLine();
            }
            X = double.Parse(s);   
            Console.Write("Input Y: \n");
            s = Console.ReadLine();
            while (double.TryParse(s, out X) == false)
            {
                Console.WriteLine("Wrong value");
                Console.Write("Input Y: \n");
                s = Console.ReadLine();
            }
            Y = double.Parse(s);           
            Console.Write("Input Z: \n");
            s = Console.ReadLine();
            while (double.TryParse(s, out X) == false)
            {
                Console.WriteLine("Wrong value");
                Console.Write("Input X: \n");
                s = Console.ReadLine();
            }
            Z = double.Parse(s);           
            data[Length - 1] = Math.Pow(Math.Abs(Math.Cos(X) - Math.Cos(Y)), (1 + 2 * Math.Pow(Math.Sin(Y), 2))) * (1 + Z + Math.Pow(Z, 2) / 2 + Math.Pow(Z, 3) / 3 + Math.Pow(Z, 4) / 4);
            if (data[Length - 1] == double.NaN)
                Length--;
            else
                Console.WriteLine("w={0:F2}", data[Length - 1]);            
            keypress = Console.ReadKey();
            Console.Clear();
            Length++;
            Array.Resize(ref data, Length);
        }
        while (keypress.Key != ConsoleKey.Escape);
    }
}