using System;
using System.Collections.Generic;
using System.Collections;
using System.Threading;

public class PlayList:IEnumerable<Song>
{
    private string _name;
    public uint ID{get; private set;}
    private List<Song> Songs;
    public TimeSpan Duraction { get; set; }
    private byte _raiting;
    public int cursong{get;set;}
    public bool repeat { get; set; }
    public bool sequentialplay { get; set; }

    private class PlayListEnumerator : IEnumerator<Song>
    {
        private int _position = -1;
        private List<Song> _playlist;

        public PlayListEnumerator(List<Song> songs)
        {
            _playlist = new List<Song>(songs);
        }

        public void Dispose()
        {
        }
        public Song Current
        {
            get { return _playlist[_position]; }
        }

        public bool MoveNext()
        {
            if (_position < _playlist.Count)
            {
                ++_position;
                return true;
            }
            else
            {
                return false;
            }
        }

        public void Reset()
        {
            _position = -1;
        }

        object IEnumerator.Current
        {
            get { return _playlist[_position]; }
        }
    }

    public IEnumerator<Song> GetEnumerator()
    {
        return new PlayListEnumerator(Songs);
    }

    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
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

    public PlayList(string name)
    {
        Name = name;
        ID = PlayListIDGenerator.IDGenerator.GetID();
        Duraction = new TimeSpan(0, 0, 0);
        _raiting = 0;
        Songs = new List<Song>();
        cursong=0;
        repeat = true;
        sequentialplay = true;
    }

    public void AddSong(Song song)
    {
        if (Songs.Find((x)=>x.ID.Equals(song.ID))==null)
        {
            Duraction += song.Duraction;
            _raiting = (byte)((_raiting * Songs.Count + song.Raiting) / (Songs.Count + 1));
            Songs.Add(song);
        }
    }

    public void DeleteSong(Song song)
    {
        int index = Songs.IndexOf(song);
        if (index != 0)
        {
            Duraction -= Songs[index].Duraction;
            _raiting = (byte)((_raiting * Songs.Count - Songs[index].Raiting) / (Songs.Count - 1));
            Songs.Remove(song);
        }
    }

    public int Count()
    {
        return Songs.Count;
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
                _raiting = 0;
            }
        }
    }

    public void SetID(uint id)
    {
        ID = id;
    }

    public void Play(object state)
    {
        object locker = new object();
        ManualResetEvent songmre = (ManualResetEvent)state;
        TimeSpan fsec = TimeSpan.FromSeconds(5);
        for (var currenttime = new TimeSpan(0, 0, 0); currenttime < Songs[cursong].Duraction; currenttime += fsec)
        {
            lock (locker)
            {
                Songs[cursong].Timeplayed = currenttime;
                Thread.Sleep(fsec);
                songmre.WaitOne();
            }
        }
        lock (locker)
        {
            Songs[cursong].Timeplayed = Songs[cursong].Duraction;
        }
    }

    public void SequentialPlaying(object thread)
    {
        ThreadResetEvent songthr = (ThreadResetEvent)thread;
        while (repeat)
        {
            foreach (var x in Songs)
            {
                songthr.curthread= new Thread(this.Play) { IsBackground = true };
                songthr.curthread.Start(songthr.MRE);
                songthr.curthread.Join();
                ++cursong;
            }
        }
    }

    public void RandomPlaying(object thread)
    {
        List<int> cash = new List<int>();
        Random random = new Random();
        ThreadResetEvent songthr = (ThreadResetEvent)thread;
        while (repeat)
        {
            int ransong = random.Next(Songs.Count);
            if (!cash.Contains(ransong))
            {
                cursong = ransong;
                cash.Add(ransong);
                songthr.curthread = new Thread(this.Play) { IsBackground = true };
                songthr.curthread.Start(songthr.MRE);
                songthr.curthread.Join();
            }
            if (cash.Count == Songs.Count)
            {
                cash = new List<int>();
            }
        }
    }
}