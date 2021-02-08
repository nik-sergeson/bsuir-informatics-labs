using System;

public static class MatrixSolv 
{

	/// <summary>
	/// вычесление определителя
	/// </summary>
	/// <param name="Matr"></param>
	/// <returns></returns>
    public static double Determinant(double[,] Matr) 
    {

        return Matr[0, 0] * Matr[1, 1] * Matr[2, 2] + Matr[0, 1] * Matr[1, 2] * Matr[2, 0] + Matr[1, 0] * Matr[2, 1] * Matr[0, 2] - (Matr[2, 0] * Matr[1, 1] * Matr[0, 2] + Matr[0, 0] * Matr[1, 2] * Matr[2, 1] + Matr[0, 1] * Matr[1, 0] * Matr[2, 2]);
    }

	/// <summary>
	/// вычесление обратной матрицы
	/// </summary>
	/// <param name="Matr"></param>
	/// <returns></returns>
    public static double[,] RevMatr(double[,] Matr) 
    {
        double det, a00, a01, a02, a10, a11, a12, a20, a21, a22;

        det = Determinant(Matr);
        if (det == 0)
            return null;
        else
        {
            a00 = Matr[1, 1] * Matr[2, 2] - Matr[2, 1] * Matr[1, 2];
            a01 = -Matr[1, 0] * Matr[2, 2] + Matr[2, 0] * Matr[1, 2];
            a02 = Matr[1, 0] * Matr[2, 1] - Matr[2, 0] * Matr[1, 1];
            a10 = -Matr[0, 1] * Matr[2, 2] + Matr[2, 1] * Matr[0, 2];
            a11 = Matr[0, 0] * Matr[2, 2] - Matr[2, 0] * Matr[0, 2];
            a12 = -Matr[0, 0] * Matr[2, 1] + Matr[2, 0] * Matr[0, 1];
            a20 = Matr[0, 1] * Matr[1, 2] - Matr[1, 1] * Matr[0, 2];
            a21 = -Matr[0, 0] * Matr[1, 2] + Matr[1, 0] * Matr[0, 2];
            a22 = Matr[0, 0] * Matr[1, 1] - Matr[1, 0] * Matr[0, 1];
            return new double[3, 3] { { a00 / det, a10 / det, a20 / det }, { a01 / det, a11 / det, a21 / det }, { a02 / det, a12 / det, a22 / det } };
        }
    }
}