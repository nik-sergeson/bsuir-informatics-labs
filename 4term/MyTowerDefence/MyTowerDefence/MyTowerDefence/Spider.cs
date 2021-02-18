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

namespace MyTowerDefence
{
    [Serializable]
    public class Spider:Enemy
    {
        public Spider(Texture2D textureImage, GraphicsDevice gdevice, Vector2 position, float layerdepth, List<Vector2> road, string textpath)
            : base(textureImage, gdevice, position, (float)2.2, layerdepth, road,textpath)
        {
            healthpoints = 300;
            fullhealth = healthpoints;
            cost = 25;
        }
    }
}
