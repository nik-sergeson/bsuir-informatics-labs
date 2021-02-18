using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using IDAL;

namespace DAL
{
    public class StationReaderWriter:IStationStorable,IStorable<Station>
    {
        private string filename = "data/stations.xml";

        public StationReaderWriter()
        {
            if (File.Exists(filename) == false)
            {
                XDocument doc = new XDocument(new XDeclaration("1.0", "utf-8", "yes"));
                doc.AddFirst(new XElement("Stations"));
                doc.Save(filename);
            }
        }

        public void Add(Station station)
        {
            XDocument doc = XDocument.Load(filename);
            doc.Root.Add(new XElement("Station", new XElement("DepartingTime", station.DepartingTime.ToString()), new XElement("ArrivalTime", station.ArrivalTime.ToString()), new XElement("Name", station.Name), new XElement("Country", station.Country),new XElement("ID",station.ID)));
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

        public void Update(Station station)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Element("ID").Value) == station.ID)
                {
                    elem.SetElementValue("DepartingTime", station.DepartingTime.ToString());
                    elem.SetElementValue("ArrivalTime", station.ArrivalTime.ToString());
                    elem.SetElementValue("Name", station.Name);
                    elem.SetElementValue("Country",station.Country);
                    break;
                }
            doc.Save(filename);
        }

        public List<Station> ReadAll()
        {
            List<Station> lstf = new List<Station>();
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
            {
                lstf.Add(new Station() { ID = int.Parse(elem.Element("ID").Value), DepartingTime = DateTime.Parse(elem.Element("DepartingTime").Value), ArrivalTime = DateTime.Parse(elem.Element("ArrivalTime").Value), Name = elem.Element("Name").Value, Country = elem.Element("Country").Value });
            }
            return lstf;
        }

        public Station Read(int id)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
            {
                if (int.Parse(elem.Element("ID").Value) == id)
                {
                    return(new Station() { ID = int.Parse(elem.Element("ID").Value), DepartingTime = DateTime.Parse(elem.Element("DepartingTime").Value), ArrivalTime = DateTime.Parse(elem.Element("ArrivalTime").Value), Name = elem.Element("Name").Value, Country = elem.Element("Country").Value });
                }
            }
            return null;
        }
    }
}
