using System;

namespace FileSavers
{
    public interface IDocStorage
    {
        void Save(string path, PlayList list);
        PlayList Load(string path);
    }
}