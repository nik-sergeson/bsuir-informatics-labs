using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

public class ResumeCommand:Icommand
{
    private string _playlist;

    public ResumeCommand(string playlist)
    {
        _playlist = playlist;
    }

    public void Execute(Player player)
    {
        ManualResetEvent listmre;
        player.threadsevents.TryGetValue(_playlist, out listmre);
        listmre.Set();
    }
}