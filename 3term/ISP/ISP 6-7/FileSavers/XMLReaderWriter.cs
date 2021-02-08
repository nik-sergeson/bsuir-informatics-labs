using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;
using System.Threading.Tasks;

namespace FileSavers
{
    public class XMLReaderWriter : IDocStorage
    {
        public void Save(string Filename, PlayList playlist)
        {
            int i = 0;
            var d = new XDeclaration("1.0", "utf-8", "yes");
            XElement[] songarr = new XElement[playlist.Count()];
            foreach (var song in playlist)
            {
                songarr[i++] = new XElement("Song", new XElement("ID", song.ID, "Name", song.Name, "Duraction", song.Duraction, "Singer", song.Singer, "Genre", song.genre, "Raiting", song.Raiting));
            }
            XDocument doc = new XDocument(d, new XElement("Playlist", new XElement("Name", playlist.Name), new XElement("ID", playlist.ID), new XElement("Duraction", playlist.Duraction), new XElement("Raiting", playlist.Raiting)), songarr);
            doc.Save(Filename, SaveOptions.None);
        }

        public PlayList Load(string filename)
        {
            var doc = XDocument.Load(filename);
            string name = doc.Root.Element("Name").Value;
            PlayList list = new PlayList(name);
            var songs = doc.Root.Elements("Song");
            foreach (var song in songs)
            {
                Song nsong = new Song(song.Element("Name").Value, song.Element("Singer").Value, byte.Parse(song.Element("Raiting").Value), TimeSpan.Parse(song.Element("Duraction").Value), (Genre)Enum.Parse(typeof(Genre), song.Element("Genre").Value));
                nsong.SetID(uint.Parse(song.Element("ID").Value));
                list.AddSong(nsong);
            }
            list.SetID(uint.Parse(doc.Root.Element("ID").Value));
            return list;
        }
    }
}