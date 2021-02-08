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
    public class Map:StaticSprite
    {
        public List<Vector2> road { get; private set; }
    
        public List<Rectangle> availableplaces;

        public Map(Texture2D texture, Vector2 position, List<Vector2> road,float layerdepth)
            : base(texture, position,layerdepth)
        {
            this.road = road;
            availableplaces = new List<Rectangle>();
            availableplaces.Add(new Rectangle(20, 240, 220, 20));
            availableplaces.Add(new Rectangle(220, 220, 20, 20));
            availableplaces.Add(new Rectangle(120, 100, 240, 20));
            availableplaces.Add(new Rectangle(120, 120, 20, 20));
            availableplaces.Add(new Rectangle(340, 120, 20, 260));
            availableplaces.Add(new Rectangle(200, 0, 20, 100));
            availableplaces.Add(new Rectangle(120, 360, 240, 20));   
        }

        public Vector2 PlaceTower(int x,int y,int width,int height,List<Building> tows)
        {
            
            for (int i = 0; i < availableplaces.Count; i++)
            {
                if ((x - availableplaces[i].X) <= availableplaces[i].Width && (y - availableplaces[i].Y) <= availableplaces[i].Height && (x - availableplaces[i].X) >= 0 && (y - availableplaces[i].Y)>=0)
                {
                    if (availableplaces[i].Width < availableplaces[i].Height)
                    {
                        x = availableplaces[i].X;
                        y = availableplaces[i].Y + ((y - availableplaces[i].Y) / 20) * 20;
                    }
                    else if (availableplaces[i].Height < availableplaces[i].Width)
                    {
                        x = availableplaces[i].X + ((x - availableplaces[i].X) / 20) * 20;
                        y = availableplaces[i].Y;
                    }
                    else
                    {
                        x = availableplaces[i].X;
                        y = availableplaces[i].Y;
                    }
                    Rectangle rec=new Rectangle(x,y,width,height);
                    foreach (Building tow in tows)
                        if (tow.Collide(rec))
                            return Vector2.Zero;
                    return new Vector2(x+width/2, y+height/2);              
                }
            }
            return Vector2.Zero;
        }
        
    }
}
