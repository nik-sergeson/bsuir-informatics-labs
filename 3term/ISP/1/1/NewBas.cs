using System;

public class NewBas
{

    /// <summary>
	/// матрица перехода к новому базису
    /// </summary>
	private double[,] MatrNB; 
    public double this[int i, int j]
    {
        get
        {
            return MatrNB[i, j];
        }
        set
        {
            MatrNB[i,j] = value;
        }
    }

    /// <summary>
	/// непосредственный переход к новуму базису
    /// </summary>
    /// <param name="a"></param>
	public void MovNB(Vector a) 
    {

        a.Fpoint.X = MatrNB[0, 0] * a.Fpoint.X + MatrNB[0, 1] * a.Fpoint.Y + MatrNB[0, 2] * a.Fpoint.Z;
        a.Fpoint.Y = MatrNB[1, 0] * a.Fpoint.X + MatrNB[1, 1] * a.Fpoint.Y + MatrNB[1, 2] * a.Fpoint.Z;
        a.Fpoint.Z = MatrNB[2, 0] * a.Fpoint.X + MatrNB[2, 1] * a.Fpoint.Y + MatrNB[2, 2] * a.Fpoint.Z;
        a.Xpr = MatrNB[0, 0] * a.Xpr + MatrNB[0, 1] * a.Ypr + MatrNB[0, 2] * a.Zpr;
        a.Ypr = MatrNB[1, 0] * a.Xpr + MatrNB[1, 1] * a.Ypr + MatrNB[1, 2] * a.Zpr;
        a.Zpr = MatrNB[2, 0] * a.Xpr + MatrNB[2, 1] * a.Ypr + MatrNB[2, 2] * a.Zpr;
    }

	/// <summary>
	/// вычисление матрицы поворота вектора
	/// </summary>
	/// <param name="a"></param>
	/// <param name="b"></param>
	/// <param name="g"></param>
    public NewBas(double a, double b, double c) 
    {

        MatrNB = new double[3, 3];
        MatrNB[0, 0] = Math.Cos(b) * Math.Cos(c);
        MatrNB[0, 1] = -Math.Cos(b)*Math.Sin(c);
        MatrNB[0, 2] =Math.Sin(b);
        MatrNB[1, 0] = Math.Sin(a)*Math.Sin(b)*Math.Cos(c)+Math.Cos(a)*Math.Sin(c);
        MatrNB[1, 1] = -Math.Sin(a)*Math.Sin(b)*Math.Sin(c)+Math.Cos(a)*Math.Cos(c);
        MatrNB[1, 2] =- Math.Cos(b) * Math.Sin(a);
        MatrNB[2, 0] = -Math.Sin(b)*Math.Cos(a)*Math.Cos(c)+Math.Sin(a)*Math.Sin(c);
        MatrNB[2, 1] = Math.Cos(a)*Math.Sin(b)*Math.Sin(c)+Math.Sin(a)*Math.Cos(c);
        MatrNB[2, 2] = Math.Cos(a)*Math.Cos(b);

    }
/// <summary>
/// заполнение матрицы перехода к новому базису
/// </summary>
/// <param name="a"></param>
/// <param name="b"></param>
/// <param name="c"></param>
/// <param name="d"></param>
/// <param name="e"></param>
/// <param name="f"></param>
/// <param name="g"></param>
/// <param name="h"></param>
/// <param name="k"></param>
    public NewBas(double a, double b, double c, double d, double e, double f, double g, double h, double k)
    {

        MatrNB = new double[3, 3];
        MatrNB[0, 0] = a;
        MatrNB[0, 1] = b;
        MatrNB[0, 2] =c;
        MatrNB[1, 0] = d;
        MatrNB[1, 1] = e;
        MatrNB[1, 2] = f;
        MatrNB[2, 0] = g;
        MatrNB[2, 1] = h;
        MatrNB[2, 2] = k;
        MatrNB = MatrixSolv.RevMatr(MatrNB);
    }

    /// <summary>
	/// представленипе в виде строки
    /// </summary>
    /// <returns></returns>
	public override string ToString() 
    {
         return string.Format("{0:0.00}  {1:0.00}  {2:0.00}\r\n{3:0.00}  {4:0.00}  {5:0.00}\r\n{6:0.00}  {7:0.00}  {8:0.00}",MatrNB[0, 0],MatrNB[0, 1],MatrNB[0, 2],MatrNB[1, 0],MatrNB[1, 1],MatrNB[1, 2],MatrNB[2, 0],MatrNB[2, 1],MatrNB[2, 2]);
    }

	/// <summary>
	/// парсинг входных данных
	/// </summary>
	/// <param name="str"></param>
	/// <returns></returns>
    public static NewBas Bparse(string str) 
    {

        char sep = ' ';
        double CoorP;

        string[] numbers = str.Split(sep);
        if ((numbers.Length != 3) && (numbers.Length != 9))
            return null;
        else
        {
            if (numbers.Length == 3)
            {
                if (!(double.TryParse(numbers[0], out CoorP)))
                    return null;
                else if (!(double.TryParse(numbers[1], out CoorP)))
                    return null;
                else if (!(double.TryParse(numbers[2], out CoorP)))
                    return null;
                else return new NewBas(double.Parse(numbers[0]), double.Parse(numbers[1]), double.Parse(numbers[2]));
            }
            else
            {
                if (!(double.TryParse(numbers[0], out CoorP)))
                    return null;
                else if (!(double.TryParse(numbers[1], out CoorP)))
                    return null;
                else if (!(double.TryParse(numbers[2], out CoorP)))
                    return null;
                if (!(double.TryParse(numbers[3], out CoorP)))
                    return null;
                else if (!(double.TryParse(numbers[4], out CoorP)))
                    return null;
                else if (!(double.TryParse(numbers[5], out CoorP)))
                    return null;
                if (!(double.TryParse(numbers[6], out CoorP)))
                    return null;
                else if (!(double.TryParse(numbers[7], out CoorP)))
                    return null;
                else if (!(double.TryParse(numbers[8], out CoorP)))
                    return null;
                else return new NewBas(double.Parse(numbers[0]), double.Parse(numbers[1]), double.Parse(numbers[2]), double.Parse(numbers[3]), double.Parse(numbers[4]),
                   double.Parse(numbers[5]), double.Parse(numbers[6]), double.Parse(numbers[7]), double.Parse(numbers[8]));
            }
        }
    }
}