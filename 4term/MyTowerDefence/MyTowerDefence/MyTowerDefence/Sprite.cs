using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace MyTowerDefence
{
    [Serializable]
    abstract public class Sprite
    {
        [NonSerialized]
        protected Texture2D textureImage;
        protected Vector2 speed;
        protected Vector2 position;
        protected float LayerDepth;

        public Vector2 Position
        {
            get { return position; }
        }

        public abstract Vector2 direction
        {
            get;
        }
        public Rectangle collisionRect
        {
            get
            {
                return new Rectangle((int)position.X,(int)position.Y,
                    textureImage.Width,textureImage.Height);
            }
        }

        public Sprite()
        {
            speed = Vector2.Zero;
            position = Vector2.Zero;
            LayerDepth = 1;
        }

        public Sprite(Texture2D textureImage, Vector2 position,Vector2 speed,float layerdepth)
        {
            this.textureImage = textureImage;
            this.position = position;
            this.speed = speed;
            LayerDepth = layerdepth;
        }

        public virtual void Update(GameTime gameTime)
        {
            
        }

        public static bool Collide(Rectangle enemerect,Rectangle collisionRect)
        {
            return enemerect.Intersects(new Rectangle(collisionRect.X, collisionRect.Y, 0, 0));
        }

        public bool Collide(Rectangle enemerect)
        {
            return collisionRect.Intersects(enemerect);
        }

        public virtual void Draw(SpriteBatch spriteBatch)
        {
            spriteBatch.Draw(textureImage, position, null, Color.White, 0, Vector2.Zero, 1, SpriteEffects.None, LayerDepth);
        }
    }
}
