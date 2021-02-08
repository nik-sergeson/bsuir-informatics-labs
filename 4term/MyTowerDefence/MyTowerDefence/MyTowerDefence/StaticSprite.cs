using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace MyTowerDefence
{
    [Serializable]
    public class StaticSprite:Sprite
    {
        public override Vector2 direction
        {
            get { return Vector2.Zero; }
        }

        public Texture2D textureimage
        {
            get { return textureImage; }
            set { textureImage = value; }
        }

        public bool BelongToSprite(float x, float y)
        {
            return (((x - position.X <= collisionRect.Width) && (x - position.X >= 0)) && ((y - position.Y <= collisionRect.Height) && (y - position.Y >= 0)));
        }

        public StaticSprite()
        {
            position = Vector2.Zero;
            LayerDepth = 1;
        }

        public StaticSprite(Texture2D textureImage, Vector2 position,float layerdepth)
        {
            this.textureImage = textureImage;
            this.position = position;
            this.LayerDepth = layerdepth;
        }
    }
}
