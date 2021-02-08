using System;
using System.Globalization;

public class Plane:IEquatable<Plane>,IComparable<Plane>,IFormattable
{
    public double A { get; set; }
    public double B { get; set; }
    public double C { get; set; }
    public double D { get; set; }
    
    /// <summary>
    /// длинна перпендикулярного вектора
    /// </summary>
    /// <returns></returns>
    public double GetLength(){
    	
    	return Math.Sqrt(Math.Pow(A,2.0)+Math.Pow(B,2.0)+Math.Pow(C,2.0));
    }

    public override string ToString() 
    {
    	return string.Format("({0:0.00})*x+({1:0.00})*y+({2:0.00})*z+({3:0.00})=0",A,B,C,D);
    }

	/// <summary>
	/// парсинг
	/// </summary>
	/// <param name="str"></param>
	/// <returns></returns>
    public static Plane Pparse(string str) 
    {

        char sep = ' ';
        double CoorP;

        string[] numbers = str.Split(sep);
        if (numbers.Length != 4)
            return null;
        else
        {
            if (!(double.TryParse(numbers[0], out CoorP)))
                return null;
            else if (!(double.TryParse(numbers[1], out CoorP)))
                return null;
            else if (!(double.TryParse(numbers[2], out CoorP)))
                return null;
            else if (!(double.TryParse(numbers[3], out CoorP)))
                return null;
            else return new Plane { A = double.Parse(numbers[0]), B = double.Parse(numbers[1]), C = double.Parse(numbers[2]), D = double.Parse(numbers[3]) };
        }
    }
    
     public bool Equals(Plane b){

        if (b == null)
            return false;
        else
            return ((A==b.A)&&(this.B==b.B)&&(C==b.C)&&(D==b.D));
    }

    public static bool operator ==(Plane a, Plane b)
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

    public static bool operator !=(Plane a, Plane b)
    {
        return !(a==b);
    }

    public int CompareTo(Plane b)
    {
        if (b == null)
            return (int)this.GetLength();
        else
            return (int)(GetLength() - b.GetLength());
    }

    public static bool operator >(Plane a, Plane b)
    {
        if (a == null)
            return false;
        return a.CompareTo(b) > 0;
    }

    public static bool operator <(Plane a, Plane b)
    {
        if (a == null)
            return false;
        return a.CompareTo(b) < 0;
    }
    
    public string ToString(string format, IFormatProvider provider)
	{
    	double m;
		if (String.IsNullOrEmpty(format)) format = "С";
		if (provider == null) provider = CultureInfo.CurrentCulture;
		switch (format)
		{
			case "A":
				return "(" + Math.Round(A, 2).ToString(provider) + ")*x+(" + Math.Round(B, 2).ToString(provider)
					+ "*)y+(" + Math.Round(C, 2).ToString(provider) + ")*z+("+Math.Round(D, 2).ToString() + ")=0";
			case "B":
				return "x/(" + Math.Round(-A/D, 2).ToString(provider) + ")+y/(" + Math.Round(-B/D, 2).ToString(provider) + ")+z/(" + Math.Round(-C/D, 2).ToString(provider) + ")=1";
			case "C":
				m=(-Math.Sign(D)/GetLength());
				return "(" + Math.Round(A*m, 2).ToString(provider) + ")*x+(" + Math.Round(B*m, 2).ToString(provider)+ "*)y+(" + Math.Round(C*m, 2).ToString(provider) + ")*z+("+Math.Round(D*m, 2).ToString() + ")=0";
			default:
				return "";
		}
	}
}
