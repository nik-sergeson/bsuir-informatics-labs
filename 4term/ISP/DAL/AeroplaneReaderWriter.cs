using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Xml.Linq;
using System.Text;
using System.Threading.Tasks;
using IDAL;

namespace DAL
{
    public class AeroplaneReaderWriter : IAeroplaneStorable, IStorable<Aeroplane>
    {
        private string filename = "data/aeroplanes.xml";

        public AeroplaneReaderWriter()
        {
            if (File.Exists(filename) == false)
            {
                XDocument doc = new XDocument(new XDeclaration("1.0", "utf-8", "yes"));
                doc.AddFirst(new XElement("Aeroplanes"));
                doc.Save(filename);
            }
        }

        public void Add(Aeroplane plane)
        {
            XDocument doc = XDocument.Load(filename);
            doc.Root.Add(new XElement("Aeroplane", new XElement("ID", plane.ID), new XElement("FlightID", plane.FlightID), new XElement("Capacity", plane.Capacity)));
            doc.Save(filename);
        }

        public void Delete(int ID)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Element("ID").Value) == ID)
                {
                    elem.Remove();
                    break;
                }
            doc.Save(filename);
        }

        public void Update(Aeroplane plane)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Element("ID").Value) == plane.ID)
                {
                    elem.SetElementValue("FlightID", plane.FlightID);
                    elem.SetElementValue("Capacity", plane.Capacity);
                    break;
                }
            doc.Save(filename);
        }

        public List<Aeroplane> ReadAll(int flightid)
        {
            List<Aeroplane> lst = new List<Aeroplane>();
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Element("FlightID").Value) == flightid)
                {
                    lst.Add(new Aeroplane(int.Parse(elem.Element("ID").Value), flightid, int.Parse(elem.Element("Capacity").Value)));
                }
            return lst;
        }

        public Aeroplane Read(int id)
        {
            List<Aeroplane> lst = new List<Aeroplane>();
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Element("ID").Value) == id)
                {
                    return (new Aeroplane(id, int.Parse(elem.Element("FlightID").Value), int.Parse(elem.Element("Capacity").Value)));
                }
            return null;
        }

        public List<Aeroplane> ReadAll()
        {
            List<Aeroplane> lst = new List<Aeroplane>();
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                lst.Add(new Aeroplane(int.Parse(elem.Element("ID").Value), int.Parse(elem.Element("FlightID").Value), int.Parse(elem.Element("Capacity").Value)));
            return lst;
        }
    }
}
