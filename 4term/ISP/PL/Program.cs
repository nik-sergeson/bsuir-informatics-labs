using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using BLL;

namespace PL
{
    class Program
    {
        public static long Combination(long n, long k)
        {
            if (n == k)
                return 1;
            if (k == 0)
                return 1;
            return Combination(n - 1, k - 1) + Combination(n - 1, k);
        }

        public static long Ways(long n, long k)
        {
            long summ = 0;
            for (int i = 0; i < k; i++)
                summ += Combination(k, i) * (long)(Math.Pow((k - i), n)*Math.Pow(-1,i));
            return summ;
        }

        public static long Factorial(long i)
        {
            if (i == 0 || i == 1)
                return 1;
            else
                return i * Factorial(i - 1);
        }

       public static long PartitionFuncB(long n, long k)
        {
            if (k == n)
                return 1;
            if (k == 1)
                return 1;
            if (n < k)
                return 0;
            return PartitionFuncB(n - 1, k - 1) + PartitionFuncB(n - k, k);
        }
         
        public static long PartitionFuncA(long n, long k)
        {
            long summ = 0;
            if (k == 1)
                return 1;
            if (n==1)
                return 1;
            for (long i = 1; i <= k; i++)
                summ += PartitionFuncB(n, i);
            return summ;
        }

        public static long AdvPartitionFunc(long m, long n, long k)
        {
            long summ = 0;
            if (m == n)
                return Factorial(m);
            if (m == 1 && n <= k)
                return 1;
            if (m == 1)
                return 0;
            if (m > n)
                return 0;
            for (long i = 1; i <= k; i++)
                summ += AdvPartitionFunc(m - 1, n - i, k);
            return summ;
        }

        public static  long CharFunc102(long n)
        {
            if (n < 0)
                return 0;
            if (n == 0)
                return 1;
            long summ= CharFunc102(n - 3) + CharFunc102(n - 4) - CharFunc102(n - 10) - CharFunc102(n - 11) + CharFunc102(n - 14);
            return summ;
        }

        static void Main(string[] args)
        {
            long summ = 0;
            for (int i = 1; i <= 7; i++)
                summ += Ways(11, i) / Factorial(i);
           // Console.WriteLine(PartitionFuncB(7, 2));
          //  Console.WriteLine(PartitionFuncA(10,7));
          //  Console.WriteLine(AdvPartitionFunc(4, 21, 8));
         /*   for (int i = -10000; i <= 10000; i++)
            {
                if (i * i * i * i + 6 * i * i * i - 22 * i + 15 == 0)
                    Console.WriteLine(i);
            }*/
            Console.WriteLine(CharFunc102(27));
            Console.Read();
        }
    }
}
