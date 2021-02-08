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
    public class FlightReaderWriter:IFlightStorable,IStorable<Flight>
    {
        private string filename = "data/flights.xml";

        public FlightReaderWriter()
        {
            if (File.Exists(filename) == false)
            {
                XDocument doc = new XDocument(new XDeclaration("1.0", "utf-8", "yes"));
                doc.AddFirst(new XElement("Flights"));
                doc.Save(filename);
            }
        }

        public void Add(Flight flight)
        {
            XDocument doc = XDocument.Load(filename);
            doc.Root.Add(new XElement("Flight", new XElement("ID",flight.ID), new XElement("Cost",flight.Cost),new XElement("DepartingPoint",flight.DepartingPoint),new XElement("ArrivalPoint",flight.ArrivalPoint)));
            doc.Save(filename);
        }

        public void Delete(int id)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Element("ID").Value) == id)
                {
                    elem.Remove();
                    break;
                }
            doc.Save(filename);
        }

        public void Update(Flight flight)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Element("ID").Value) == flight.ID)
                {
                    elem.SetElementValue("Cost", flight.Cost);
                    elem.SetElementValue("DepartingPoint", flight.DepartingPoint);
                    elem.SetElementValue("ArrivalPoint", flight.ArrivalPoint);
                    break;
                }
            doc.Save(filename);
        }

        public List<Flight> ReadAll()
        {
            List<Flight> lstf = new List<Flight>();
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
            {
                lstf.Add(new Flight(int.Parse(elem.Element("ID").Value),int.Parse(elem.Element("Cost").Value), int.Parse(elem.Element("DepartingPoint").Value), int.Parse(elem.Element("ArrivalPoint").Value)));
            }
            return lstf;
        }

        public Flight Read(int id)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
            {
                if (int.Parse(elem.Element("ID").Value) == id)
                {
                    return (new Flight(int.Parse(elem.Element("ID").Value), int.Parse(elem.Element("Cost").Value), int.Parse(elem.Element("DepartingPoint").Value), int.Parse(elem.Element("ArrivalPoint").Value)));
                }
            }
            return null;
        }
    }
    
}
