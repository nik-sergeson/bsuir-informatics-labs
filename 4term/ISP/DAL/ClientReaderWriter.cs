using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using IDAL;

namespace DAL
{
    public class ClientReaderWriter:IClientStorable,IStorable<Client>
    {
        private string filename = "data/clients.xml";

        public ClientReaderWriter()
        {
            if(File.Exists(filename)==false){
                XDocument doc = new XDocument(new XDeclaration("1.0", "utf-8", "yes"));
                doc.AddFirst(new XElement("Clients"));
                doc.Save(filename);
            }
        }

        public void Add(Client client)
        {
            XDocument doc = XDocument.Load(filename);
            doc.Root.Add(new XElement("Client", new XElement("Name", client.Name), new XElement("ID", client.ID)));
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

        public void Update(Client client)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Element("ID").Value) == client.ID)
                {
                    elem.SetElementValue("Name", client.Name);
                    break;
                }
            doc.Save(filename);
        }

        public Client Read(int id)
        {
            XDocument doc = XDocument.Load(filename);
            foreach (XElement elem in doc.Root.Elements())
                if (int.Parse(elem.Element("ID").Value) ==id)
                {
                    return new Client() { ID = id, Name = elem.Element("Name").Value };
                }
            return null;
        }

        public List<Client> ReadAll()
        {
            XDocument doc = XDocument.Load(filename);
            List<Client> lst = new List<Client>();
            foreach (XElement elem in doc.Root.Elements())
                lst.Add(new Client() { ID  =int.Parse(elem.Element("ID").Value), Name = elem.Element("Name").Value });
            return lst;
        }
    }
}
