using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace MyTowerDefence
{
    public class MenuButton:StaticSprite
    {
        public GameState state{get;set;}

        public MenuButton(Texture2D textureImage, Vector2 position, float layerdepth, GameState state)
            : base(textureImage, position, layerdepth)
        {
            this.state = state;
        }
    }
}
