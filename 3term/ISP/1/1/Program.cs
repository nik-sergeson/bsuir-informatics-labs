using System;

class Tryclass{
     static void Main(){
         Point Fpoint, Spoint;
         Vector Fvec,Svec;
         double MulNum,D;
         Plane Splane;
         NewBas Bas;

        Fpoint = Point.Pparse("1 1 1");
        Spoint = Point.Pparse("10 10 10");
		
        Svec =Vector.CheckVec(Fpoint, Spoint);
        Console.WriteLine("{0:A}",Svec);
		Console.WriteLine("{0:C}",Svec);
		if (Svec != null)
        {
            Console.WriteLine("\r\nLength:{0:0.00}", Svec.GetLength());
            Console.WriteLine("Angle between X axis:{0:0.00}", Svec.GetXAngle());
            Console.WriteLine("Angle between Y axis:{0:0.00}", Svec.GetYAngle());
            Console.WriteLine("Angle between Z axis:{0:0.00}", Svec.GetZAngle());
			MulNum = 5;
			Svec = MulNum * Svec;
			Console.WriteLine("{0:0.00}*Vec="+Svec.ToString(),MulNum);
        }
        Spoint = Point.Pparse("0 0 0");
        Fpoint = Point.Pparse("-5 1 6");
        Fvec = Vector.CheckVec(Fpoint, Spoint);
        if (Fvec != null){
        	Console.WriteLine();
			Console.WriteLine("{0:C}",Fvec);
            Console.WriteLine("Scalar multiplication={0:0.00}", Fvec.ScalMul(Svec));
            Console.WriteLine("Scalar multiplication={0:0.00}", Svec.ScalMul(Fvec));
            Console.WriteLine("Vector multiplication="+(Svec.VecMul(Fvec)).ToString());
            Console.WriteLine("Vector multiplication="+ (Fvec.VecMul(Svec)).ToString());
        }
        Splane = Plane.Pparse("100 0 50 -5");
        if (Splane != null)
        {
        	Console.WriteLine("{0:A}",Splane);
            Console.WriteLine("Vector belong to plane:{0:0.00}", Svec.VecOnPlane(Splane));
        }
        else
        Console.WriteLine("Wrong value");
        D=-(Svec.Xpr*Svec.Fpoint.X+Svec.Ypr*Svec.Fpoint.Y+Svec.Zpr*Svec.Fpoint.Z);
        Splane = Plane.Pparse((Svec.Xpr).ToString()+' '+(Svec.Ypr).ToString()+' '+(Svec.Xpr).ToString()+' '+D.ToString());
        if (Splane != null)
        {
        	Console.WriteLine(Splane.ToString());
        	Console.WriteLine("Vector belong to plane:{0:0.00}", (Svec.PerpVec()).VecOnPlane(Splane));
        }
        else
        Console.WriteLine("Wrong value");
        Console.WriteLine();
		Console.WriteLine("{0:C}",Fvec);
		Console.WriteLine("{0:C}",Svec);
		Console.WriteLine();
		Console.WriteLine("Rotation matrix");
        Bas = NewBas.Bparse("0 0 0");
        if (Bas != null)
        {           
            Console.WriteLine( Bas.ToString());
            Bas.MovNB(Fvec);
			Console.WriteLine();
            Bas.MovNB(Svec);
            Console.WriteLine("{0:C}",Fvec);
			Console.WriteLine("{0:C}",Svec);
        }
        else
            Console.WriteLine("Wrong value");
		Console.WriteLine();
		Bas = NewBas.Bparse("1 0 3 1 2 5 2 1 3");
		Console.WriteLine("Matrix of new basis");
		if (Bas != null)
		{		
			Console.WriteLine(Bas.ToString());
			Console.WriteLine();
			Bas.MovNB(Fvec);
			Bas.MovNB(Svec);
			Console.WriteLine("{0:C}",Fvec);
		Console.WriteLine("{0:C}",Svec);
		}
		else
			Console.WriteLine("Wrong value");
		Console.ReadLine();
     }
 }