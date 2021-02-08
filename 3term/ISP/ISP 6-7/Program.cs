using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;


namespace ISP_6_7
{
    class Program
    {
        static void Main(string[] args)
        {
            Song song1 = new Song("Track1", "Singer1", 7, new TimeSpan(0, 3, 20), Genre.Alternative);
            Song song2 = new Song("Track2", "Singer2", 10, new TimeSpan(0, 2, 49), Genre.Classic);
            Song song3 = new Song("Track3", "Singer3", 5, new TimeSpan(0, 4, 44), Genre.Pop);
            Song song4 = new Song("Track4", "Singer4", 8, new TimeSpan(0, 2, 55), Genre.Punk);
            song1.NowPlaying += PerformPlay;
            song2.NowPlaying += PerformPlay;
            song3.NowPlaying += PerformPlay;
            song4.NowPlaying += PerformPlay;
            song1.Timeplayed = new TimeSpan(0, 0, 0);
            PlayList plist1 = new PlayList("MorningList");
            PlayList plist2 = new PlayList("SadList");
            plist1.AddSong(song1);
            plist1.AddSong(song2);
            plist2.AddSong(song3);
            plist2.AddSong(song4);
            Lazy<Player> myplayer = new Lazy<Player>();
            myplayer.Value.Add(plist1);
            myplayer.Value.Add(plist2);
            myplayer.Value.Execute(new StartCommand(plist1.Name));
            myplayer.Value.Execute(new StartCommand(plist1.Name));
            Console.ReadKey();
        }

        public static void PerformPlay(Song song, SongEventArgs args)
        {
            Console.WriteLine("{0}-{1}-{2}", song.Name, song.Duraction, args.currenttime);
        }
    }
}
