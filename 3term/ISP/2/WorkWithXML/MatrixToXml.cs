using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using System.Xml.Linq;

public class MatrixToXml<Datatype> : Matrix<Datatype>
    where Datatype:struct
{
    public void SequentalProc(string filename)
    {
        var settings = new XmlWriterSettings { Indent = true };
        using (var writer = XmlWriter.Create(filename, settings))
        {
            writer.WriteStartDocument();
            writer.WriteStartElement("matrix");
            writer.WriteAttributeString("rows", Rows.ToString());
            writer.WriteAttributeString("cols", Colls.ToString());
            foreach (var row in this)
            {
                writer.WriteStartElement("Row");
                writer.WriteAttributeString("Count", this.Find(row).ToString());
                foreach (var elem in row)
                {
                    writer.WriteStartElement("Element");
                    writer.WriteAttributeString("Value", elem.ToString());
                    writer.WriteEndElement();
                }
                writer.WriteEndElement();
            }
            writer.WriteEndElement();
            writer.WriteEndDocument();
        }
    }

    public static MatrixToXml<Datatype> ParseXMLSequentially(string xmlfile)
    {
        var settings=new XmlReaderSettings{ IgnoreWhitespace = true };
        try
        {
            using (var reader = XmlReader.Create(xmlfile, settings))
            {
                reader.Read();
                reader.Read();
                if (reader.Name != "matrix")
                    return null;
                if (reader.AttributeCount != 2)
                    return null;
                int rowc, colc;
                if ((!Int32.TryParse(reader.GetAttribute(0), out rowc)) || (!Int32.TryParse(reader.GetAttribute(1), out colc)))
                    return null;
                rowc = Int32.Parse(reader.GetAttribute(0));
                colc = Int32.Parse(reader.GetAttribute(1));
                var newmatr = new MatrixToXml<Datatype>();
                for (int i = 1; i < rowc; i++)
                {
                    int temp;
                    reader.Read();
                    if (reader.Name != "Row")
                        return null;
                    if (reader.AttributeCount != 1)
                        return null;
                    if (!Int32.TryParse(reader.GetAttribute(0), out temp))
                        return null;
                    temp = Int32.Parse(reader.GetAttribute(0));
                    if (temp >= rowc)
                        return null;
                    var newvec = new VectorToXml<Datatype>();
                    for (int j = 1; j <= colc; j++)
                    {
                        reader.Read();
                        if (reader.Name != "Element")
                            return null;
                        if (reader.AttributeCount != 1)
                            return null;
                        if (Cell<Datatype>.TryParse(reader.GetAttribute(0)) == false)
                            return null;
                        var newelem = new Cell<Datatype>() { _value = Cell<Datatype>.Parse(reader.GetAttribute(0)) };
                        newvec.AddVec(newelem);
                    }
                    newmatr.Add(newvec);
                }
                return newmatr;
            }
        }
        catch
        {
            return null;
        } 
    }

    public string MatrixLINQXML(string filename)
    {
        int i, j = 0 ;
        var d = new XDeclaration("1.0", "utf-8", "yes");
        XElement[] vecarr = new XElement[Rows];
        foreach (var vec in this)
        {
            i = 0;
            XElement[] cellarr = new XElement[Colls];
            foreach (var elem in vec)
            {
                cellarr[i++] = new XElement("Element", new XAttribute("value", elem.ToString()));
            }
            vecarr[j++]=new XElement("Row",new XAttribute("Count",this.Find(vec).ToString()),cellarr);
        }
        XDocument doc =new XDocument(d, new XElement("Matrix", new XAttribute("rows", Rows.ToString()), new XAttribute("cols", Colls.ToString()), vecarr));
        doc.Save(filename, SaveOptions.None);
        return doc.ToString();
    }

    public static MatrixToXml<Datatype> MatrixParseLINQXML(string filename)
    {
        var xml = XDocument.Load(filename);
        var attrb = xml.Root.Attributes();
        try
        {
            MatrixToXml<Datatype> matr = new MatrixToXml<Datatype>();
            matr.Rows = Int32.Parse(attrb.First<XAttribute>(x => x.Name.Equals("rows")).Value);
            matr.Colls = Int32.Parse(attrb.First<XAttribute>(x => x.Name.Equals("cols")).Value);
            foreach (IEnumerable<XElement> row in xml.Root.Elements())
            {
                var newrow = new Vector<Datatype>(matr.Colls, null);
                foreach (var cell in row)
                {
                    newrow.AddVec(new Cell<Datatype>() { _value = Cell<Datatype>.Parse(cell.Attribute("value").Value) });
                }
                matr.Add(newrow);
            }
            return matr;
        }
        catch
        {
            return null;
        }
    }

    public void MatrToDOMXM(string filename)
    {
        XmlDocument doc = new XmlDocument();
        XmlElement root = doc.CreateElement("matrix");
        root.SetAttribute("rows", Rows.ToString());
        root.SetAttribute("cols", Colls.ToString());
        foreach (var row in this)
        {
            XmlElement xmlrow=doc.CreateElement("Row");
            xmlrow.SetAttribute("Count", this.Find(row).ToString());
            foreach (var cell in row)
            {
                XmlElement cellnode = doc.CreateElement("Element");
                cellnode.SetAttribute("Value", cell.ToString());
                xmlrow.AppendChild(cellnode);
            }
            root.AppendChild(xmlrow);
        }
        var settings = new XmlWriterSettings { Indent = true };
        using (var writer = XmlWriter.Create(filename, settings))
        {
            doc.Save(writer);
        }
    }

    public static MatrixToXml<Datatype> ParseXMLDOM(string filename)
    {
        try
        {
            XmlDocument doc = new XmlDocument();
            doc.Load(filename);
            XmlElement root = doc.DocumentElement;
            var rows=Int32.Parse(root.GetAttribute("rows"));
            var cols=Int32.Parse(root.GetAttribute("cols"));
            var matr = new MatrixToXml<Datatype>();
            foreach (XmlNode vecnode in root)
            {
                var vec = new Vector<Datatype>(cols, null);
                foreach (XmlNode cellnode in vecnode)
                {
                    vec.AddVec(new Cell<Datatype> { _value = Cell<Datatype>.Parse(cellnode.InnerText) });
                }
                matr.Add(vec);
            }
            return matr;
        }
        catch
        {
            return null;
        }
    }

    public static void AddRow(Vector<Datatype> vec, string filename)
    {
        try
        {
            XmlDocument doc = new XmlDocument();
            doc.Load(filename);
            XmlElement newelem = doc.CreateElement("Row");
            XmlElement root = doc.DocumentElement;
            int count = Int32.Parse(root.GetAttribute("rows")) + 1;
            root.SetAttribute("rows", count.ToString());
            newelem.SetAttribute("Count", (count).ToString());
            foreach (var x in vec)
            {
                var cell = doc.CreateElement("Element");
                cell.SetAttribute("value", x.ToString());
                newelem.AppendChild(cell);
            }
            root.AppendChild(newelem);
            doc.Save(filename);
        }
        catch
        {
            return;
        }
    }

    public static List<Datatype> Search(string filename, Datatype value)
    {
        var retlist = new List<Datatype>();
        XmlDocument doc = new XmlDocument();
        try
        {
            doc.Load(filename);
        }
        catch
        {
            return null;
        }
        XmlNodeList values = doc.GetElementsByTagName("Element");
        foreach (XmlNode x in values)
        {
            if (x.Value == value.ToString())
            {
                retlist.Add(Cell<Datatype>.Parse(x.Value));
            }
        }
        return retlist;
    }

    public static void RemoveVector(string filename, int count)
    {
        XmlDocument doc = new XmlDocument();
        try
        {
            doc.Load(filename);
        }
        catch
        {
            return;
        }
        var root = doc.DocumentElement;
        XmlNodeList rows = doc.GetElementsByTagName("Row");
        foreach (XmlNode node in rows)
        {
            if (node.Value == count.ToString())
            {
                node.RemoveAll();
                root.RemoveChild(node);
            }
        }
        doc.Save(filename);
    }
}