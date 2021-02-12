using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solver
{
    public class EqualitySolver:ISolver
    {
        protected double[] _values;
        protected int _curpos;

        public EqualitySolver()
        {
            _values = new double[40];
            _curpos = 0;
        }

        public int Priority(char oper)
        {
            switch (oper)
            {
                case '(': return 0;
                case ')': return 0;
                case '+': return 1;
                case '-': return 1;
                case '*': return 2;
                case '/': return 2;
                case '^': return 3;
                default: return 0;
            }
        }

        public string ShuntingYard(string expression)
        {
            Stack<char> operators=new Stack<char>();
            int valuepos = _curpos;
            string opbexpr=string.Empty, curoper=string.Empty;
            for (int i = 0; i < expression.Length; i++)
            {
                if (((expression[i] > 47) && (expression[i] < 59))||(expression[i]==46)||(expression[i]==45))
                {
                    curoper += expression[i];
                }
                else
                {
                    if (!(curoper.Length == 0))
                    {
                        _values[valuepos] = double.Parse(curoper);
                        if (valuepos != 0)
                        {
                            opbexpr += ',';
                        }
                        curoper = string.Empty;
                        opbexpr += valuepos.ToString();
                        valuepos++;
                    }
                    if (operators.Count == 0)
                    {
                        operators.Push(expression[i]);
                    }
                    else if ((expression[i] >= 'a') && (expression[i] <= 'z'))
                    {
                        operators.Push(expression[i]);
                    }

                    else if (expression[i] == '(')
                    {
                        operators.Push(expression[i]);
                    }
                    else if (expression[i] == ')')
                    {
                        char sttop = operators.Pop();
                        while (sttop != '(')
                        {
                            opbexpr += sttop;
                            sttop = operators.Pop();
                        }
                        sttop = operators.Pop();
                        if ((sttop >= 'a') && (sttop <= 'z'))
                        {
                            opbexpr += sttop;
                        }
                        else
                        {
                            operators.Push(sttop);
                        }
                    }
                    else
                    {
                        char symb = operators.Pop();
                        int stprior = Priority(symb);
                        int exprprior = Priority(expression[i]);
                        while (stprior >= exprprior)
                        {
                            opbexpr += symb;
                            symb = operators.Pop();
                            stprior = Priority(symb);
                        }
                        operators.Push(symb);
                        operators.Push(expression[i]);
                    }

                }
            }
            if (!(curoper.Length == 0))
            {
                if (valuepos != 0)
                {
                    if ((opbexpr[opbexpr.Length - 1] >= '0') && (opbexpr[opbexpr.Length - 1] <= 9))
                    {
                        opbexpr += ',';
                    }
                }
                _values[valuepos] = double.Parse(curoper);
                curoper = string.Empty;
                opbexpr += valuepos.ToString();
                valuepos++;
            }
            while (operators.Count != 0)
            {
                opbexpr += operators.Pop();
            }
            _curpos = valuepos;
            return opbexpr;
        }

        public virtual double CountEquality(string opb)
        {
            string curindex = string.Empty;
            double op1, op2;
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
                            case 's':operands.Push(Math.Sin(op1));
                                break;
                            case 'c':operands.Push(Math.Cos(op1));
                                break;
                            case 'e':operands.Push(Math.Exp(op1));
                                break;
                            case 'l':operands.Push(Math.Log(op1,Math.E));
                                break;
                            case 't':operands.Push(Math.Atan(op1));
                                break;
                            case 'r':operands.Push(Math.Asin(op1));
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
    }
}
