using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using System.Xml.Linq;

class VectorToXml<DataType>:Vector<DataType>
    where DataType:struct
{
    public void SequentalProc(string filename)
    {
        var settings = new XmlWriterSettings { Indent = true };
        using (var writer = XmlWriter.Create(filename, settings))
        {
            writer.WriteStartDocument();
            writer.WriteStartElement("vector");
            writer.WriteAttributeString("elementcount", Numbers.Count.ToString());
            foreach (var elem in this)
            {               
                writer.WriteStartElement("element");
                writer.WriteAttributeString("count", Numbers.FindIndex(x=>x==elem).ToString());
                writer.WriteAttributeString("Value", elem.ToString());
                writer.WriteEndElement();
            }
            writer.WriteEndElement();
            writer.WriteEndDocument();
        }
    }
    public static VectorToXml<DataType> ParseXMLSequentially(string xmlfile)
    {
        var settings = new XmlReaderSettings { IgnoreWhitespace = true };
        try
        {
            using (var reader = XmlReader.Create(xmlfile, settings))
            {
                 int temp;
                 int colc;
                 reader.Read();
                 if (reader.Name != "vector")
                    return null;
                 if (reader.AttributeCount != 1)
                    return null;
                 if (!Int32.TryParse(reader.GetAttribute(0), out colc))
                     return null;
                 colc= Int32.Parse(reader.GetAttribute(0));             
                 var newvec = new VectorToXml<DataType>();
                 for (int j = 1; j <= colc; j++)
                 {
                     reader.Read();
                     if (reader.Name != "element")
                         return null;
                     if (reader.AttributeCount != 2)
                         return null;
                     if (!Int32.TryParse(reader.GetAttribute(0), out temp))
                         return null;
                     temp = Int32.Parse(reader.GetAttribute(0));
                     if (temp > colc)
                         return null;
                     if (Cell<DataType>.TryParse(reader.GetAttribute(1)) == false)
                         return null;
                     var newelem = new Cell<DataType>() { _value = Cell<DataType>.Parse(reader.GetAttribute(1)) };
                     newvec.AddVec(newelem);
                 }
                 return newvec;
             }         
        }
    
     catch
     {
         return null;
     }
    }

    public string VectorLINQXML(string filename)
    {
        int i=0;
        var d = new XDeclaration("1.0", "utf-8", "yes");
        XElement[] cellarr = new XElement[Numbers.Count];
        foreach (var elem in this)
        {                     
           cellarr[i++] = new XElement("element", new XAttribute("value", elem.ToString()));
        }
        XDocument doc = new XDocument(d, new XElement("vector", new XAttribute("elemcount", Numbers.Count.ToString())));
        doc.Save(filename, SaveOptions.None);
        return doc.ToString();
    }

    public static VectorToXml<DataType> VectorParseLINQXML(string filename)
    {
        var xml = XDocument.Load(filename);
        var attrb = xml.Root.Attributes();
        VectorToXml<DataType> vec = new VectorToXml<DataType>();
        vec.Numbers.Capacity= Int32.Parse(attrb.First<XAttribute>(x => x.Name.Equals("elemcount")).Value);
        foreach (var cell in xml.Root.Elements())
        {
            vec.Add(new Cell<DataType>() { _value = Cell<DataType>.Parse(cell.Attribute("value").Value) });
        }
        return vec;
    }

    public void VecToDOMXM(string filename)
    {
        XmlDocument doc = new XmlDocument();
        XmlElement root = doc.CreateElement("vector");
        root.SetAttribute("elemtcount", Numbers.Count.ToString());
        foreach (var cell in this)
        {
            XmlElement cellnode = doc.CreateElement("element");
            cellnode.SetAttribute("Value", cell.ToString());
            root.AppendChild(cellnode);
        }
        var settings = new XmlWriterSettings { Indent = true };
        using (var writer = XmlWriter.Create(filename, settings))
        {
            doc.Save(writer);
        }
    }

    public static VectorToXml<DataType> ParseXMLDOM(string filename)
    {
        try
        {
            XmlDocument doc = new XmlDocument();
            doc.Load(filename);
            XmlElement root = doc.DocumentElement;
            var rows = Int32.Parse(root.GetAttribute("elementcount"));
            var vec = new VectorToXml<DataType>();
            foreach (XmlNode cellnode in root)
            {
                vec.AddVec(new Cell<DataType> { _value = Cell<DataType>.Parse(cellnode.InnerText) });
            }
            return vec;
        }
        catch
        {
            return null;
        }
    }
}