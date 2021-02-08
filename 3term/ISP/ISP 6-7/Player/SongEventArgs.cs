using System;

public class SongEventArgs
{
    public TimeSpan currenttime { get; set; }
    public SongEventArgs(TimeSpan currenttime)
    {
        this.currenttime = currenttime;
    }
}