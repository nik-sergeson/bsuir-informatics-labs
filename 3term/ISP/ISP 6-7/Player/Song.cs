using System;

public class Song
{
    private string _name;
    private string _singer;
    private byte _raiting;
    private TimeSpan _timeplayed;
    public uint ID { get; private set; }
    public TimeSpan Duraction { get; private set; }
    public Genre genre { get; private set; }
    public delegate void Handler(Song csong, SongEventArgs args);
    public event Handler NowPlaying;

    public TimeSpan Timeplayed
    {
        get { return _timeplayed; }
        set
        {
            _timeplayed = value;
            if (NowPlaying != null)
            {
                NowPlaying(this, new SongEventArgs(value));
            }
        }
    }

    public Song(string name, string singer, byte raiting, TimeSpan duraction, Genre genre)
    {
        Name = name;
        Singer = singer;
        Raiting = raiting;
        Duraction = duraction;
        this.genre = genre;
        ID = SongIDGenerator.IDGenerator.GetID();
        _timeplayed=new TimeSpan(0,0,0);
    }

    public string Name
    {
        get { return _name; }
        set
        {
            if (value.Length > 255)
            {
                _name = "Noname";
            }
            else
            {
                _name = value;
            }
        }
    }

    public string Singer
    {
        get { return _singer; }
        set
        {
            if (value.Length > 255)
            {
               _singer = "Unknown";
            }
            else
            {
                _singer = value;
            }
        }
    }

    public byte Raiting
    {
        get { return _raiting; }
        set
        {
            if ((value >= 0) && (value <= 10))
            {
                _raiting = value;
            }
            else
            {
                _raiting = 10;
            }
        }
    }

    public void SetID(uint id)
    {
        ID = id;
    }
}

public enum Genre { Rock, Pop, Alternative, Rap, Punk, Metal, Folk, Classic }