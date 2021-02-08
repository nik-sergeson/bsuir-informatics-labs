using System;
using System.Globalization;

public class Vector:IEquatable<Vector>,IComparable<Vector>, IFormattable 
{
    public double Xpr{get;set;}
    public double Ypr{get;set;}
    public double Zpr { get; set; }
	public Point Fpoint { get; set; }
	private const double xTodegr=57.3248;
	/// <summary>
	/// получение длины
	/// </summary>
	/// <returns></returns>
    public double GetLength()
    {
        return Math.Sqrt(Math.Pow(Xpr, 2.0) + Math.Pow(Ypr, 2.0) + Math.Pow(Zpr, 2.0));
    }

	/// <summary>
	/// вычисление угла с осью  ох
	/// </summary>
	/// <returns></returns>
    public double GetXAngle() 
    {
        return Math.Acos(Xpr / GetLength())*xTodegr;
    }

	/// <summary>
	/// вычисление угла с осью оу
	/// </summary>
	/// <returns></returns>
    public double GetYAngle() 
    {
        return Math.Acos(Ypr / GetLength())*xTodegr;
    }

	/// <summary>
	/// вычисление угла с осью oz
	/// </summary>
	/// <returns></returns>
    public double GetZAngle() 
    {
        return Math.Acos(Zpr / GetLength())*xTodegr;
    }
/// <summary>
/// проверка вектора
/// </summary>
/// <param name="Fpoint"></param>
/// <param name="Spoint"></param>
/// <returns></returns>
    public static Vector CheckVec(Point Fpoint, Point Spoint) 
    {
        if ((Fpoint == null) || (Spoint == null))
            return null;
        else
            return new Vector(Fpoint, Spoint);
    }

    public Vector(double Xpr, double Ypr, double Zpr,Point Fpoint) 
	{
        this.Xpr = Xpr;
        this.Ypr = Ypr;
        this.Zpr = Zpr;
        this.Fpoint = Fpoint;
    }

	/// <summary>
	/// конструктор по точкам
	/// </summary>
	/// <param name="Fpoint"></param>
	/// <param name="Spoint"></param>
    public Vector(Point Fpoint, Point Spoint) 
    {
        Xpr = Spoint.X - Fpoint.X;
        Ypr = Spoint.Y - Fpoint.Y;
        Zpr = Spoint.Z - Fpoint.Z;
        this.Fpoint = Fpoint;
    }

    public override string ToString()
    {
       return string.Format("({0:0.00}; {1:0.00}; {2:0.00})",Xpr,Ypr,Zpr);
    }

	/// <summary>
	/// сложение векторов
	/// </summary>
	/// <param name="a"></param>
	/// <param name="b"></param>
	/// <returns></returns>
    public static Vector operator +(Vector a, Vector b) 
    {
        return new Vector(a.Xpr + b.Xpr,a.Ypr + b.Ypr,a.Zpr + b.Zpr,a.Fpoint);
    }

	/// <summary>
	/// произведение вкктора на число
	/// </summary>
	/// <param name="a"></param>
	/// <param name="SVec"></param>
	/// <returns></returns>
    public static Vector operator *(double a, Vector SVec) 
    {
        if (a == 0)
            return null;
        else
            return new Vector(a * SVec.Xpr, a * SVec.Ypr, a * SVec.Zpr,SVec.Fpoint);
    }

	/// <summary>
	/// скалярное произведение
	/// </summary>
	/// <param name="b"></param>
	/// <returns></returns>
    public double ScalMul(Vector b) 
    {
        return this.Xpr * b.Xpr + this.Ypr * b.Ypr + this.Zpr * b.Zpr;
    }

	/// <summary>
	/// векторное произведение
	/// </summary>
	/// <param name="b"></param>
	/// <returns></returns>
    public Vector VecMul(Vector b) 
    {
        double xpvec, ypvec, zpvec;

        xpvec = this.Ypr * b.Zpr - b.Ypr * this.Zpr;
        ypvec = this.Xpr * b.Zpr - b.Xpr * this.Zpr;
        zpvec = this.Xpr * b.Ypr - b.Xpr * this.Ypr;

        if ((xpvec == 0) && (ypvec == 0) && (zpvec == 0))
            return null;
        else
            return new Vector(xpvec, ypvec, zpvec,this.Fpoint);
    }

	/// <summary>
	/// проверка на принадлежность плоскости
	/// </summary>
	/// <param name="Pl"></param>
	/// <returns></returns>
    public bool VecOnPlane(Plane Pl) 
    {
        double POnPlane,VecPerp;

        if (Pl != null)
        {
            POnPlane = Pl.A * Fpoint.X + Pl.B * Fpoint.Y + Pl.C * Fpoint.Z + Pl.D;
            VecPerp = Pl.A * Xpr + Pl.B * Ypr + Pl.C * Zpr;
            if ((POnPlane == 0) && (VecPerp == 0))
                return true;
            else
                return false;
        }
        else return false;
    }
    /// <summary>
    /// находим перпендикулярный
    /// </summary>
    /// <returns></returns>
    public Vector PerpVec(){
    	
    	return new Vector(1,1,-(this.Xpr+this.Ypr)/this.Zpr,Fpoint=this.Fpoint);
    }

	/// <summary>
	/// угол между векторами
	/// </summary>
	/// <param name="b"></param>
	/// <returns></returns>
    public double AngBtwVec(Vector b)
    {
        return Math.Acos(this.ScalMul(b) / (this.GetLength() * b.GetLength()));
    }

    public bool Equals(Vector b){

        if (b == null)
            return false;
        else
            return ((Xpr==b.Xpr)&&(Ypr==b.Ypr)&&(Zpr==b.Zpr));
    }

    public static bool operator ==(Vector a, Vector b)
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

    public static bool operator !=(Vector a, Vector b)
    {
        return !(a==b);
    }

    public int CompareTo(Vector b)
    {
        if (b == null)
            return (int)this.GetLength();
        else
            return (int)(GetLength() - b.GetLength());
    }

    public static bool operator >(Vector a, Vector b)
    {
        if (a == null)
            return false;
        return a.CompareTo(b) > 0;
    }

    public static bool operator <(Vector a, Vector b)
    {
        if (a == null)
            return false;
        return a.CompareTo(b) < 0;
    }

	public string ToString(string format, IFormatProvider provider)
	{
		if (String.IsNullOrEmpty(format)) format = "С";
		if (provider == null) provider = CultureInfo.CurrentCulture;
		switch (format)
		{
			case "A":
				return "[ " + Math.Round(GetLength(), 2).ToString(provider) + ": " + Math.Round(GetXAngle(), 2).ToString(provider)
					+ "; " + Math.Round((GetYAngle()), 2).ToString(provider) + "; "
					+ Math.Round((GetZAngle()), 2).ToString() + ']';
			case "C":
				return "( " + Math.Round(Xpr, 2).ToString(provider) + "; " + Math.Round(Ypr, 2).ToString(provider) + "; " + Math.Round(Zpr, 2).ToString(provider) + ')';
			default:
				return "";
		}
	}
}