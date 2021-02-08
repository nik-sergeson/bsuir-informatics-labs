using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

public class StartCommand : Icommand
{
    private string _playlist;

    public StartCommand(string playlist)
    {
        _playlist = playlist;
    }

    public void Execute(Player player)
    {
        PlayList playlist = player.Playlists.Find((x) => x.Name == _playlist);
        Thread[] thread;
        ManualResetEvent listmre;
        player.threadsevents.TryGetValue(_playlist,out listmre);
        player.playlistthread.TryGetValue(_playlist, out thread);
        if (playlist != null)
        {
            if (thread[0] != null)
            {
                if (thread[0].ThreadState == ThreadState.WaitSleepJoin)
                {
                    thread[0].Interrupt();
                }
                else
                {
                    thread[0].Abort();
                }
            }
            if (thread[1] != null)
            {
                if (thread[1].ThreadState == ThreadState.WaitSleepJoin)
                {
                    thread[1].Interrupt();
                }
                else
                {
                    thread[1].Abort();
                }
            }
            if (playlist.sequentialplay==true)
            {
                thread[0] = new Thread(playlist.SequentialPlaying) { IsBackground = true };
            }
            else
            {
                thread[0] = new Thread(playlist.RandomPlaying) { IsBackground = true };
            }
            thread[0].Start(new ThreadResetEvent() { curthread = thread[1], MRE = listmre });
        }
    }
}

