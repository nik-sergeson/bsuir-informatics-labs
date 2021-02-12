using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class PlayListIDGenerator
{
    private uint _id = uint.MaxValue;

    public static PlayListIDGenerator IDGenerator { get; private set; }

    private PlayListIDGenerator() { }

    static PlayListIDGenerator()
    {
        IDGenerator = new PlayListIDGenerator();
    }

    public uint GetID()
    {
        _id--;
        return _id;
    }
}
