using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.IO.Compression;
using System.Security;
using System.Security.Cryptography;

static class VectorReaderWriter<Celltype>
    where Celltype : struct
{
    static byte[] keys, iv;
    private static int _size;

    public static void SetSize(int size)
    {
        _size = size;
    }

    public static void BinaryWriting(BinaryWriter binarywriter,Vector<Celltype> vectortowrite)
    {
            foreach (var x in vectortowrite)
            {
                CellReaderWriter<Celltype>.BinaryWriting(binarywriter, x);
            }
       
    }

    public static void Textwriting(StreamWriter twriter, Vector<Celltype> vectortowrite)
    {
        foreach (var x in vectortowrite)
        {
            CellReaderWriter<Celltype>.Textwriting(twriter, x);
        }
    }

    public static Vector<Celltype> BinaryReading(BinaryReader binread)
    {
        try
        {
            Vector<Celltype> rvect=new Vector<Celltype>(_size,null);
            for (int i = 1; i <= _size; i++)
            {
                rvect.AddVec(CellReaderWriter<Celltype>.BinaryReading(binread));
            }
            return rvect;
        }
        catch
        {
            return null;
        }
    }

    public static Vector<Celltype> TextReading(StreamReader reader)
    {
        Cell<Celltype> Temp;
        Vector<Celltype> outvec = new Vector<Celltype>(_size, null);
        for (int i = 1; i <= _size; i++)
        {
            if (reader.EndOfStream == true)
                return null;
            Temp = CellReaderWriter<Celltype>.TextReading(reader);
            if (Temp == null)
                return null;
            outvec.AddVec(Temp);

        }
        return outvec;
    }

    public static void Save(Vector<Celltype> x, string file)
    {
        using (var temp = new GZipStream(File.Open(file, FileMode.Create, FileAccess.Write, FileShare.None), CompressionMode.Compress))
        {
            var bstream = new BinaryWriter(temp);
            BinaryWriting(bstream, x);
        }
    }

    public static void Read(Vector<Celltype> x, string file)
    {
        using (var temp = new GZipStream(File.Open(file, FileMode.Open, FileAccess.Read, FileShare.Read), CompressionMode.Decompress))
        {
            var bstream = new BinaryReader(temp);
            x = BinaryReading(bstream);
        }
    }

    public static void CryptoSave(Vector<Celltype> x, string file, bool binary)
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

    public static void CryptoLoad(Vector<Celltype> x, string file, bool binary)
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