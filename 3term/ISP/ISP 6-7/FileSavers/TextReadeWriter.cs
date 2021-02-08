using System;
using System.IO;

namespace FileSavers
{
    public class TextReaderWriter : IDocStorage
    {
        public void Save(string filename, PlayList playlist)
        {
            using (var filestream = new FileStream(filename, FileMode.Create))
            {
                using (var textwriter = new StreamWriter(filestream))
                {
                    textwriter.Write(playlist.Name);
                    textwriter.Write(playlist.ID);
                    textwriter.Write(playlist.Count());
                    foreach (var song in playlist)
                    {
                        textwriter.Write(song.ID);
                        textwriter.Write(song.Name);
                        textwriter.Write(song.Duraction.ToString());
                        textwriter.Write(song.Singer);
                        textwriter.Write(song.genre.ToString());
                        textwriter.Write(song.Raiting);
                    }
                }
            }
        }

        public PlayList Load(string filename)
        {
            PlayList pl;
            try
            {
                using (var filestream = new FileStream(filename, FileMode.Open))
                {
                    using (var textreader = new StreamReader(filestream))
                    {
                        string name = textreader.ReadLine();
                        pl = new PlayList(name);
                        pl.SetID(UInt32.Parse(textreader.ReadLine()));
                        int count = Int32.Parse(textreader.ReadLine());
                        for (int i = 1; i <= count; i++)
                        {
                            uint id = UInt32.Parse(textreader.ReadLine());
                            string sname = textreader.ReadLine();
                            TimeSpan duraction = TimeSpan.Parse(textreader.ReadLine());
                            string singer = textreader.ReadLine();
                            Genre genre = (Genre)Enum.Parse(typeof(Genre), textreader.ReadLine());
                            byte raiting = byte.Parse(textreader.ReadLine());
                            Song song = new Song(sname, singer, raiting, duraction, genre);
                            song.SetID(id);
                            pl.AddSong(song);
                        }
                    }
                }
            }
            catch
            {
                return null;
            }
            return pl;
        }
    }
}