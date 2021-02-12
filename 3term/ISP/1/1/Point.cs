using System;

public class Point:IEquatable<Point>,IComparable<Point>{

    public double X { get; set; }
    public double Y { get; set; }
    public double Z { get; set; }
    
    public double GetLength(){
    	return Math.Sqrt(Math.Pow(X,2.0)+Math.Pow(Y,2.0)+Math.Pow(Z,2.0));
    }

    public override string ToString()
    {
        return "(" + X.ToString() + "," + Y.ToString() + "," + Z.ToString() + ")";
    }

	/// <summary>
	/// парсинг
	/// </summary>
	/// <param name="str"></param>
	/// <returns></returns>
    public static Point Pparse(string str)
    {

        char sep = ' ';
        double CoorP;

        string[] numbers = str.Split(sep);
        if (numbers.Length != 3)
            return null;
        else
        {
            if (!(double.TryParse(numbers[0], out CoorP)))
                return null;
            else if (!(double.TryParse(numbers[1], out CoorP)))
                return null;
            else if (!(double.TryParse(numbers[2], out CoorP)))
                return null;
            else return new Point { X = double.Parse(numbers[0]), Y =double.Parse(numbers[1]), Z = double.Parse(numbers[2]) };
        }
    }
    
     public bool Equals(Point b){

        if (b == null)
            return false;
        else
            return ((X==b.X)&&(Y==b.Y)&&(Z==b.Z));
    }

    public static bool operator ==(Point a, Point b)
    {
        try
        {
            return a.Equals(b);
        }
        catch (NullReferenceException)
        {
            try
            {
                return b.Equals(a);
            }
            catch (NullReferenceException)
            {
                return true;
            }
        }
    }

    public static bool operator !=(Point a, Point b)
    {
        return !(a==b);
    }

    public int CompareTo(Point b)
    {
        if (b == null)
            return (int)this.GetLength();
        else
            return (int)(GetLength() - b.GetLength());
    }

    public static bool operator >(Point a, Point b)
    {
        if (a == null)
            return false;
        return a.CompareTo(b) > 0;
    }

    public static bool operator <(Point a, Point b)
    {
        if (a == null)
            return false;
        return a.CompareTo(b) < 0;
    }
}