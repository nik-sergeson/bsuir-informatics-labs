using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.IO.Compression;
using System.Security;
using System.Security.Cryptography;

static class MatrixReaderWriter<Celltype>
    where Celltype : struct
{
    static byte[] keys, iv;
    private static int _size;

    public static void SetSize(int size)
    {
        _size = size;
    }

    public static void BinaryWriting(BinaryWriter binarywriter, Matrix<Celltype> matrixtowrite)
    {
        binarywriter.Write(matrixtowrite.Rows);
        binarywriter.Write(matrixtowrite.Colls);
        foreach (var x in matrixtowrite)
        {
            VectorReaderWriter<Celltype>.BinaryWriting(binarywriter, x);
        }

    }

    public static void Textwriting(StreamWriter twriter,Matrix<Celltype> matrixtowrite)
    {
        twriter.WriteLine(matrixtowrite.Rows);
        twriter.WriteLine(matrixtowrite.Colls);
        foreach (var x in matrixtowrite)
        {
            VectorReaderWriter<Celltype>.Textwriting(twriter, x);
        }
    }

    public static Matrix<Celltype> BinaryReading(BinaryReader binread)
    {
        try
        {
           int rows=binread.ReadInt32();
            int cols=binread.ReadInt32();
            Matrix<Celltype> outmatr = new Matrix<Celltype>(rows, cols);
            _size = rows;
            VectorReaderWriter<Celltype>.SetSize(cols);
            for (int i = 1; i <= _size; i++)
            {
                outmatr.Add(VectorReaderWriter<Celltype>.BinaryReading(binread));
            }
            return outmatr;
        }
        catch
        {
            return null;
        }
    }

    public static Matrix<Celltype> TextReading(StreamReader reader)
    {
        int rows, colls;
        string dim;
        if (reader.EndOfStream == true)
            return null;
        dim=reader.ReadLine();
        if(!int.TryParse(dim,out rows))
            return null;
        rows=int.Parse(dim);
        if (reader.EndOfStream == true)
            return null;
        dim=reader.ReadLine();
        if(!int.TryParse(dim,out colls))
            return null;
        colls=int.Parse(dim);
        _size = rows;
        Matrix<Celltype> outmatr = new Matrix<Celltype>(rows, colls);
        Vector<Celltype> temp = new Vector<Celltype>(colls, outmatr);
        for (int i = 1; i <= _size; i++)
        {
            if (reader.EndOfStream == true)
                return null;
            temp = VectorReaderWriter<Celltype>.TextReading(reader);
            if (temp == null)
                return null;
            outmatr.Add(temp);
        }
        return outmatr;
    }

    public static void Save(Matrix<Celltype> x, string file)
    {
        using (var temp = new GZipStream(File.Open(file, FileMode.Create, FileAccess.Write, FileShare.None), CompressionMode.Compress))
        {
            var bstream = new BinaryWriter(temp);
            BinaryWriting(bstream, x);
        }
    }

    public static void Read(Matrix<Celltype> x, string file)
    {
        using (var temp = new GZipStream(File.Open(file, FileMode.Open, FileAccess.Read, FileShare.Read), CompressionMode.Decompress))
        {
            var bstream = new BinaryReader(temp);
            x = BinaryReading(bstream);
        }
    }

    public static void CryptoSave(Matrix<Celltype> x, string file, bool binary)
    {
        TripleDESCryptoServiceProvider tdes = new TripleDESCryptoServiceProvider();
        tdes.GenerateKey();
        tdes.GenerateIV();
        Array.Resize(ref keys, tdes.KeySize);
        Array.Resize(ref iv, tdes.KeySize);
        Array.Copy(keys, tdes.Key, tdes.KeySize);
        Array.Copy(iv, tdes.IV, tdes.KeySize);
        var enscrypt = tdes.CreateEncryptor(tdes.Key, tdes.IV);
        using (var filestream = new FileStream(file, FileMode.Create))
        {
            using (var cryptostream = new CryptoStream(filestream, enscrypt, CryptoStreamMode.Write))
            {
                using (var deflatestream = new DeflateStream(cryptostream, CompressionMode.Compress))
                {
                    if (binary)
                    {
                        using (var bwriter = new BinaryWriter(deflatestream))
                        {
                            BinaryWriting(bwriter, x);
                        }
                    }
                    else
                    {
                        using (var writer = new StreamWriter(deflatestream))
                        {
                            Textwriting(writer, x);
                        }
                    }
                }
            }
        }
    }

    public static void CryptoLoad(Matrix<Celltype> x, string file, bool binary)
    {
        TripleDESCryptoServiceProvider tdes = new TripleDESCryptoServiceProvider();
        var enscrypt = tdes.CreateDecryptor(keys, iv);
        using (var filestream = new FileStream(file, FileMode.Open))
        {
            using (var cryptostream = new CryptoStream(filestream, enscrypt, CryptoStreamMode.Read))
            {
                using (var deflatestream = new DeflateStream(cryptostream, CompressionMode.Decompress))
                {
                    if (binary)
                    {
                        using (var breader = new BinaryReader(deflatestream))
                        {
                            x = BinaryReading(breader);
                        }
                    }
                    else
                    {
                        using (var reader = new StreamReader(deflatestream))
                        {
                            x = TextReading(reader);
                        }
                    }
                }
            }
        }
    }
}