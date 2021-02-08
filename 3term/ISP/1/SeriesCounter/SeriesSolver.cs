using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Solver;
using System.Threading.Tasks;

namespace SeriesSolver
{
    [Myattribute("SeriesSolver", Build = "2.0")]
    public class SeriesSolver:EqualitySolver,ISolver
    {
        public double _epsilon{get; set;}

        public SeriesSolver():base()
        {
            _epsilon=0.001;
        }

        public override double CountEquality(string opb)
        {
            string curindex = string.Empty;
            double op1, op2,res=0;
            int n;
            Stack<double> operands=new Stack<double>();
            for (int i = 0; i < opb.Length; i++)
            {
                if ((opb[i] >= '0') && (opb[i] <= '9'))
                {
                    curindex += opb[i];
                }
                else if (opb[i] == ',')
                {
                    operands.Push( _values[Int32.Parse(curindex)]);
                    curindex = string.Empty;
                }
                else{
                    operands.Push( _values[Int32.Parse(curindex)]);
                    curindex = string.Empty;
                    op1=operands.Pop();
                    if((opb[i]>='a')&&(opb[i]<='z')){
                        switch(opb[i]){
                            case 's':
                                n=0;
                                double xn=Math.Pow(-1,n)*Math.Pow(op1,2*n+1)/Factorial(2*n+1);
                                n++;
                                while(xn>_epsilon)
                                {
                                    res+=xn;
                                    xn=Math.Pow(-1,n)*Math.Pow(op1,2*n+1)/Factorial(2*n+1);
                                    n++;
                                }
                                operands.Push(res);
                                res=0;
                                break;
                            case 'c':
                                n=0;
                                xn=Math.Pow(-1,n)*Math.Pow(op1,2*n)/Factorial(2*n);
                                n++;
                                while(xn>_epsilon)
                                {
                                    res+=xn;
                                    xn=Math.Pow(-1,n)*Math.Pow(op1,2*n)/Factorial(2*n);
                                    n++;
                                }
                                operands.Push(res);
                                res=0;
                                break;
                            case 'e':
                                n=0;
                                xn=Math.Pow(op1,n)/Factorial(n);
                                n++;
                                while(xn>_epsilon)
                                {
                                    res+=xn;
                                    xn=Math.Pow(op1,n)/Factorial(n);
                                    n++;
                                }
                                operands.Push(res);
                                res=0;
                                break;
                            case 'l':
                                op1=op1-1;
                                n=0;
                                xn=Math.Pow(-1,n)*Math.Pow(op1,n+1)/(n+1);
                                n++;
                                while(xn>_epsilon)
                                {
                                    res+=xn;
                                    xn=Math.Pow(-1,n)*Math.Pow(op1,n+1)/n+1;
                                    n++;
                                }
                                operands.Push(res);
                                res=0;
                                break;
                            case 't':
                                n=0;
                                xn=Math.Pow(-1,n)*Math.Pow(op1,2*n+1)/(2*n+1);
                                n++;
                                while(xn>_epsilon)
                                {
                                    res+=xn;
                                    xn=Math.Pow(-1,n)*Math.Pow(op1,2*n+1)/(2*n+1);
                                    n++;
                                }
                                operands.Push(res);
                                res=0;
                                break;
                            case 'r':
                                n=0;
                                xn=Math.Pow(op1,2*n+1)/(2*n+1);
                                n++;
                                while(xn>_epsilon)
                                {
                                    res+=xn;
                                    xn=SpecFactorial(n)*Math.Pow(op1,2*n+1);
                                    n++;
                                }
                                operands.Push(res);
                                res=0;
                                break;
                            default:operands.Push(0);
                                break;
                        }
                    }
                    else{
                        op2=operands.Pop();
                            switch(opb[i]){
                                case '+': operands.Push(op1+op2);
                                    break;
                                case '-': operands.Push(op1-op2);
                                    break;
                                case '*': operands.Push(op1*op2);
                                    break;
                                case '/': operands.Push(op1/op2);
                                    break;
                                case '^': operands.Push(Math.Pow(op1,op2));
                                    break;
                                default: operands.Push(0);
                                    break;
                            }                        
                    }
                }
            }
            return operands.Pop();
        }

        private int Factorial(int i)
        {
            int res=1;
            for (int j = i; j > 1; j--)
                res *= i;
            return res;
        }

        private double SpecFactorial(int i)
        {
            double res = 1;
            for (int j = 1; j <= i; j += 2)
            {
                res = res * j / (j + 1);
            }
            return res;
        }
    }
}
