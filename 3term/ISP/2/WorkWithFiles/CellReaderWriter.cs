using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.IO.Compression;
using System.Security;
using System.Security.Cryptography;

static class CellReaderWriter<Celltype>
    where Celltype : struct
{
    static byte[] keys, iv;
    public static void BinaryWriting(BinaryWriter binarywriter, Cell<Celltype> celltowrite)
    {
        binarywriter.Write(celltowrite.ToString());
    }

    public static void Textwriting(StreamWriter twriter, Cell<Celltype> celltowrite)
    {
        twriter.WriteLine(celltowrite.ToString());
    }

    public static Cell<Celltype> BinaryReading(BinaryReader binread)
    {
        try
        {
            string value;

            value = binread.ReadString();
            Cell<Celltype> outcell = new Cell<Celltype>();
            outcell._value = Cell<Celltype>.Parse(value);
            return outcell;
        }
        catch
        {
            return null;
        }
    }

    public static Cell<Celltype> TextReading(StreamReader reader)
    {
        string value;
        if (reader.EndOfStream == true)
            return null;
        value = reader.ReadLine();
        if (!Cell<Celltype>.TryParse(value))
            return null;
        Cell<Celltype> outcell = new Cell<Celltype>();
        outcell._value = Cell<Celltype>.Parse(value);
        return outcell;
    }

    public static void Save(Cell<Celltype> x, string file)
    {
        using (var temp = new GZipStream(File.Open(file, FileMode.Create, FileAccess.Write, FileShare.None), CompressionMode.Compress))
        {
            var bstream = new BinaryWriter(temp);
            BinaryWriting(bstream, x);
        }
    }

    public static void Read(Cell<Celltype> x, string file)
    {
        using (var temp = new GZipStream(File.Open(file, FileMode.Open, FileAccess.Read, FileShare.Read), CompressionMode.Decompress))
        {
            var bstream = new BinaryReader(temp);
            x=BinaryReading(bstream);
        }
    }

    public static void CryptoSave(Cell<Celltype> x, string file,bool binary)
    {
        TripleDESCryptoServiceProvider tdes=new TripleDESCryptoServiceProvider();
        tdes.GenerateKey();
        tdes.GenerateIV();
        Array.Resize(ref keys, tdes.KeySize);
        Array.Resize(ref iv, tdes.KeySize);
        Array.Copy(keys, tdes.Key, tdes.KeySize);
        Array.Copy(iv, tdes.IV,tdes.KeySize);
        var enscrypt=tdes.CreateEncryptor(tdes.Key,tdes.IV);        
        using (var filestream = new FileStream(file, FileMode.Create))
        {
            using (var cryptostream = new CryptoStream(filestream, enscrypt, CryptoStreamMode.Write))
            {
                using(var deflatestream=new DeflateStream(cryptostream,CompressionMode.Compress))
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

    public static void CryptoLoad(Cell<Celltype> x, string file, bool binary)
    {
        TripleDESCryptoServiceProvider tdes = new TripleDESCryptoServiceProvider();
        var enscrypt = tdes.CreateDecryptor(keys,iv);
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