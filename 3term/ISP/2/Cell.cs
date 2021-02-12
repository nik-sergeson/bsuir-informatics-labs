using System;
using System.IO;
using System.IO.Compression;
using System.Runtime.Serialization;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime;

[Serializable]
[DataContract]
public class Cell<Datatype>:IEquatable<Cell<Datatype>>
    where Datatype:struct
{
    [DataMember]
    public Datatype _value{get; set;}

    public static Datatype operator +(Cell<Datatype> FVal,Cell<Datatype> SVal)
    {
        dynamic a = FVal._value, b = SVal._value;
        return a + b;
    }

    public static Datatype operator +(Cell<Datatype> FVal,Datatype SVal)
    {
        dynamic a = FVal._value, b = SVal;
        return a + b;
    }

    public static Datatype operator *(Cell<Datatype> FVal, Cell<Datatype> SVal)
    {
        dynamic a = FVal._value, b = SVal._value;
        return a * b;
    }

    public static Datatype operator *(Cell<Datatype> FVal, Datatype SVal)
    {
        dynamic a = FVal._value, b = SVal;
        return a * b;
    }

    public static Datatype operator *(int FVal, Cell<Datatype> SVal)
    {
        dynamic a = FVal, b = SVal._value;
        return a * b;
    }

    public static Datatype operator -(Cell<Datatype> FVal)
    {
        dynamic a = FVal._value;
        return -a;
    }

    public bool Equals(Datatype OtherNum)
    {
        dynamic a = this._value, b = OtherNum;
        return a == b;
    }

    public bool Equals(Cell<Datatype> OtherNum)
    {
        dynamic a = this._value, b = OtherNum._value;
        return a == b;
    }

    public Cell()
    {
        _value = default(Datatype);
    }

    public override string ToString()
    {
        return _value.ToString();
    }

    public static bool TryParse(string str)
    {
        dynamic a = default(Datatype);
        Datatype b;
        try
        {
           b=(Datatype)Convert.ChangeType(str, typeof(Datatype));
           return true;
        }
        catch
        {
            return false; 
        }
    }

    public static Datatype Parse(string str)
    {
        dynamic a = default(Datatype);
        return (Datatype)Convert.ChangeType(str, typeof(Datatype));
    }
}