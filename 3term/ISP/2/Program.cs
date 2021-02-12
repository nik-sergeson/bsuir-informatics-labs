using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

public class Programm
{
    static void Main()
    {
        Random rnd=new Random();
        Matrix<int> Testmatr = new Matrix<int>(3, 3);
        for (int i = 0; i < 3;i++)
        {
            for (int j = 0; j < 3;j++)
            {
                Testmatr[i].AddVec(new Cell<int> { _value = rnd.Next(80) });
            }
        }
        Testmatr.ShowMatr();
        var OneVec = Testmatr.Where(x => x.Numbers[0]._value == 1);
        foreach (var x in OneVec)
        {
            x.ToString(); 
        }
        var GPAArray = Testmatr.Select(x => x.Cashlength);
        foreach (var x in GPAArray)
        {
            Console.WriteLine(x);
        }

        var LenAr = Testmatr.GroupBy(x => x.Numbers[0]._value);
        LenAr = LenAr.OrderByDescending(x => x.Key);
        foreach (var elem in LenAr)
        {
            Console.WriteLine(elem.Key);
            foreach(var y in elem)
                Console.WriteLine(y.ToString());
        }
        var Arr = Testmatr.ToArray();
        Cell<int> Test = new Cell<int> { _value = 5 };
        Matrix<int> SMatr = new Matrix<int>(3, 3);
        for (int i = 0; i < 3; i++)
        {
            for (int j = 1; j <= 3; j++)
            {
                SMatr[i].AddVec(new Cell<int> { _value = rnd.Next(80) });
            }
        }
        SMatr.ShowMatr();
        var Summ=Testmatr.Summ(SMatr);
        Summ.ShowMatr();
        Matrix<int> Det = new Matrix<int>(2, 2);
        for (int i = 0; i < 2; i++)
        {
            for (int j = 1; j <= 2; j++)
            {
                Det[i].AddVec(new Cell<int> { _value = i+j });
            }
        }
        Console.WriteLine();
        Det.ShowMatr();
        Console.Write(Matrix<int>.Determinant(Det));
        Console.WriteLine();
        Stream s = File.Create(@"D:\2ISP\matr.dat");
        MatrixReaderWriter<int>.BinaryWriting(new BinaryWriter(s), SMatr);
        s.Close();
        FileSystemEventHandler handler = (o, e) =>Console.WriteLine("Someone touched your matrix");
        var watcher = new MyWathcer<int>(@"D:\2ISP", "*.dat", "matr.dat", SMatr, handler);
        if (!File.Exists(@"D:\2ISP\2\matr.dat"))
            File.Copy(@"D:\2ISP\matr.dat", @"D:\2ISP\2\matr.dat");
        Serializer<int>.XmlSerializer(@"D:\2ISP\matr.xml", SMatr);
        var temp=Serializer<int>.XmlDeSerializer(@"D:\2ISP\matr.xml");
        Console.ReadKey();
    }
}