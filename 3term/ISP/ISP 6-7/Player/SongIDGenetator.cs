using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class SongIDGenerator
{
    private uint _id = 0;

    static SongIDGenerator()
    {
        IDGenerator = new SongIDGenerator();
    }

    private SongIDGenerator() { }

    public static SongIDGenerator IDGenerator { get; private set; }

    public uint GetID()
    {
        _id++;
        return _id;
    }
}
