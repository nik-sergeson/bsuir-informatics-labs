using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using System.Runtime.Serialization.Formatters.Binary;
using System.Runtime.Serialization;
using System.IO;

namespace MyTowerDefence
{
    [Serializable]
    public class DeFeu:Building
    {
        public DeFeu(Texture2D textureImage, Texture2D bullettext, float X, float Y, float layerdepth, string textpath, string bullpath) :
            base(textureImage, bullettext, X, Y, layerdepth,textpath,bullpath)
        {
            attackradius = 110;
            bullattackradius = 230;
            bulldamage = 60;
            bullmaxspeed = 7;
        }
    }
}
