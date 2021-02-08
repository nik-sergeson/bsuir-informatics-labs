using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Security.Cryptography;
using System.Runtime.Serialization.Formatters.Binary;
using System.Runtime.Serialization;
using System.Xml.Serialization;

public static class Serializer<Datatype>
    where Datatype:struct
{
    public static void BinarySerializer(string fileName, MatrixToXml<Datatype> matr)
    {
        var formatter = new BinaryFormatter();
        using (Stream stream = File.Create(fileName))
        {
            formatter.Serialize(stream, matr);
        }
    }

    public static MatrixToXml<Datatype> BinaryDeserializer(string fileName)
    {
        MatrixToXml<Datatype> xt = new MatrixToXml<Datatype>();
        var formatter = new BinaryFormatter();
        using (Stream stream = File.OpenRead(fileName))
        {
            xt = (MatrixToXml<Datatype>)formatter.Deserialize(stream);
        }
        return xt;
    }


    public static void ContractSerializer(string fileName, MatrixToXml<Datatype> t)
    {
        var ds = new DataContractSerializer(typeof(MatrixToXml<Datatype>));
        using (Stream s = File.Create(fileName))
        {
            ds.WriteObject(s, t);
        }
    }

    public static MatrixToXml<Datatype> ContractDeserializer(string fileName)
    {
        MatrixToXml<Datatype> xt = new MatrixToXml<Datatype>();
        var ds = new DataContractSerializer(typeof(MatrixToXml<Datatype>));
        using (Stream s = File.OpenRead(fileName))
        {
            xt = (MatrixToXml<Datatype>)ds.ReadObject(s);
        }
        return xt;
    }

    public static void XmlSerializer(string fileName, Matrix<Datatype> t)
    {
        var serializer = new XmlSerializer(typeof(Matrix<Datatype>));
        using (Stream stream = File.Create(fileName))
        {
            serializer.Serialize(stream, t);
        }
    }

    public static Matrix<Datatype> XmlDeSerializer(string fileName)
    {
        MatrixToXml<Datatype> xt = new MatrixToXml<Datatype>();
        var serializer = new XmlSerializer(typeof(Matrix<Datatype>));
        using (Stream stream = File.OpenRead(fileName))
        {
            serializer.Deserialize(stream);
        }
        return xt;
    }
}