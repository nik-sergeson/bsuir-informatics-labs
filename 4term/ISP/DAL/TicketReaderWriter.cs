using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;
using System.IO;
using System.Threading.Tasks;
using IDAL;

namespace DAL
{
    public class TicketReaderWriter:ITicketStorable,IStorable<Ticket>
    {
        private string filename = "data/tickets.xml";

        public TicketReaderWriter()
        {
            if (File.Exists(filename) == false)
            {
                XDocument doc = new XDocument(new XDeclaration("1.0", "utf-8", "yes"));
                doc.AddFirst(new XElement("Tickets"));
                doc.Save(filename);
            }
        }

        public void Add(Ticket ticket)
        {
            bool found = false;
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Name.LocalName) == ticket.AeroplaneID)
                {
                    elem.Add(new XElement("Ticket", new XElement("FlightID", ticket.FlightID), new XElement("OwnerID", ticket.OwnerID), new XElement("Cost", ticket.Cost), new XElement("ID", ticket.ID), new XElement("Seat", ticket.Seat)));
                    found = true;
                    break;
                }
            if(found==false)
                doc.Root.Add(new XElement(ticket.AeroplaneID.ToString(),new XElement("Ticket", new XElement("FlightID", ticket.FlightID), new XElement("OwnerID", ticket.OwnerID), new XElement("Cost", ticket.Cost), new XElement("ID", ticket.ID), new XElement("Seat", ticket.Seat))));
            doc.Save(filename);
        }

        public void Delete(int id)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (IEnumerable<XElement> tickets in doc.Root.Elements())
                foreach(XElement elem in tickets)
                if (int.Parse(elem.Element("ID").Value) == id)
                {
                    elem.Remove();
                    break;
                }
            doc.Save(filename);
        }

        public void Update(Ticket ticket)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (IEnumerable<XElement> tickets in doc.Root.Elements())
                foreach (XElement elem in tickets)
                    if (int.Parse(elem.Element("ID").Value) == ticket.ID)
                    {
                        elem.SetElementValue("FlightID", ticket.FlightID);
                        elem.SetElementValue("OwnerID", ticket.OwnerID);
                        elem.SetElementValue("Cost", ticket.Cost);
                        elem.SetElementValue("Seat", ticket.Seat);
                        break;
                    }
            doc.Save(filename);
        }

        public List<Ticket> ReadAllForPlane(int aeroplaneid)
        {
            List<Ticket> lst = new List<Ticket>();
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Element(aeroplaneid.ToString()).Elements())
                lst.Add(new Ticket() { ID = int.Parse(elem.Element("ID").Value), AeroplaneID = aeroplaneid, Cost = int.Parse(elem.Element("Cost").Value), FlightID = int.Parse(elem.Element("FlightID").Value), OwnerID = int.Parse(elem.Element("OwnerID").Value), Seat = int.Parse(elem.Element("Seat").Value) });
            return lst;
        }

        public List<Ticket> ReadAllForClient(int OwnerID)
        {
            List<Ticket> lst = new List<Ticket>();
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                foreach (XElement ticket in elem.Elements())
                    if (int.Parse(ticket.Element("OwnerID").Value) == OwnerID)
                        lst.Add(new Ticket() { ID = int.Parse(elem.Element("ID").Value), AeroplaneID = int.Parse(elem.Name.LocalName), Cost = int.Parse(elem.Element("Cost").Value), FlightID = int.Parse(elem.Element("FlightID").Value), OwnerID = int.Parse(elem.Element("OwnerID").Value), Seat = int.Parse(elem.Element("Seat").Value) });
            return lst;
        }

        public Ticket Read(int id)
        {
            List<Ticket> lst = new List<Ticket>();
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                foreach (XElement ticket in elem.Elements())
                    if (int.Parse(ticket.Element("ID").Value) == id)
                        return(new Ticket() { ID = int.Parse(elem.Element("ID").Value), AeroplaneID = int.Parse(elem.Name.LocalName), Cost = int.Parse(elem.Element("Cost").Value), FlightID = int.Parse(elem.Element("FlightID").Value), OwnerID = int.Parse(elem.Element("OwnerID").Value), Seat = int.Parse(elem.Element("Seat").Value) });
            return null;
        }

        public List<Ticket> ReadAll()
        {
            List<Ticket> lst = new List<Ticket>();
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                foreach (XElement ticket in elem.Elements())
                    lst.Add(new Ticket() { ID = int.Parse(elem.Element("ID").Value), AeroplaneID = int.Parse(elem.Name.LocalName), Cost = int.Parse(elem.Element("Cost").Value), FlightID = int.Parse(elem.Element("FlightID").Value), OwnerID = int.Parse(elem.Element("OwnerID").Value), Seat = int.Parse(elem.Element("Seat").Value) });
            return lst;
        }
    }
}
