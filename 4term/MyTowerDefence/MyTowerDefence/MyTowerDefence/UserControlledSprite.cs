using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;


namespace MyTowerDefence
{
    public class UserControlledSprite:Sprite
    {
        public override Vector2 direction
        {
            get { return speed; }
        }

        public BuildingType curtower { get; set; }
        public bool towerischosen { get; set; }
        private MouseState prevMouseState;
        public Texture2D image { get { return textureImage; } set { textureImage = value; } }

        public UserControlledSprite(Texture2D textureImage, Vector2 position,Vector2 speed,float layerdepth): base(textureImage, position,speed,layerdepth)
        {
            towerischosen = false;
        }

        public override void Update(GameTime gameTime)
        {
            if (towerischosen == true)
            {
                MouseState currMouseState = Mouse.GetState();
                if (currMouseState.X != prevMouseState.X || currMouseState.Y != prevMouseState.Y)
                {
                    position = new Vector2(currMouseState.X - textureImage.Width / 2, currMouseState.Y - textureImage.Height / 2);
                }
                prevMouseState = currMouseState;
                if (position.X < 0)
                    position.X = 0;
                if (position.Y < 0)
                    position.Y = 0;
                base.Update(gameTime);
            }
        }
    }
}
