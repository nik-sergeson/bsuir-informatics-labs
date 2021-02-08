using System;
using System.IO; 

namespace FileSavers
{
    public class BinaryReaderWriter : IDocStorage
    {
        public void Save(string filename, PlayList playlist)
        {
            using (var filestream = new FileStream(filename, FileMode.Create))
            {
                using (var binarywriter = new BinaryWriter(filestream))
                {
                    binarywriter.Write(playlist.Name);
                    binarywriter.Write(playlist.ID);
                    binarywriter.Write(playlist.Count());
                    foreach (var song in playlist)
                    {
                        binarywriter.Write(song.ID);
                        binarywriter.Write(song.Name);
                        binarywriter.Write(song.Duraction.ToString());
                        binarywriter.Write(song.Singer);
                        binarywriter.Write(song.genre.ToString());
                        binarywriter.Write(song.Raiting);
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
                    using (var binaryreader = new BinaryReader(filestream))
                    {
                        string name = binaryreader.ReadString();
                        pl = new PlayList(name);
                        pl.SetID(binaryreader.ReadUInt32());
                        int count = binaryreader.ReadInt32();
                        for (int i = 1; i <= count; i++)
                        {
                            uint id = binaryreader.ReadUInt32();
                            string sname = binaryreader.ReadString();
                            TimeSpan duraction = TimeSpan.Parse(binaryreader.ReadString());
                            string singer = binaryreader.ReadString();
                            Genre genre = (Genre)Enum.Parse(typeof(Genre), binaryreader.ReadString());
                            byte raiting = binaryreader.ReadByte();
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