using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.Serialization.Formatters.Binary;
using System.Runtime.Serialization;
using System.IO;
using System.Xml.Serialization;

namespace MyTowerDefence
{
    public static class GameSaver<T>
    {
        public static void Save(T obj,string filename)
        {
            var formatter = new BinaryFormatter();
            using (Stream s = File.Create(filename))
            {
                formatter.Serialize(s, obj);
            }
        }

        public static T Read(string filename)
        {
            T newobjs;
            var formatter = new BinaryFormatter();
            using (Stream s = File.OpenRead(filename))
            {
                newobjs = (T)formatter.Deserialize(s);
            }
            return newobjs;
        }
    }
}
