using System;
using System.Threading;
using System.Collections.Generic;

public class Player
{
    public List<PlayList> Playlists { get; private set; }
    public Dictionary<string,Thread[]> playlistthread{get; private set;}
    public Dictionary<string, ManualResetEvent> threadsevents { get; private set; }

    public Player()
    {
        Playlists = new List<PlayList>();
        playlistthread = new Dictionary<string, Thread[]>();
        threadsevents = new Dictionary<string, ManualResetEvent>();
    }

    public void Add(PlayList list)
    {
        if (list != null && Playlists.Find((x) => x.ID == list.ID) == null)
        {
            Playlists.Add(list);
            playlistthread.Add(list.Name, new Thread[2]);
            threadsevents.Add(list.Name, new ManualResetEvent(true));
        }
    }

    public void Execute(Icommand command)
    {
        command.Execute(this);
    }
}